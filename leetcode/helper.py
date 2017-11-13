class MethodProxy(object):
    def __init__(self, obj, method_name):
        self.obj = obj
        self.method_name = method_name

    def __call__(self, *args, **kwargs):
        result = getattr(self.obj, self.method_name)(*args, **kwargs)
        print(self.method_name, args, kwargs, "->", result)
        return result


class ObjectProxy(object):
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, name):
        return MethodProxy(self.obj, name)


