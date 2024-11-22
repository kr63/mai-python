class CustomMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        attrs = {f'custom_{key}' if not key.startswith('__') else key: value for key, value in attrs.items()}

        def __setattr__(self, name, value):
            object.__setattr__(self, name if name.startswith('__') else f'custom_{name}', value)

        attrs['__setattr__'] = __setattr__

        return super().__new__(cls, name, bases, attrs, **kwargs)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
