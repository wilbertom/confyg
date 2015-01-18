"""

"""
import json
import os


def attributes(obj):
    return list(sorted(filter(
        lambda k: not k.startswith('__'), obj.__dict__.keys()
    )))


def attributes_values(obj):
    return list(map(lambda a: (a, getattr(obj, a)), attributes(obj)))


def config_attributes_values(obj):
    return list(filter(lambda av: av[0].isupper(), attributes_values(obj)))


class Confyg(object):

    __source__ = None
    __config_store__ = None

    @classmethod
    def load(cls):

        cls.__config_store__ = cls.load_store()

        for k, vk in config_attributes_values(cls):
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

    @classmethod
    def load_store(cls):
        with open(cls.__source__, 'r') as f:
            return json.load(f)


class OsConfyg(Confyg):

    upper_cased = True

    @classmethod
    def load_store(cls):
        return os.environ

    @classmethod
    def get(cls, key):
        return cls.__config_store__[key.upper() if cls.upper_cased else key]
