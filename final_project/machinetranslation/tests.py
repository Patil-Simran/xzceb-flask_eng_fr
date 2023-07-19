import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        result1 = english_to_french("Hello")
        result2 = english_to_french("Goodbye")
        self.assertEqual(result1, "Bonjour")
        self.assertNotEqual(result2, "Bonjour")

    def test_french_to_english(self):
        result1 = french_to_english("Bonjour")
        result2 = french_to_english("Au revoir")
        self.assertEqual(result1, "Hello")
        self.assertNotEqual(result2, "Hello")

if __name__ == '__main__':
    unittest.main()
