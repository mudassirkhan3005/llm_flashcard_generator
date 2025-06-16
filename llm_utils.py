from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)

def generate_flashcards(text, subject="General"):
    prompt = f"""
    Generate 10 question-answer flashcards from the following content.
    Format:
    Q: ...
    A: ...
    Content:
    {text}
    """
    try:
        output = generator(prompt)[0]['generated_text']
    except Exception as e:
        return [{"question": "Error", "answer": str(e)}]

    flashcards = []
    parts = output.split("Q:")
    for part in parts[1:]:
        if "A:" in part:
            q, a = part.split("A:", 1)
            flashcards.append({"question": q.strip(), "answer": a.strip()})

    return flashcards[:15]
