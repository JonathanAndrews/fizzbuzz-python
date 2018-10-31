import unittest

from fizzbuzz_python import *

class FizzBuzz(unittest.TestCase):

    def test_fizzer_return_Fizz(fizzbuzz):
        fizzbuzz.assertEqual(fizzer(3), "Fizz")

    def test_fizzer_return_number(self):
        self.assertEqual(fizzer(4), 4)

    def test_buzzer_return_Buzz(self):
        self.assertEqual(buzzer(5), "Buzz")

    def test_buzzer_return_number(self):
        self.assertEqual(buzzer(4), 4)

    def test_fizzbuzzer_return_Fizzbuzz(self):
        self.assertEqual(fizzbuzzer(15), "Fizzbuzz")

    def test_fizzbuzzer_return_number(self):
        self.assertEqual(fizzbuzzer(16), 16)


if __name__ == "__main__":
 unittest.main()
