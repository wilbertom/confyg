
from unittest import TestCase
from confyg import OsConfyg
import os

os.environ['URL'] = 'localhost'
os.environ['DEBUG'] = 'True'


os.environ['url'] = 'localhost:5000'
os.environ['debug'] = 'False'


class TestOsConfyc(TestCase):

    class Config(OsConfyg):
        URL = 'url'
        DEBUG = 'debug'


    def test_url_and_debug(self):
        TestOsConfyc.Config.load()

        self.assertEquals(TestOsConfyc.Config.URL, 'localhost')
        self.assertEquals(TestOsConfyc.Config.DEBUG, 'True')


class TestOsConfygLower(TestCase):

    class Config(OsConfyg):
        upper_cased = False

        URL = 'url'
        DEBUG = 'debug'

    def test_url_and_debug(self):
        TestOsConfygLower.Config.load()

        self.assertEquals(TestOsConfygLower.Config.URL, 'localhost:5000')
        self.assertEquals(TestOsConfygLower.Config.DEBUG, 'False')


