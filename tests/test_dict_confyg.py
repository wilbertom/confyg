
from unittest import TestCase
from confyg import DictConfyg


class Config(DictConfyg):
    __source__ = {
        'url': 'localhost:5000',
        'debug': True
    }

    URL = 'url'
    DEBUG = 'debug'


class TestDictConfyg(TestCase):

    def test_url_and_debug(self):
        Config.load()

        self.assertEquals(Config.URL, 'localhost:5000')
        self.assertEquals(Config.DEBUG, True)
