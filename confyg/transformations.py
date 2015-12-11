
upper_case = lambda key: key.upper()
transformation = staticmethod
composite = lambda f, g: lambda x: f(g(x))
