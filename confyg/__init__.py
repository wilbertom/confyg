"""

Welcome to Confyg's documentation. Confyg is a class based
configuration module. By defining configuration classes, Confyg
will load the values from their sources.

A source can be anything like a file or environment variables.
The advantage to using Confyg is that you will have a unifying
syntax to load configurations, independent of the data source.

Tutorial
========

Here is a simple example that uses environment variables for a
web server.

`server_config.py`

.. code-block:: python

    from confyg import OsConfyg


    class Config(OsConfyg):
        SECRET_KEY = 'key'
        LOGGER_NAME = 'logger_name'
        DEBUG = 'debug'

    Config.load()
    assert Config.SECRET_KEY == '5b6ba13f79129a74a3e819b78e36b922'
    assert Config.LOGGER_NAME == 'web_server'
    assert Config.DEBUG == 'True'

.. code-block:: bash

    export SECRET_KEY='5b6ba13f79129a74a3e819b78e36b922'
    export LOGGER_NAME='web_server'
    export DEBUG='True'
    python server_config.py

We changed our mind and want to use a configuration file. The
file needs to be in some format. For simplicity we choose JSON.
The code doesn't change much:

.. code-block:: python

    from confyg import JsonConfyg


    class Config(JsonConfyg):

        __source__ = 'config.json'

        SECRET_KEY = 'key'
        LOGGER_NAME = 'logger_name'
        DEBUG = 'debug'

    Config.load()
    assert Config.SECRET_KEY == '5b6ba13f79129a74a3e819b78e36b922'
    assert Config.LOGGER_NAME == 'web_server'
    assert Config.DEBUG == True

`config.json`

.. code-block:: javascript

    {
        "key": "5b6ba13f79129a74a3e819b78e36b922",
        "logger_name": "web_server",
        "debug": true
    }

There is one thing to notice here. With JSON, `DEBUG`
has a different type. This is because the operating system
environment only supports strings. Different sources support
different types. We think this can lead to bugs, and hope
to fix it.

Interface
=========

Every Confyg has a `__source__`. The source is used
to find the configuration values.

The `__config_store__` holds the serialized key values
after being loaded from the `__source__`.

New Confyg subclasses should only have to override the `load_store` method.
This method should return a dictionary like object. If so
the default `get` and `set` methods should work fine.

We encourage you to read the source code for the project. It is
tested, small, simple and documented.

"""
import json
import os

VERSION = '0.1.0'


def attributes_values(obj):
    """
    Returns a list of (attribute, value) tuples for obj.

    """
    return list(filter(
        lambda kv: not kv[0].startswith('_'), obj.__dict__.items()
    ))


def confyg_attributes_values(obj):
    """
    Returns a list of (attribute, value) tuples that we
    consider to be keys for a Confyg class. For now
    these are the ones that upper cased.

    """
    return list(filter(lambda av: av[0].isupper(), attributes_values(obj)))


class Confyg(object):
    """
    The base configuration class implementing the common
    functionality. Subclassing this class should make
    it easy to add new configuration sources.

    """
    __source__ = None
    __config_store__ = None

    @classmethod
    def load(cls):

        cls.__config_store__ = cls.load_store()

        for k, vk in confyg_attributes_values(cls):
            v = cls.get(vk)
            cls.set(k, v)

    @classmethod
    def load_store(cls):
        return {}

    @classmethod
    def get(cls, key):
        return cls.__config_store__[key]

    @classmethod
    def set(cls, key, val):
        setattr(cls, key, val)


class JsonConfyg(Confyg):
    """
    JsonConfyg let's you load configuration from a JSON
    file. The path to the file should be specified in
    `__source__`.

    """

    @classmethod
    def load_store(cls):
        with open(cls.__source__, 'r') as f:
            return json.load(f)


class DictConfyg(Confyg):
    """
    The DictConfyg loads configuration from the dictionary
    set in `__source__`.

    """

    @classmethod
    def load_store(cls):
        return cls.__source__


class OsConfyg(DictConfyg):
    """
    The OSConfyg class loads configuration from environment
    variables.

    By default OSConfyg transforms the configuration keys to
    uppercase. To prevent this behavior set `upper_cased` to
    False.

    """
    upper_cased = True

    __source__ = os.environ

    @classmethod
    def get(cls, key):
        return cls.__config_store__[key.upper() if cls.upper_cased else key]
