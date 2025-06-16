import streamlit as st
from llm_utils import generate_flashcards
from preprocessing import extract_text_from_file
from export_utils import export_flashcards

st.set_page_config(page_title="LLM Flashcard Generator", layout="centered")
st.title("📚 LLM-Powered Flashcard Generator")

uploaded_file = st.file_uploader("Upload Educational Content (.txt or .pdf)", type=["txt", "pdf"])
subject = st.selectbox("Select Subject (Optional)", ["General", "Biology", "History", "Computer Science", "Math"])
input_text = st.text_area("Or paste your educational content here:", height=200)

if st.button("Generate Flashcards"):
    if uploaded_file:
        raw_text = extract_text_from_file(uploaded_file)
    elif input_text:
        raw_text = input_text
    else:
        st.warning("Please upload a file or paste some content.")
        st.stop()

    with st.spinner("Generating flashcards using LLM..."):
        flashcards = generate_flashcards(raw_text, subject)

    st.success("Flashcards generated successfully!")
    for i, card in enumerate(flashcards, 1):
        st.markdown(f"**{i}. Q:** {card['question']}")
        st.markdown(f"**A:** {card['answer']}")
        st.divider()

    export_format = st.selectbox("Export format", ["None", "CSV", "JSON"])
    if export_format != "None":
        export_flashcards(flashcards, export_format)
