import os
import openai

openai.api_key = "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"


def send_query(message):
    return openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = [
            {"role" : "user", "content" : message}
        ]
    )

def get_reply(response):
    return response['choices'][0]['message']['content'] 
     

