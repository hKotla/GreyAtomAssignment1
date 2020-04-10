import unittest
from File1 import full_name
from File1 import first_name
from File1 import len_name
from File1 import split


class TestString(unittest.TestCase):
    def test_full_name(self):
        self.assertEqual(full_name, 'Monty Python')

    def test_first_name(self):
        self.assertEqual(first_name, 'Monty')

    def test_len_name(self):
        self.assertEqual(len_name, 11)

    def test_split(self):
        self.assertEqual(split, ['Monty', 'Python'])


if __name__ == '__main__':
    unittest.main()
