
import unittest

____="FILL ME IN"

# this methods simply return information about their parameters.

def func_positional(a, b):
    return a, b

def func_positional_multiple(*args):
    return type(args).__name__

def func_keywords(name="default", year = 2019):
    return name, year

def func_keywords_multiple(**kwargs):
    return type(kwargs).__name__, kwargs


class TestFunctionParameters(unittest.TestCase):

    def test_positional(self):
        c, d = func_positional(4, 6)
        self.assertEqual(c,4)
        self.assertEqual(d,6)

    def test_positional_multiple(self):
        type_name = func_positional_multiple(1,2,"hello")
        self.assertEqual('tuple',type_name)

    def test_keywords(self):
        name, year = func_keywords(name='python', year=2019)
        self.assertEqual(name,'python')
        self.assertEqual(year,2019)


    def test_keywords_defaults(self):
        name, year = func_keywords()
        self.assertEqual(name,'default')
        self.assertEqual(year,2019)

    def test_keywords_multiple(self):
        type_name, kwargs = func_keywords_multiple(name='python', year=2019)
        self.assertEqual('dict',type_name)
        self.assertEqual(kwargs['name'],'python')
        self.assertEqual(kwargs['year'],2019)


if __name__ == '__main__':
    unittest.main()
