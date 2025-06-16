
import pandas as pd
import streamlit as st
import json

def export_flashcards(flashcards, format_type):
    if format_type == "CSV":
        df = pd.DataFrame(flashcards)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, "flashcards.csv", "text/csv")
    elif format_type == "JSON":
        json_data = json.dumps(flashcards, indent=2)
        st.download_button("Download JSON", json_data, "flashcards.json", "application/json")
