import openai
import os

openai.api_key = os.getenv("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")

def generate_image(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    return response['data'][0]['url']
