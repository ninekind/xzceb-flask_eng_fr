from translator import englishToFrench, frenchToEnglish
import unittest

import sys
import os
print(os.getcwd())
sys.path.append(os.getcwd())


class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertIsNotNone(englishToFrench(None))
        self.assertNotEqual(englishToFrench("Bonjour"), "Hello")


class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertIsNotNone(frenchToEnglish(None))
        self.assertNotEqual(frenchToEnglish("Hello"), "Bonjour")


unittest.main()
