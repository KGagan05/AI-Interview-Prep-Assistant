from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def generate_questions(role):
    prompt = f"""
You are an expert interviewer.

Generate 5 interview questions for a {role}.

Questions:
1.
"""

    result = generator(
        prompt,
        max_length=120,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )

    output = result[0]["generated_text"]

    return output