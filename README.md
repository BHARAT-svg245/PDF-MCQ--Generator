# 📚 LLM-Based MCQ Generator from PDF

## 📌 Overview

Preparing for competitive and academic examinations often requires students to study and memorize large amounts of theoretical content from lengthy PDF documents. Revising these documents repeatedly can be time-consuming and challenging.

This project addresses this problem by leveraging **Large Language Models (LLMs)** to automatically convert theoretical content from PDF documents into Multiple Choice Questions (MCQs).

Users can upload a PDF containing theoretical study material, and the application extracts its text and generates multiple-choice questions along with four or more answer options, the correct answer, and a brief explanation.

This approach helps students actively revise and memorize important concepts through question-based learning rather than repeatedly reading lengthy theoretical documents.

## 🎯 Problem Statement

Students preparing for competitive examinations often struggle with:
- Memorizing lengthy theoretical concepts.
- Revising large PDF documents efficiently.
- Identifying important concepts and potential exam questions.
- Creating practice questions manually, which consumes considerable time.

- here, the question is visible on UI, which can be used to answer and then cross check with the solution in the downloaded solution pdf.
**Solution:** An AI-powered MCQ generation system that automatically transforms PDF study materials into interactive practice questions.

## ✨ Key Features

- **PDF Upload:** Upload theoretical study materials in PDF format.
- **Automatic Text Extraction:** Extract textual content from uploaded PDF documents.
- **LLM-Based MCQ Generation:** Generate context-relevant multiple-choice questions from extracted content.
- **Multiple Answer Options:** Each question contains multiple options with one correct answer.
- **Correct Answer Identification:** Clearly identify the correct answer for every question.
- **Brief Explanations:** Provide explanations to help users understand the concepts behind the answers.
- **Customizable Question Count:** Adjust the number of MCQs to generate using the Streamlit sidebar.
- **Interactive Streamlit UI:** View and practice generated questions through a simple user interface.
- **Downloadable Output:** Download the final generated MCQ document containing questions, options, correct answers, and explanations.

## ⚙️ Project Workflow

1. **PDF Upload:** The user uploads a PDF document through the Streamlit interface.
2. **Text Extraction:** The application extracts the textual content from the PDF.
3. **Content Processing:** The extracted text is processed and prepared for the LLM.
4. **MCQ Generation:** The LLM analyzes the content and generates MCQs based on the provided theoretical information.
5. **Structured Output:** Each generated question contains:
   - Question
   - Multiple answer options
   - Correct answer
   - Brief explanation
6. **Question Display:** Generated questions are displayed in the Streamlit application.
7. **Download Output:** Users can download the final MCQ file for offline practice and revision.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Large Language Models (LLMs)** – Intelligent question and answer generation.
- **Streamlit** – Interactive web application interface.
- **PyPDF2** – PDF text extraction.
- **Pydantic** – Structured output validation (if used in the implementation).

## 📂 Project Structure

```text
MCQ-Generator/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── Mcq_generator.ipyn    # shows the evolution of project
├── pdfs/                   # Sample pdf documents to test the app
│
└── output/                 # Generated MCQ files (optional)
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the Project Directory

```bash
cd MCQ-Generator
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Credentials

If your application uses an LLM API, configure the required API key using environment variables or Streamlit secrets.

Never upload API keys or other sensitive credentials to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 💡 How to Use

1. Launch the Streamlit application.
2. Upload your theoretical study material in PDF format.
3. Select the desired number of MCQs from the sidebar.
4. Generate questions using the application.
5. Review the questions, answer options, correct answers, and explanations.
6. Download the generated MCQ file.
7. Use the downloaded questions for examination preparation and revision.

## 🎓 Use Cases

- Competitive examination preparation.
- University and college examination preparation.
- Revision of lengthy theoretical subjects.
- Self-assessment and knowledge testing.
- Converting educational PDFs into practice material.
- Quick revision of academic notes and study materials.

## 🔮 Future Improvements

- Support for multiple PDF uploads.
- Difficulty-level selection (Easy, Medium, Hard).
- Topic-wise MCQ generation.
- Interactive quizzes with automatic score calculation.
- Support for scanned PDFs using OCR.
- Improved question diversity and duplicate detection.
- Export generated questions into PDF and DOCX formats.

## ⚠️ Limitations

- The quality of generated questions depends on the quality and clarity of the extracted PDF text.
- Complex tables, diagrams, and scanned documents may require additional processing.
- LLM-generated answers and explanations should be reviewed for accuracy before relying on them for examination preparation.

## 👨‍💻 Author

**Bharat Chauhan**
---

**Built for preparation of authors own software programm management exam preparation of nptel conducted by IIT Madras with Generative AI.**
