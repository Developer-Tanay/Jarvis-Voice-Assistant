import ollama

def query_llm(prompt):
    response = ollama.chat(model='deepseek-r1', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']
