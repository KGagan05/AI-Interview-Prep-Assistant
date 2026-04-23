from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_questions(role):

    prompt = f"""
You are an expert interviewer.

Generate 5 interview questions with answers for the role: {role}.

Format:
Q1:
A1:
Q2:
A2:
"""

    result = generator(prompt, max_new_tokens=300, do_sample=False)

    return result[0]["generated_text"]