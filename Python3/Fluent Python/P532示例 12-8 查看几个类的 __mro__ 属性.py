print(bool.__mro__)
def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

print_mro(bool)
# >>> from frenchdeck2 import FrenchDeck2
# >>> print_mro(FrenchDeck2) ➌
# FrenchDeck2, MutableSequence, Sequence, Sized, Iterable, Container, object
import numbers
print_mro(numbers.Integral)
#Integral, Rational, Real, Complex, Number, object
import io
print_mro(io.BytesIO)
#BytesIO, _BufferedIOBase, _IOBase, object
print_mro(io.TextIOWrapper)
#TextIOWrapper, _TextIOBase, _IOBase, object