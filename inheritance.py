
import unittest

____="FILL ME IN"

class A:
    def quack(self):
        return 'quaaack'

class B(A):
    def wuff(self):
        return 'wuff B'
    def miau(self):
        return 'miau B ' + super().miau()

class C(A):
    def wuff(self):
        return 'wuff C'
    def miau(self):
        return 'miau C'

class D(B, C):
    def quack(self):
        return 'D called ' + super().quack()


class TestInheritance(unittest.TestCase):

    def test_direct(self):
        b = B()
        self.assertEqual(b.wuff(),____)

    def test_inheritance(self):
        b = B()
        self.assertEqual(b.quack(),____)

    def test_multiple_inheritance(self):
        d = D()
        self.assertEqual(d.wuff(),____)

    def test_super_goes_all_the_way_up(self):
        d = D()
        self.assertEqual(d.quack(),____)

    def test_message_resolution_order_with_multiple_inheritance(self):
        d = D()
        self.assertEqual(d.miau(),____)

    def test_mro(self):
        d = D()
        mro = D.mro()
        mro_names = [c.__name__ for c in D.mro()]
        self.assertEqual(mro_names,____)



if __name__ == '__main__':
    unittest.main()
