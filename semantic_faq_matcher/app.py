import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Semantic FAQ Matcher", page_icon="🤖", layout="centered")

@st.cache_resource
def load_model():
    # Downloads this small pretrained model the first time; cached afterwards.
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

@st.cache_data
def load_faq():
    data = pd.read_csv("faq.csv")
    data = data.dropna(subset=["question", "answer"])
    return data

st.title("🤖 Semantic FAQ Matcher")
st.write("Ask a question in your own words. The AI finds the FAQ with the closest meaning.")
st.caption("Project: PS 47 — Semantic FAQ Matcher (Generative AI Jury 2)")

try:
    faq = load_faq()
    model = load_model()
except Exception as exc:
    st.error("Could not load the FAQ file or AI model. Check the setup instructions and internet connection for the first model download.")
    st.exception(exc)
    st.stop()

question = st.text_input("Enter your question", placeholder="e.g. I cannot remember my login password")
threshold = st.slider("Minimum similarity required", min_value=0.10, max_value=0.90, value=0.35, step=0.05)

if st.button("Find Answer", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Understanding your question and searching the FAQ..."):
            question_vector = model.encode([question])
            faq_vectors = model.encode(faq["question"].astype(str).tolist())
            scores = cosine_similarity(question_vector, faq_vectors)[0]
            best_index = int(scores.argmax())
            best_score = float(scores[best_index])

        st.subheader("Result")
        if best_score >= threshold:
            st.success("Relevant FAQ found")
            st.markdown("**Matched FAQ:**")
            st.write(faq.iloc[best_index]["question"])
            st.markdown("**Answer:**")
            st.info(faq.iloc[best_index]["answer"])
            st.metric("Semantic similarity", f"{best_score:.1%}")
        else:
            st.warning("No sufficiently close FAQ was found. Please rephrase your question or contact support.")
            st.metric("Best similarity found", f"{best_score:.1%}")

        with st.expander("See the top 3 matches"):
            top_indices = scores.argsort()[::-1][:3]
            for rank, idx in enumerate(top_indices, start=1):
                st.write(f"**{rank}. {faq.iloc[idx]['question']}**")
                st.caption(f"Similarity: {scores[idx]:.1%}")
                st.write(faq.iloc[idx]["answer"])
                st.divider()

with st.expander("How does this model work?"):
    st.markdown("""
    1. The Sentence Transformer converts each FAQ question into a numerical vector called an **embedding**.
    2. The user's question is converted into an embedding using the same model.
    3. **Cosine similarity** compares the meaning represented by the vectors.
    4. The FAQ with the highest similarity is selected.
    5. A threshold prevents the app from returning an unrelated answer when no FAQ is close enough.
    """)

st.caption("Educational prototype. Similarity is a matching score, not a guarantee that an answer is correct.")
