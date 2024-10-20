#Example 1-1. A deck as a sequence of playing cards
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    
    
beer_card = Card('7', 'diamonds')
beer_card
Card(rank='7', suit='diamonds')


deck = FrenchDeck()
len(deck)
52

deck[0]
Card(rank='2', suit='spades')
deck[-1]
Card(rank='A', suit='hearts')


from random import choice
choice(deck)
Card(rank='3', suit='hearts')
choice(deck)
Card(rank='K', suit='spades')
choice(deck)
Card(rank='2', suit='clubs')


deck[:3]
for card in deck: # doctest: +ELLIPSIS
    print(card)
    Card(rank='2', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='spades')
    ...

for card in reversed(deck): # doctest: +ELLIPSIS
    print(card)
    Card(rank='A', suit='hearts')
    Card(rank='K', suit='hearts')
    Card(rank='Q', suit='hearts')
    ...

Card('Q', 'hearts') in deck
True
Card('7', 'beasts') in deck
False

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
 rank_value = FrenchDeck.ranks.index(card.rank)
 return rank_value * len(suit_values) + suit_values[card.suit]

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)


v1 = vector(2, 4)
v2 = vector(2, 1)
v1 + v2
vector(4, 5)

v = vector(3, 4)
abs(v)
5.0

v * 3
vector(9, 12)
abs(v * 3)
15.0

"""
vector2d.py: a simplistic class demonstrating some special methods
It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.
This example is greatly expanded later in the book.
Addition::
 v1 = Vector(2, 4)
 v2 = Vector(2, 1)
 v1 + v2
 Vector(4, 5)
Absolute value::
 v = Vector(3, 4)
 abs(v)
 5.0
Scalar multiplication::
 v * 3
 Vector(9, 12)
 abs(v * 3)
 15.0
"""
import math
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)
    
def __mul__(self, scalar):
    return Vector(self.x * scalar, self.y * scalar)

Table 1-1. Special method names (operators excluded)
Category                            Method names
String/bytes representation         __repr__ __str__ __format__ __bytes__ __fspath__
Conversion to number                __bool__ __complex__ __int__ __float__ __hash__ __index__
Emulating collections               __len__ __getitem__ __setitem__ __delitem__ __contains__
Iteration                           __iter__ __aiter__ __next__ __anext__ __reversed__
Callable or coroutine execution     __call__ __await__
Context management                  __enter__ __exit__ __aexit__ __aenter__
Instance creation and destruction   __new__ __init__ __del__
Attribute management                __getattr__ __getattribute__ __setattr__ __delattr__ __dir__
Attribute descriptors               __get__ __set__ __delete__ __set_name__
Abstract base classes               __instancecheck__ __subclasscheck__
Class metaprogramming               __prepare__ __init_subclass__ __class_getitem__ __mro_entries__


Table 1-2. Special method names and symbols for operators
Operator category               Symbols                 Method names
Unary numeric                   - + abs()               __neg__ __pos__ __abs__
Rich comparison                 < <= == != > >=         __lt__ __le__ __eq__ __ne__ __gt__ __ge__
Arithmetic                      + - * / // % @          __add__ __sub__ __mul__ __truediv__ 
                                divmod() round() **     __floordiv__ __mod__ __matmul__ __div
                                pow()                   mod__ __round__ __pow__
Reversed arithmetic             (arithmetic operators   __radd__ __rsub__ __rmul__ __rtrue
                                with swapped operands)  div__ __rfloordiv__ __rmod__ __rmat
                                                        mul__ __rdivmod__ __rpow__
Augmented assignment arithmetic += -= *= /= //= %=      __iadd__ __isub__ __imul__ __itrue
                                @= **=                  div__ __ifloordiv__ __imod__ __imat
                                                        mul__ __ipow__
Bitwise                         & | ^ << >> ~           __and__ __or__ __xor__ __lshift__ 
                                                        __rshift__ __invert__
Reversed bitwise                (bitwise operators      __rand__ __ror__ __rxor__ 
                                with swapped operands)  __rlshift__ __rrshift__
Augmented assignment bitwise    &= |= ^= <<= >>=        __iand__ __ior__ __ixor__ 
                                                        __ilshift__ __irshift__