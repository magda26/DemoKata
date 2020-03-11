from unittest import TestCase
from Calculator import Calculator

class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(""),0,"Empty string")

    def test_add_oneString(self):
        self.assertEqual(Calculator().add("1"),1,"A Number")

    def test_add_stringWithANumber(self):
        self.assertEqual(Calculator().add("1"),1,"A Number")
        self.assertEqual(Calculator().add("2"),2,"A Number")


