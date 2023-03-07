import time
from pretrained_transformer.gpt3 import get_gpt_3_5_response, get_gpt_3_response


def run():
    start_time = time.perf_counter()
    context = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain second law of thermodynamics?"},
        {
            "role": "assistant",
            "content": "The second law of thermodynamics is a rule that says things in our world "
            "tend to get more messy over time. This means that when we use energy, "
            "like when we play with toys or run around outside, some of the energy turns "
            "into heat and gets lost. We can't get it back! It's like trying to put "
            "toothpaste back into the tube once you've squeezed it out - you just can't "
            "do it! So, this law tells us that everything tends to become less organized "
            "and more random as time goes on.",
        },
        {"role": "user", "content": "Now explain the third law."},
    ]
    print("waiting for get_gpt_3_5_response...")
    response = get_gpt_3_5_response(context=context)
    end_time = time.perf_counter()
    print(f"response time: {end_time - start_time} seconds")
    print(f"response: {response}")


if __name__ == "__main__":
    run()
