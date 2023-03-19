import os
import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_text(response):
    if "choices" in response and len(response["choices"]) > 0:
        if "text" in response["choices"][0]:
            return response["choices"][0]["text"]
        elif "message" in response["choices"][0]:
            return response["choices"][0]["message"]["content"]
    else:
        raise RuntimeError("Something Went Wrong")


@retry(wait=wait_random_exponential(multiplier=0.5, max=60), stop=stop_after_attempt(3))
def get_gpt_3_response(prompt) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return extract_text(response)


@retry(wait=wait_random_exponential(multiplier=0.5, max=60), stop=stop_after_attempt(3))
def get_gpt_3_5_response(context) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=context,
        temperature=0.3,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=1.0,
        presence_penalty=1.0,
    )
    return extract_text(response)
