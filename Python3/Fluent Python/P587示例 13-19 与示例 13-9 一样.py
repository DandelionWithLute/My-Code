>>> v1 + 'ABC'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "vector_v6.py", line 329, in __add__
return Vector(a + b for a, b in pairs) # ➊
File "vector_v6.py", line 243, in __init__
self._components = array(self.typecode, components) # ➋
File "vector_v6.py", line 329, in <genexpr>
return Vector(a + b for a, b in pairs) # ➌
TypeError: unsupported operand type(s) for +: 'float' and 'str