"""

"""
import json


def attributes(obj):
    return list(sorted(filter(
        lambda k: not k.startswith('__'), obj.__dict__.keys()
    )))


def attributes_values(obj):
    return list(map(lambda a: (a, getattr(obj, a)), attributes(obj)))


class Confyg(object):

    __source__ = None
    __config_store__ = None

    @classmethod
    def load(cls):

        cls.__config_store__ = cls.load_store()

        for k, vk in attributes_values(cls):
            v = cls.get(vk)
            cls.set(k, v)

    @classmethod
    def load_store(cls):
        raise NotImplementedError('load_store needs to be implemented')

    @classmethod
    def get(cls, key):
        raise NotImplementedError('get needs to be implemented')

    @classmethod
    def set(cls, key, val):
        setattr(cls, key, val)


class JsonConfyg(Confyg):

    @classmethod
    def load_store(cls):
        with open(cls.__source__, 'r') as f:
            return json.load(f)

    @classmethod
    def get(cls, key):
        return cls.__config_store__[key]


