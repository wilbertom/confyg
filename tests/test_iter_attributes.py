from unittest import TestCase
from confyg import attributes_values


class A(object):
    I = None
    J = None
    x = True

    def __init__(self):
        self.i = None
        self.j = None


class TestIterAttributes(TestCase):

    def test_attributes_values_instance(self):
        attrs = sorted(attributes_values(A()))

        self.assertEquals(
            attrs,
            [('i', None), ('j', None)]
        )

    def test_attributes_values_cls(self):
        attrs = sorted(attributes_values(A))

        self.assertEquals(
            attrs,
            [('I', None), ('J', None), ('x', True)]
        )
