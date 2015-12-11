
from unittest import TestCase
import os
from confyg import OsConfyg
from confyg.transformations import upper_case, composite, transformation, \
    hyphens_to_underscore


os.environ['URL'] = 'localhost'
os.environ['DEBUG'] = 'True'
os.environ['APP_HOST'] = 'localhost'

os.environ['url'] = 'localhost:5000'
os.environ['debug'] = 'False'



class TestOsConfyg(TestCase):

    class Config(OsConfyg):
        __transformation__ = transformation(
            upper_case
        )

        URL = 'url'
        DEBUG = 'debug'

    def test_url_and_debug(self):
        TestOsConfyg.Config.load()

        self.assertEquals(TestOsConfyg.Config.URL, 'localhost')
        self.assertEquals(TestOsConfyg.Config.DEBUG, 'True')


class TestOsConfygLower(TestCase):

    class Config(OsConfyg):
        URL = 'url'
        DEBUG = 'debug'

    def test_url_and_debug(self):
        TestOsConfygLower.Config.load()

        self.assertEquals(TestOsConfygLower.Config.URL, 'localhost:5000')
        self.assertEquals(TestOsConfygLower.Config.DEBUG, 'False')


class TestOsConfygFancy(TestCase):

    class Config(OsConfyg):

        __transformation__ = transformation(
            composite(
                upper_case,
                hyphens_to_underscore
            )
        )

        APP_HOST = 'app-host'

    def test_app_host(self):
        TestOsConfygFancy.Config.load()

        self.assertEquals(TestOsConfygFancy.Config.APP_HOST, 'localhost')

