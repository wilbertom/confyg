
upper_case = lambda key: key.upper()

hyphens_to_underscore = lambda key: key.replace('-', '_')

transformation = staticmethod

composite = lambda f, g: lambda x: f(g(x))
