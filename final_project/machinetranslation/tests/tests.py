import json
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

 def test_englishToFrenchTable(self):
        self.assertEqual(english_to_french('table')['translations'][0]['translation'], 'Table')

 def test_englishToFrenchChair(self):
        self.assertEqual(english_to_french('chair')['translations'][0]['translation'], 'Chaise')

 def test_englishToFrenchHello(self):
        self.assertEqual(english_to_french('Hello')['translations'][0]['translation'], 'Bonjour')

 def test_frenchToEnglishHello(self):
        self.assertEqual( french_to_english('Bonjour')['translations'][0]['translation'], 'Hello')

 def test_englishToFrenchNull(self):
        self.assertEqual( french_to_english('Bonjour')['translations'][0]['translation'], 'Hello')


 def test_frenchToEnglishNull(self):
        self.assertEqual( french_to_english('Bonjour')['translations'][0]['translation'], 'Hello')



if __name__ == '__main__':
    unittest.main()