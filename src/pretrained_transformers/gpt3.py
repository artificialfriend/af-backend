import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_text(response):
    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text']
    else:
        raise RuntimeError('Something Went Wrong')


def send_request(prompt, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    return response


def generate_essay(prompt):
    """
        Example Prompt: "Create an outline for an essay about Nikola Tesla and his contributions to technology:"
    """
    model_parameters = {
        'model': 'text-davinci-003',
        'temperature': 0.3,
        'max_tokens': 150,
        'top_p': 1.0,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0
    }
    response = send_request(prompt, **model_parameters)
    print(response)
    return extract_text(response)