from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]#Is it OK without -1
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)

        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))
        
    shortcut_names = 'xyzt'

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name = cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

        def __eq__(self, other):
            return tuple(self) == tuple(other)

        def __hash__(self):
            hashes = (hash(x) for x in self._components)
            return functools.reduce(operator.xor, hashes, 0)

        def __hash__(self):
            hashes = map(hash, self._components)
            return functools.reduce(operator.xor, hashes)
            
##########################these were added as new elements
        def __abs__(self):
            return math.sqrt(sum(x * x for x in self))

        def __neg__(self):
            return Vector(-x for x in self);

        def __pos__(self):
            return Vector(self)

#P558
        def __add__(self, other):
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)

#P561
        def __radd__(self, other):
            return self + other

print(v1 + 1)#?