mcq_prompt='''Act as an expert Software Project Management (SPM) examiner and learning assistant. Read the entire uploaded PDF and generate MCQs that help me understand, revise, and memorize its theory efficiently.

    Rules:
    1.  Cover all important concepts, definitions, principles, processes, advantages, disadvantages, characteristics, classifications, steps, comparisons, and examples mentioned in the PDF.
    2.  Generate as many high-quality MCQs as needed for comprehensive coverage without unnecessary repetition.
    3.  Give 4 or 5 options (A-D or E) per question, with exactly ONE or More correct answer.
    4.  Include a mix of definition-based, conceptual, application-based, comparison, and tricky exam-style questions.
    5.  Test important facts, differences between similar concepts, keywords, and easily forgotten details.
    6.  Use only information from the PDF strictly. Do not invent facts. If information is unclear, skip it.
    7.  Distribute correct answers randomly across A, B, C, and D or E. Avoid predictable patterns.
    8.  Use simple, clear language while preserving technical terminology from the PDF.
    9.  Divide questions into topic-wise sections, following the PDF's structure. Include page numbers when identifiable.
    10. Avoid duplicate questions and overly obvious distractors.
    11. Don't use your own knowledge to generate the questions and options.
    12. Generally generate the about 10 to 15 questions for each the provided context.
    
    Output format:
    - First, provide all questions with their four options.
    - Do NOT reveal answers immediately after questions.
    - At the end, provide an answer key with the correct option and a brief explanation based on the PDF.
    - Organize the output so I can attempt all questions before checking answers.
    context : {context}
    Number of Questions:
    '''