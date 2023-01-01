import unittest

from pretrained_transformers.gpt3 import Gpt3


class GPT3Test(unittest.TestCase):

    def test_generate_essay(self):
        gpt3 = Gpt3()
        response = gpt3.generate_essay('hello')
        print(response)
        assert len(response) > 0
