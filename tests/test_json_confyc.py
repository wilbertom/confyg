
from confyg import JsonConfyg
from unittest import TestCase


class Config(JsonConfyg):

    __source__ = 'tests/config.json'

    URL = 'url'
    DEBUG = 'debug'


class TestConfyg(TestCase):

    def test_url(self):
        Config.load()
        self.assertEquals(Config.URL, 'localhost')
