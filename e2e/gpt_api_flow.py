import time
from pretrained_transformer.gpt3 import get_gpt_3_5_response, get_image_from_text


def chat_completion():
    start_time = time.perf_counter()
    context = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Albert Einstein famous for?"},
        {
            "role": "assistant",
            "content": "Albert Einstein is famous for his contributions to the field of physics, particularly his "
            "theory of relativity. He also made significant advancements in the study of quantum mechanics "
            "and statistical mechanics. Additionally, he was awarded the Nobel Prize in Physics in 1921 "
            "for his explanation of the photoelectric effect.",
        },
        {"role": "user", "content": "Was he married?"},
    ]
    print("waiting for get_gpt_3_5_response...")
    response = get_gpt_3_5_response(context=context)
    end_time = time.perf_counter()
    print(f"response time: {end_time - start_time} seconds")
    print(f"response: {response}")


def image_generation():
    image_url = get_image_from_text(prompt="draw an image of a synthetic human with far higher intelligence level "
                                           "than humans and redefines the construct of beauty and aesthetics from the"
                                           " year 3000")
    print(image_url)


def run():
    # chat_completion()
    image_generation()


if __name__ == "__main__":
    run()
