from collections import abc
issubclass(tuple, abc.Sequence)
True
issubclass(list, abc.MutableSequence)
True

#Example 2-1. Build a list of Unicode code points from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
... codes.append(ord(symbol))
...
codes
[36, 162, 163, 165, 8364, 164]

#Example 2-2. Build a list of Unicode code points from a string, using a listcomp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes
[36, 162, 163, 165, 8364, 164]




x = 'ABC'
codes = [ord(x) for x in x]
x 
'ABC'
codes
[65, 66, 67]
codes = [last := ord(c) for c in x]
last 
67
c 
    File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined


#Example 2-3. The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii
[162, 163, 165, 8364, 164]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii
[162, 163, 165, 8364, 164]


#Example 2-4. Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes] 
tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
 ('white', 'M'), ('white', 'L')]
for color in colors: 
... for size in sizes:
... print((color, size))
...
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')
tshirts = [(color, size) for size in sizes 
... for color in colors]
tshirts
[('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'),
 ('black', 'L'), ('white', 'L')]


#Example 2-5 shows basic usage of genexps to build a tuple and an array. Initializing a tuple and an array from a generator expression
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols) 
(36, 162, 163, 165, 8364, 164)
import array
array.array('I', (ord(symbol) for symbol in symbols)) 
array('I', [36, 162, 163, 165, 8364, 164])


#Example 2-6. Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes): 
... print(tshirt)
...
black S
black M
black L
white S
white M
white L


#Example 2-7. Tuples used as records
lax_coordinates = (33.9425, -118.408056) 
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014) 
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), 
... ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids): 
... print('%s/%s' % passport) 
...
BRA/CE342567
ESP/XDA205856
USA/31195855
for country, _ in traveler_ids: 
... print(country)
...
USA
BRA
ESP



a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
a == b
True
b[-1].append(99)
a == b
False
b
(10, 'alpha', [1, 2, 99])



def fixed(o):
... try:
... hash(o)
... except TypeError:
... return False
... return True
...
tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
fixed(tf)
True
Tuples Are Not Just Immutable Lists | 33
fixed(tm)
False


Table 2-1. Methods and attributes found in list or tuple (methods implemented by object
are omitted for brevity)
                            list        tuple
s.__add__(s2)               ●           ●       s + s2—concatenation
s.__iadd__(s2)              ●                   s += s2—in-place concatenation
s.append(e)                 ●                   Append one element after last
s.clear()                   ●                   Delete all items
s.__contains__(e)           ●           ●       e in s
s.copy()                    ●                   Shallow copy of the list
s.count(e)                  ●           ●       Count occurrences of an element
s.__delitem__(p)            ●                   Remove item at position p
s.extend(it)                ●                   Append items from iterable it
s.__getitem__(p)            ●           ●       s[p]—get item at position
s.__getnewargs__()                      ●       Support for optimized serialization with pickle
s.index(e)                  ●           ●       Find position of first occurrence of e
s.insert(p, e)              ●                   Insert element e before the item at position p
s.__iter__()                ●           ●       Get iterator
s.__len__()                 ●           ●       len(s)—number of items
s.__mul__(n)                ●           ●       s * n—repeated concatenation
s.__imul__(n)               ●                   s *= n—in-place repeated concatenation
s.__rmul__(n)               ●           ●       n * s—reversed repeated concatenationa
s.pop([p])                  ●                   Remove and return last item or item at optional position p
s.remove(e)                 ●                   Remove first occurrence of element e by value
s.reverse()                 ●                   Reverse the order of the items in place
s.__reversed__()            ●                   Get iterator to scan items from last to first
s.__setitem__(p, e)         ●                   s[p] = e—put e in position p, overwriting existing itemb
s.sort([key], [reverse])    ●                   Sort items in place with optional keyword arguments key and reverse
a
 Reversed operators are explained in Chapter 16.
 Also used to overwrite a subsequence. See “Assigning to Slices” on page 50
 
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # unpacking
latitude
33.9425
longitude
-118.408056

b, a = a, b

divmod(20, 8)
(2, 4)
t = (20, 8)
divmod(*t)
(2, 4)
quotient, remainder = divmod(*t)
quotient, remainder
(2, 4)

import os
_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
filename
'id_rsa.pub'

a, b, *rest = range(5)
a, b, rest
(0, 1, [2, 3, 4])
a, b, *rest = range(3)
a, b, rest
(0, 1, [2])
a, b, *rest = range(2)
a, b, rest
(0, 1, [])

a, *body, c, d = range(5)
a, body, c, d
(0, [1, 2], 3, 4)
*head, b, c, d = range(5)
head, b, c, d
([0, 1], 2, 3, 4)


def fun(a, b, c, d, *rest):
... return a, b, c, d, rest
...
fun(*[1, 2], 3, *range(4, 7))
(1, 2, 3, 4, (5, 6))


*range(4), 4
(0, 1, 2, 3, 4)
[*range(4), 4]
[0, 1, 2, 3, 4]
{*range(4), 4, *(5, 6, 7)}
{0, 1, 2, 3, 4, 5, 6, 7}

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas: 
        if lon <= 0: 
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
if __name__ == '__main__':
    main()

The output of Example 2-8 is:
                | latitude  | longitude
Mexico City     | 19.4333   | -99.1333
New York-Newark | 40.8086   | -74.0204
São Paulo       | -23.5478  | -46.6358

#Example 2-9. Method from an imaginary Robot class
def handle_command(self, message):
    match message: 
        case ['BEEPER', frequency, times]: 
            self.beep(times, frequency)
        case ['NECK', angle]: 
            self.rotate_neck(angle)
        case ['LED', ident, intensity]: 
            self.leds[ident].set_brightness(ident, intensity)
        case ['LED', ident, red, green, blue]: 
            self.leds[ident].set_color(ident, red, green, blue)
        case _: 
            raise InvalidCommand(message)

#Example 2-10. Destructuring nested tuples—requires Python ≥ 3.10
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),    
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record: 
            case [name, _, _, (lat, lon)] if lon <= 0: 
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


match tuple(phone):
 case ['1', *rest]: # North America and Caribbean
    ...
 case ['2', *rest]: # Africa and some territories
    ...
 case ['3' | '4', *rest]: # Europe
    ...

list    memoryview  array.array
tuple   range       collections.deque

Variable    Set Value
name        'Shanghai'
lat         31.1
lon         121.3
coord       (31.1, 121.3)

match record:
    case [name, _, _, (lat, lon)] if lon <= 0:
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

parse('(gcd 18 45)')
['gcd', 18, 45]
parse('''
... (define double
... (lambda (n)
... (* n 2)))
... ''')
['define', 'double', ['lambda', ['n'], ['*', 'n', 2]]

#Example 2-11. Matching patterns without match/case
def evaluate(exp: Expression, env: Environment) -> Any:
    "Evaluate an expression in an environment."
    if isinstance(exp, Symbol): # variable reference
        return env[exp]
    # ... lines omitted
    elif exp[0] == 'quote': # (quote exp)
        (_, x) = exp
        return x
    elif exp[0] == 'if': # (if test conseq alt)
        (_, test, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif exp[0] == 'lambda': # (lambda (parm…) body…)
        (_, parms, *body) = exp
        return Procedure(parms, body, env)
    elif exp[0] == 'define':
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)
    # ... more lines omitted

#Example 2-12. Pattern matching with match/case—requires Python ≥ 3.10
def evaluate(exp: Expression, env: Environment) -> Any:
    "Evaluate an expression in an environment."
    match exp:
    # ... lines omitted
        case ['quote', x]: 
            return x
        case ['if', test, consequence, alternative]: 
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body: 
            return Procedure(parms, body, env)
        case ['define', Symbol() as name, value_exp]: 
            env[name] = evaluate(value_exp, env)
        # ... more lines omitted
        case _: 
            raise SyntaxError(lispstr(exp))

#Table 2-2. Some Scheme syntactic forms and case patterns to handle them
Scheme syntax                               Sequence pattern
(quote exp)                                 ['quote', exp]
(if test conseq alt)                        ['if', test, conseq, alt]
(lambda (parms…) body1 body2…)              ['lambda', [*parms], *body] if body
(define name exp)                           ['define', Symbol() as name, exp]
(define (name parms…) body1 body2…)         ['define', [Symbol() as name, *parms], *body] if body

l = [10, 20, 30, 40, 50, 60]
l[:2] # split at 2
[10, 20]
l[2:]
[30, 40, 50, 60]
l[:3] # split at 3
[10, 20, 30]
l[3:]
[40, 50, 60]

s = 'bicycle'
s[::3]
'bye'
s[::-1]
'elcycib'
s[::-2]
'eccb'

deck[12::13]
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'),
Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]


invoice = """
... 0.....6.................................40........52...55........
... 1909 Pimoroni PiBrella $17.50 3 $52.50
... 1489 6mm Tactile Switch x20 $4.95 2 $9.90
... 1510 Panavise Jr. - PV-201 $28.00 1 $28.00
... 1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
... """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
... print(item[UNIT_PRICE], item[DESCRIPTION])
...
    $17.50 Pimoroni PiBrella
    $4.95 6mm Tactile Switch x20
    $28.00 Panavise Jr. - PV-201
    $34.95 PiTFT Mini Kit 320x240
 
 
l = list(range(10))
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
l
[0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
l
[0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
l
[0, 1, 20, 11, 5, 22, 9]
l[2:5] = 100 
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
l[2:5] = [100]
l
[0, 1, 100, 22, 9]
 
 
l = [1, 2, 3]
l * 5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
5 * 'abcd'
'abcdabcdabcdabcdabcd'

 
#Example 2-14. A list with three lists of length 3 can represent a tic-tac-toe board
board = [['_'] * 3 for i in range(3)] 
board
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X' 
board
[['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
 

#Example 2-15. A list with three references to the same list is useless
weird_board = [['_'] * 3] * 3 
weird_board
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weird_board[1][2] = 'O'
Using + and * with Sequences | 51
weird_board
[['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
 
 
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
 
 
board = []
for i in range(3):
...     row = ['_'] * 3 
...     board.append(row)
...
board
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[2][0] = 'X'
board 
[['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]
 
l = [1, 2, 3]
 id(l)
4311953800 
 l *= 2
 l
[1, 2, 3, 1, 2, 3]
 id(l)
4311953800 
 t = (1, 2, 3)
 id(t)
4312681568 
 t *= 2
 id(t)
4301348296
 
#Example 2-16. A riddle
t = (1, 2, [30, 40])
t[2] += [50, 60]

What happens next? Choose the best answer:
A. t becomes (1, 2, [30, 40, 50, 60]).
B. TypeError is raised with the message 'tuple' object does not support item
assignment.
C. Neither.
D. Both A and B.
 
t = (1, 2, [30, 40])
t[2] += [50, 60]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
t
(1, 2, [30, 40, 50, 60])
 
 
#Example 2-18. Bytecode for the expression s[a] += b
dis.dis('s[a] += b')
1       0 LOAD_NAME             0 (s)
        3 LOAD_NAME             1 (a)
        6 DUP_TOP_TWO
        7 BINARY_SUBSCR 
        8 LOAD_NAME             2 (b)
        11 INPLACE_ADD 
        12 ROT_THREE
        13 STORE_SUBSCR 
        14 LOAD_CONST           0 (None)
        17 RETURN_VALUE
 
 
fruits = ['grape', 'raspberry', 'apple', 'banana']
 sorted(fruits)
['apple', 'banana', 'grape', 'raspberry'] 
 fruits
['grape', 'raspberry', 'apple', 'banana'] 
 sorted(fruits, reverse=True)
['raspberry', 'grape', 'banana', 'apple'] 
 sorted(fruits, key=len)
['grape', 'apple', 'banana', 'raspberry'] 
 sorted(fruits, key=len, reverse=True)
['raspberry', 'banana', 'grape', 'apple'] 
 fruits
['grape', 'raspberry', 'apple', 'banana'] 
 fruits.sort() 
 fruits
['apple', 'banana', 'grape', 'raspberry']
 
#Example 2-19. Creating, saving, and loading a large array of floats
from array import array 
from random import random
floats = array('d', (random() for i in range(10**7))) 
floats[-1] 
0.07802343889111107
fp = open('floats.bin', 'wb')
floats.tofile(fp) 
fp.close()
floats2 = array('d') 
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7) 
fp.close()
floats2[-1] 
0.07802343889111107
floats2 == floats 
True


#Table 2-3. Methods and attributes found in list or array (deprecated array methods 
#and those also implemented by object are omitted for brevity)
                                        list    array
s.__add__(s2)                           ●       ●       s + s2—concatenation
s.__iadd__(s2)                          ●       ●       s += s2—in-place concatenation
s.append(e)                             ●       ●       Append one element after last
s.byteswap()                                    ●       Swap bytes of all items in array for endianness conversion
s.clear()                               ●               Delete all items
s.__contains__(e)                       ●       ●       e in s
s.copy()                                ●               Shallow copy of the list
s.__copy__()                                    ●       Support for copy.copy
s.count(e)                              ●       ●       Count occurrences of an element
s.__deepcopy__()                                ●       Optimized support for copy.deepcopy
s.__delitem__(p)                        ●       ●       Remove item at position p
s.extend(it)                            ●       ●       Append items from iterable it
s.frombytes(b)                                  ●       Append items from byte sequence interpreted as packed machine values
s.fromfile(f, n)                                ●       Append n items from binary file f interpreted as packed machine values
s.fromlist(l)                                   ●       Append items from list; if one causes TypeError, none are appended
s.__getitem__(p)                        ●       ●       s[p]—get item or slice at position
s.index(e)                              ●       ●       Find position of first occurrence of e
s.insert(p, e)                          ●       ●       Insert element e before the item at position p
s.itemsize                                      ●       Length in bytes of each array item
s.__iter__()                            ●       ●       Get iterator
s.__len__()                             ●       ●       len(s)—number of items
s.__mul__(n)                            ●       ●       s * n—repeated concatenation
s.__imul__(n)                           ●       ●       s *= n—in-place repeated concatenation
s.__rmul__(n)                           ●       ●       n * s—reversed repeated concatenationa
s.pop([p])                              ●       ●       Remove and return item at position p (default: last)
s.remove(e)                             ●       ●       Remove first occurrence of element e by value
s.reverse()                             ●       ●       Reverse the order of the items in place
s.__reversed__()                        ●               Get iterator to scan items from last to first
s.__setitem__(p, e)                     ●       ●       s[p] = e—put e in position p, overwriting existing item or slice
s.sort([key], [reverse])                ●               Sort items in place with optional keyword arguments key and reverse
s.tobytes()                                     ●       Return items as packed machine values in a bytes object
s.tofile(f)                                     ●       Save items as packed machine values to binary file f
s.tolist()                                      ●       Return items as numeric objects in a list
s.typecode                                      ●       One-character string identifying the C type of the items
 Reversed operators are explained in Chapter 16.


#Example 2-20. Handling 6 bytes of memory as 1×6, 2×3, and 3×2 views
from array import array
octets = array('B', range(6)) 
m1 = memoryview(octets) 
m1.tolist()
[0, 1, 2, 3, 4, 5]
m2 = m1.cast('B', [2, 3]) 
m2.tolist()
[[0, 1, 2], [3, 4, 5]]
m3 = m1.cast('B', [3, 2]) 
m3.tolist()
[[0, 1], [2, 3], [4, 5]]
m2[1,1] = 22 
m3[1,1] = 33 
octets 
array('B', [0, 1, 2, 33, 22, 5])


#Example 2-21. Changing the value of a 16-bit integer array item by poking one of its bytes
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers) 
len(memv)
5
memv[0] 
-2
memv_oct = memv.cast('B') 
memv_oct.tolist() 
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4 
numbers
array('h', [-2, -1, 1024, 1, 2])


#Example 2-22. Basic operations with rows and columns in a numpy.ndarray
import numpy as np
a = np.arange(12) 
a
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
type(a)
<class 'numpy.ndarray'>
a.shape 
(12,)
a.shape = 3, 4 
a
array([[ 0, 1, 2, 3],
        [ 4, 5, 6, 7],
        [ 8, 9, 10, 11]])
a[2] 
array([ 8, 9, 10, 11])
a[2, 1] 
9
a[:, 1] 
array([1, 5, 9])
a.transpose() 
array([[ 0, 4, 8],
        [ 1, 5, 9],
        [ 2, 6, 10],
        [ 3, 7, 11]])


import numpy
floats = numpy.loadtxt('floats-10M-lines.txt') 
When a List Is Not the Answer | 65
floats[-3:] 
array([ 3016362.69195522, 535281.10514262, 4566560.44373946])
floats *= .5 
floats[-3:]
array([ 1508181.34597761, 267640.55257131, 2283280.22186973])
from time import perf_counter as pc
t0 = pc(); floats /= 3; pc() - t0
0.03690556302899495
numpy.save('floats-10M', floats) 
floats2 = numpy.load('floats-10M.npy', 'r+') 
floats2 *= 6
floats2[-3:] 
memmap([ 3016362.69195522, 535281.10514262, 4566560.44373946])


#Example 2-23. Working with a deque
from collections import deque
dq = deque(range(10), maxlen=10) 
dq
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3) 
dq
deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-4)
dq
deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
dq.appendleft(-1) 
dq
deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.extend([11, 22, 33]) 
dq
deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
dq.extendleft([10, 20, 30, 40]) 
dq
deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)



#Table 2-4. Methods implemented in list or deque (those that are also implemented by
#object are omitted for brevity)
                                    list        deque
s.__add__(s2)                       ●                   s + s2—concatenation
s.__iadd__(s2)                      ●           ●       s += s2—in-place concatenation
s.append(e)                         ●           ●       Append one element to the right (after last)
s.appendleft(e)                                 ●       Append one element to the left (before first)
s.clear()                           ●           ●       Delete all items
s.__contains__(e)                   ●                   e in s
s.copy()                            ●                   Shallow copy of the list
s.__copy__()                                    ●       Support for copy.copy (shallow copy)
s.count(e)                          ●           ●       Count occurrences of an element
s.__delitem__(p)                    ●           ●       Remove item at position p
s.extend(i)                         ●           ●       Append items from iterable i to the right
s.extendleft(i)                                 ●       Append items from iterable i to the left
s.__getitem__(p)                    ●           ●       s[p]—get item or slice at position
s.index(e)                          ●                   Find position of first occurrence of e
s.insert(p, e)                      ●                   Insert element e before the item at position p
s.__iter__()                        ●           ●       Get iterator
s.__len__()                         ●           ●       len(s)—number of items
s.__mul__(n)                        ●                   s * n—repeated concatenation
s.__imul__(n)                       ●                   s *= n—in-place repeated concatenation
s.__rmul__(n)                       ●                   n * s—reversed repeated concatenationa
s.pop()                             ●           ●       Remove and return last itemb
s.popleft()                                     ●       Remove and return first item
s.remove(e)                         ●           ●       Remove first occurrence of element e by value
s.reverse()                         ●           ●       Reverse the order of the items in place
s.__reversed__()                    ●           ●       Get iterator to scan items from last to first
s.rotate(n)                                     ●       Move n items from one end to the other
s.__setitem__(p, e)                 ●           ●       s[p] = e—put e in position p, overwriting existing item or slice
s.sort([key], [reverse])            ●                   Sort items in place with optional keyword arguments key and reverse
Reversed operators are explained in Chapter 16.
a_list.pop(p) allows removing from position p, but deque does not support that option





names = []

















