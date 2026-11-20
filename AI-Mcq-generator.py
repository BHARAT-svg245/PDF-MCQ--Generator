
import os
import re
import streamlit as st
from io import BytesIO
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from pydantic import BaseModel, Field
from typing import List, Literal


# ---------------------------------------
# Page configuration
# ---------------------------------------

st.set_page_config(
    page_title="PDF MCQ Generator",
    page_icon="📚",
    layout="wide"
)

st.title("📚 PDF Based MCQ Generator")
st.write("Upload your study material and generate MCQs using Gemini LLM.")


# ---------------------------------------
# Pydantic output structure
# ---------------------------------------

class MCQ(BaseModel):

    question: str = Field(
        description="Multiple choice question based on PDF"
    )

    options: List[str] = Field(
        description="Four options labeled A., B., C., D. or E.",
        min_length=4,
        max_length=6
    )
    correct_answer: Literal["A", "B", "C", "D", "E", "F"]=Field(
        description="give the label of the right answer."
    )
    explanation: str= Field(
        description="give the brief explaination of the the answer of the question."
    )
    page_number: int | None = None

class MCQSet(BaseModel):
    questions: List[MCQ] = Field(
        description="Generated MCQ questions"
    )

# ---------------------------------------
# Text preprocessing
# ---------------------------------------

def text_preprocessing(text):
    # Remove unnecessary NPTEL headers
    text = re.sub(r"\bNPTEL\b","",text,flags=re.IGNORECASE)
    # Remove the digit
    text = re.sub(r"\d+","", text)
    return text.strip()

# ---------------------------------------
# PDF extraction
# ---------------------------------------
def extract_pdf_text(uploaded_files):
    all_text=[]                                   #it contains the elements in form of documents alongwith metadata as well as text of the topics.
    reader=PdfReader(uploaded_files)
    for page in reader.pages:
        text=page.extract_text()
        text=text_preprocessing(text)
        all_text.append(text)
    return all_text

# Prepare context
# ---------------------------------------

def prepare_context(all_text,start_page,end_page):
    context=""
    for i in range(start_page,end_page,1):
        context+=all_text[i]
    return context 

# ---------------------------------------
# Prompt
# ---------------------------------------
from prompts import mcq_prompt
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template(mcq_prompt)

# ---------------------------------------
# Gemini LLM
# ---------------------------------------

@st.cache_resource
def load_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        api_key="Place Your API key here"
    )
    return llm.with_structured_output(MCQSet)

# ---------------------------------------
# Streamlit sidebar
# ---------------------------------------

with st.sidebar:
    st.header("Generation Settings")
    num_questions = st.number_input(
        "Number of questions",
        min_value=1,
        max_value=100,
        value=30,
        step=5
    )

# ---------------------------------------
# PDF uploader
# ---------------------------------------

uploaded_files = st.file_uploader(
    "Upload your PDF files",
    type=["pdf"]
    #accept_multiple_files=True
)


# ---------------------------------------
# Generate MCQs
# ---------------------------------------

if st.button("Generate MCQs", type="primary"):
    if not uploaded_files:
        st.warning("Please upload at least one PDF.")
    else:
        try:
            with st.spinner("Extracting PDF content..."):
                all_pages = extract_pdf_text(uploaded_files)
            if not all_pages:
                st.error(
                    "No extractable text found. "
                    "The PDF may contain scanned images."
                )
                st.stop()
            with st.spinner("Preparing text chunks..."):
                context = prepare_context(all_pages,0,10)
            st.success(
                f"Extracted {len(all_pages)} pages ")            
            with st.spinner("Generating MCQs using Gemini..."):
                llm = load_llm()
                prompt = PromptTemplate.from_template(
                    mcq_prompt
                )
                chain = prompt | llm
                response = chain.invoke({
                    "context": context,
                    "Number of Questions": num_questions
                })
            questions = response.questions
            if len(questions) != num_questions:
                st.warning(
                    f"Requested {num_questions} questions, "
                    f"but Gemini generated {len(questions)}."
                )
            else:
                st.success(
                    f"Successfully generated {len(questions)} MCQs!"
                )
            # Store generated questions
            st.session_state["mcqs"] = questions
        except Exception as e:
            st.error(f"Error: {str(e)}")


# ---------------------------------------
# Display MCQs
# ---------------------------------------

if "mcqs" in st.session_state:
    questions = st.session_state["mcqs"]
    st.divider()
    st.header("Generated Questions")
    for index, mcq in enumerate(questions):
        with st.expander(f"Question {index + 1}: {mcq.question}",expanded=False):
            # st.write("**Question:**", mcq.question)
            for option in mcq.options:
                st.write(option)
    # ---------------------------------------
    # Download MCQs
    # ---------------------------------------

    output_text = ""
    for index, mcq in enumerate(questions):
        output_text += f"\nQ{index + 1}. {mcq.question}\n"
        for option in mcq.options:
            output_text += option + "\n"
        output_text += (
            f"\nCorrect Answer: {mcq.correct_answer}\n"
        )
        output_text += (
            f"Explanation: {mcq.explanation}\n"
        )

    st.download_button(
        label="Download MCQs as TXT",
        data=output_text,
        file_name="Generated_MCQs.txt",
        mime="text/plain"
    )
