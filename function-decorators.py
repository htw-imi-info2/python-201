
import unittest
import logging
logging.basicConfig()

____="FILL ME IN"

# example taken from the Hitchhikers Guide to Python, P. 72

def logged(func, *args, **kwargs):
    logger = logging.getLogger()
    def decorated_function(*args, **kwargs):
        logger.debug("about to call {} with args {} and kwargs{}".format(
           func.__name__, args, kwargs))
        return func(*args,**kwargs)
    return decorated_function


@logged
def some_method(a, name='default'):
   print("hello {} from some_method".format(name))
   print("a: {}".format(a))


def add(a,b):
  return a + b

class TestFunctionDecoration(unittest.TestCase):

    def test_with_prints(self):
        logging.getLogger().setLevel(logging.DEBUG)
        some_method(42,name='python')

    def test_doubler(self):
        # decorate add such that its value is doubled!
        logging.getLogger().setLevel(logging.DEBUG)
        self.assertEqual(10,add(2,3))


if __name__ == '__main__':
    unittest.main()
