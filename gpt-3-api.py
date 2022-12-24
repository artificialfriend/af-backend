import openai

def t
openai.api_key = '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'

response = openai.Completion.create(
  model='text-davinci-003',
  prompt='Create an outline for an essay about Nikola Tesla and his contributions to technology:',
  temperature=0.3,
  max_tokens=500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)
