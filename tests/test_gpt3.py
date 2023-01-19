from pretrained_transformer.gpt3 import generate_essay


def mock_response():
    return {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "logprobs": None,
                "text": "\n\nHi there! How can I help you?",
            }
        ],
        "created": 1672682397,
        "id": "cmpl-6UJOHaJWAuYx5Pbg8kfFjkRJodi4p",
        "model": "text-davinci-003",
        "object": "text_completion",
        "usage": {
            "completion_tokens": 11,
            "prompt_tokens": 1,
            "total_tokens": 12,
        },
    }


def test_generate_essay(mocker):
    mocker.patch(
        "pretrained_transformer.gpt3.send_request", return_value=mock_response()
    )
    response = generate_essay("hello")
    print(response)
    assert response == "\n\nHi there! How can I help you?"
