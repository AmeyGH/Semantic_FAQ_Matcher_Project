# Semantic FAQ Matcher — PS 47

A small semantic question-matching application for the Generative AI Jury 2 practical.

## What it does
- Accepts a question written in natural language.
- Converts the question and FAQ questions into sentence embeddings using `all-MiniLM-L6-v2`.
- Uses cosine similarity to find the closest FAQ.
- Shows the corresponding answer and similarity score.
- Uses a minimum-score threshold to avoid returning a weak match.

## Files
- `app.py` — Streamlit application and matching logic.
- `faq.csv` — editable FAQ question-and-answer dataset.
- `requirements.txt` — Python packages required.
- `test_questions.txt` — suggested demo questions.

## Requirements
- Python 3.10 or 3.11 recommended.
- Internet connection for the first download of the pretrained Sentence Transformer model.
- After the model is downloaded and cached, it can usually be loaded from the local cache.

## Setup on Windows
1. Extract the ZIP file.
2. Install Python 3.10 or 3.11 from https://www.python.org/downloads/ . During installation, tick **Add Python to PATH**.
3. Open the extracted `semantic_faq_matcher` folder.
4. Click the folder address bar, type `cmd`, and press Enter.
5. Create a virtual environment:

   `python -m venv venv`

6. Activate it:

   `venv\Scripts\activate`

7. Install packages:

   `python -m pip install --upgrade pip`

   `pip install -r requirements.txt`

8. Start the app:

   `streamlit run app.py`

9. A browser tab should open. If it does not, copy the Local URL shown in the terminal (usually `http://localhost:8501`) into your browser.

## How to demonstrate in the practical
1. Ask: `I cannot remember my login password`.
2. Show that it matches `How do I reset my password?`.
3. Ask: `Where can I find my enrolled classes?`.
4. Show the matched FAQ and similarity score.
5. Ask an unrelated question such as `What is the capital of Japan?`.
6. Explain that the threshold can prevent an unrelated FAQ from being returned.
7. Open the “How does this model work?” section and explain embeddings and cosine similarity.

## Customise the FAQ dataset
Open `faq.csv` in Excel or a text editor. Add rows with two columns:
- `question`
- `answer`

Keep the column names unchanged. Save the file and restart or refresh the app.

## Important explanation for viva
- **Embedding:** a numerical vector representing the meaning of a sentence.
- **Sentence Transformer:** a pretrained model that creates sentence embeddings.
- **Cosine similarity:** measures how close two vectors point in the same direction; higher scores indicate more similar embeddings.
- **Threshold:** minimum similarity score required before showing an answer.
- **Limitation:** the app retrieves an existing FAQ answer; it does not generate a new answer. It can fail when the FAQ database does not cover the user's question or when two questions are semantically ambiguous.

This is an educational prototype, not a production customer-support system.
