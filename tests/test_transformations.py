from unittest import TestCase
import confyg.transformations


class TestTransformations(TestCase):

    def test_upper_case(self):
        self.assertEquals(
            confyg.transformations.upper_case('hello'),
            'HELLO'
        )
