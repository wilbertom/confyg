from unittest import TestCase
import confyg.transformations


class TestTransformations(TestCase):

    def test_upper_case(self):
        self.assertEquals(
            confyg.transformations.upper_case('hello'),
            'HELLO'
        )

    def test_hyphens_to_undersquare(self):
        self.assertEquals(
            confyg.transformations.hyphens_to_underscore('hello-world'),
            'hello_world'
        )
