from .translator import english_to_french, french_to_english
import unittest

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        # Test None returns empty string
        self.assertNotEqual(french_to_english("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(french_to_english(0), 0) 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 

unittest.main()