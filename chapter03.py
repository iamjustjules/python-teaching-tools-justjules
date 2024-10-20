Example 3-1. Examples of dict comprehensions
 dial_codes = [ 
... (880, 'Bangladesh'),
... (55, 'Brazil'),
... (86, 'China'),
... (91, 'India'),
... (62, 'Indonesia'),
... (81, 'Japan'),
... (234, 'Nigeria'),
... (92, 'Pakistan'),
... (7, 'Russia'),
... (1, 'United States'),
... ]
 country_dial = {country: code for code, country in dial_codes} 
 country_dial
{'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62,
'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}
 {code: country.upper() 
...     for country, code in sorted(country_dial.items())
...     if code < 70}
{55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}





def dump(**kwargs):
... return kwargs
...
dump(**{'x': 1}, y=2, **{'z': 3})
{'x': 1, 'y': 2, 'z': 3}

{'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}
{'a': 0, 'x': 4, 'y': 2, 'z': 3}




d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 | d2
{'a': 2, 'b': 4, 'c': 6}

d1
{'a': 1, 'b': 3}
d1 |= d2
d1
{'a': 2, 'b': 4, 'c': 6}




def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}: 
            return names
        case {'type': 'book', 'api': 1, 'author': name}: 
            return [name]
        case {'type': 'book'}: 
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}: 
            return [name]
        case _: 
            raise ValueError(f'Invalid record: {record!r}')
        
        
        
b1 = dict(api=1, author='Douglas Hofstadter',
... type='book', title='Gödel, Escher, Bach')
get_creators(b1)
['Douglas Hofstadter']
from collections import OrderedDict
b2 = OrderedDict(api=2, type='book',
... title='Python in a Nutshell',
... authors='Martelli Ravenscroft Holden'.split())
get_creators(b2)
['Martelli', 'Ravenscroft', 'Holden']
get_creators({'type': 'book', 'pages': 770})
Traceback (most recent call last):
 ...
ValueError: Invalid 'book' record: {'type': 'book', 'pages': 770}
get_creators('Spam, spam, spam')
Traceback (most recent call last):
 ...
ValueError: Invalid record: 'Spam, spam, spam'

        
food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
... case {'category': 'ice cream', **details}:
... print(f'Ice cream details: {details}')
...
Ice cream details: {'flavor': 'vanilla', 'cost': 199}
        
        
        
        
my_dict = {}
isinstance(my_dict, abc.Mapping)
True
isinstance(my_dict, abc.MutableMapping)
True        
        
        
        
        
tt = (1, 2, (30, 40))
hash(tt)
8027212646858338501
tl = (1, 2, [30, 40])
hash(tl)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
tf = (1, 2, frozenset([30, 40]))
hash(tf)
-4118419923444501110
        
        
        
        
        
Table 3-1. Methods of the mapping types dict, collections.defaultdict, and collec
tions.OrderedDict (common object methods omitted for brevity); optional arguments are
enclosed in […]
                            dict    defaultdict     OrderedDict
d.clear()                   ●           ●               ●           Remove all items
d.__contains__(k)           ●           ●               ●           k in d
d.copy()                    ●           ●               ●           Shallow copy
d.__copy__()                            ●                           Support for copy.copy(d)
d.default_factory                       ●                           Callable invoked by __missing__ to set missing valuesa
d.__delitem__(k)            ●           ●               ●           del d[k]—remove item with key k 
d.fromkeys(it, [initial])   ●           ●               ●           New mapping from keys in iterable, with optional initial value (defaults to None)
d.get(k, [default])         ●           ●               ●           Get item with key k, return default or None if missing
d.__getitem__(k)            ●           ●               ●           d[k]—get item with key k
d.items()                   ●           ●               ●           Get view over items—(key, value) pairs
d.__iter__()                ●           ●               ●           Get iterator over keys
d.keys()                    ●           ●               ●           Get view over keys
d.__len__()                 ●           ●               ●           len(d)—number of items
d.__missing__(k)                        ●                           Called when __getitem__ cannot find the key
d.move_to_end(k, [last])                                ●           Move k first or last position (last is True by default)
d.__or__(other)             ●           ●               ●           Support for d1 | d2 to create new dict merging d1 and d2 (Python ≥ 3.9)
d.__ior__(other)            ●           ●               ●           Support for d1 |= d2 to update d1 with d2 (Python ≥ 3.9)
d.pop(k, [default])         ●           ●               ●           Remove and return value at k, or default or None if missing
d.popitem()                 ●           ●               ●           Remove and return the last inserted item as (key, value) b
d.__reversed__()            ●           ●               ●           Support for reverse(d)—returns iterator for keys from last to first inserted.
d.__ror__(other)            ●           ●               ●           Support for other | dd— reversed union operator (Python ≥ 3.9)c
d.setdefault(k, [default])  ●           ●               ●           If k in d, return d[k]; else set d[k] = default and return it
d.__setitem__(k, v)         ●           ●               ●           d[k] = v—put v at k 
d.update(m, [**kwargs])     ●           ●               ●           Update d with items from mapping or iterable of (key, value) pairs
d.values()                  ●           ●               ●           Get view over values
- default_factory is not a method, but a callable attribute set by the end user when a defaultdict is instantiated.
- OrderedDict.popitem(last=False) removes the first item inserted (FIFO). The last keyword argument is not
supported in dict or defaultdict as recently as Python 3.10b3.
- Reversed operators are explained in Chapter 16        
        
        
Example 3-3. Partial output from Example 3-4 processing the “Zen of Python”;
each line shows a word and a list of occurrences coded as pairs:
(line_number, column_number)
$ python3 index0.py zen.txt
a [(19, 48), (20, 53)]
Although [(11, 1), (16, 1), (18, 1)]
ambiguity [(14, 16)]
and [(15, 23)]
are [(21, 12)]
aren [(10, 15)]
at [(16, 38)]
bad [(19, 50)]
Standard API of Mapping Types | 87
4 The original script appears in slide 41 of Martelli’s “Re-learning Python” presentation. His script is actually a
demonstration of dict.setdefault, as shown in our Example 3-5.
be [(15, 14), (16, 27), (20, 50)]
beats [(11, 23)]
Beautiful [(3, 1)]
better [(3, 14), (4, 13), (5, 11), (6, 12), (7, 9), (8, 11), (17, 8), (18, 25)]
...
        
#Example 3-4 is a suboptimal script written to show one case where dict.get is not
#the best way to handle a missing key. I adapted it from an example by Alex Martelli.4

#Example 3-4. index0.py uses dict.get to fetch and update a list of word occurrences
#from the index (a better solution is in Example 3-5)

#"""Build an index mapping word -> list of occurrences"""

import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, []) 
            occurrences.append(location) 
            index[word] = occurrences 
# display in alphabetical order
for word in sorted(index, key=str.upper): 
    print(word, index[word])

            
        
#Example 3-5. index.py uses dict.setdefault to fetch and update a list of word
#occurrences from the index in a single line; contrast with Example 3-4

#"""Build an index mapping word -> list of occurrences"""

import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location) 
# display in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
        
        
my_dict.setdefault(key, []).append(new_value)
…is the same as running…

 my_dict[key] = []
my_dict[key].append(new_value)
        
   
#Example 3-6. index_default.py: using defaultdict instead of the setdefault method

#"""Build an index mapping word -> list of occurrences"""

import collections
import re
import sys

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list) 
with open(sys.argv[1], encoding='utf-8') as fp:
     for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location) 
# display in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])      
        
        
#Example 3-7. When searching for a nonstring key, StrKeyDict0 converts it to str
#when it is not found
#Tests for item retrieval using `d[key]` notation::
d = StrKeyDict0([('2', 'two'), ('4', 'four')])
d['2']
 'two'
d[4]
 'four'
d[1]
 Traceback (most recent call last):
 ...
 KeyError: '1'
Tests for item retrieval using `d.get(key)` notation::
d.get('2')
 'two'
d.get(4)
 'four'
d.get(1, 'N/A')
 'N/A'
Tests for the `in` operator::
2 in d
 True
1 in d
 False
    
    
#Example 3-8 implements a class StrKeyDict0 that passes the preceding doctests.
#Example 3-8. StrKeyDict0 converts nonstring keys to str on lookup (see tests in Example 3-7)
class StrKeyDict0(dict): 
    
 def __missing__(self, key):
    if isinstance(key, str): 
       raise KeyError(key)
    return self[str(key)] 
 def get(self, key, default=None):
    try:
        return self[key] 
    except KeyError:
        return default 
 def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()    
    
    
    
d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
from collections import ChainMap
chain = ChainMap(d1, d2)
chain['a']
1
chain['c']
6
    
    
chain['c'] = -1
d1
{'a': 1, 'b': 3, 'c': -1}
d2
{'a': 2, 'b': 4, 'c': 6}

    
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))
    
    
ct = collections.Counter('abracadabra')
ct
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')
ct
Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.most_common(3)
[('a', 10), ('z', 3), ('b', 2)]
    
    
import collections

class StrKeyDict(collections.UserDict): 
    
    def __missing__(self, key): 
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self, key):
        return str(key) in self.data 
    def __setitem__(self, key, item):
        self.data[str(key)] = item 
    
    
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
d_proxy
mappingproxy({1: 'A'})
d_proxy[1] 
'A'
d_proxy[2] = 'x' 
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
d_proxy 
mappingproxy({1: 'A', 2: 'B'})
d_proxy[2]
'B'
    
    
d = dict(a=10, b=20, c=30)
values = d.values()
values
dict_values([10, 20, 30]) 
len(values) 
3
list(values) 
[10, 20, 30]
reversed(values) 
<dict_reversevalueiterator object at 0x10e9e7310>
values[0]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'dict_values' object is not subscriptable 
    
    
d['z'] = 99
d
{'a': 10, 'b': 20, 'c': 30, 'z': 99}
values
dict_values([10, 20, 30, 99])
 
    
values_class = type({}.values())
v = values_class()
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: cannot create 'dict_values' instances
    
    
    
l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
set(l)
{'eggs', 'spam', 'bacon'}
list(set(l))
['eggs', 'spam', 'bacon']    
    
    
    
found = len(needles & haystack)    
    
found = 0
for n in needles:
    if n in haystack:
        found += 1    
    
    
    
s = {1}
type(s)
<class 'set'>
s
{1}
s.pop()
1
s
set()
    
    
frozenset(range(10))
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    
    
from unicodedata import name 
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')} 
{'§', '=', '¢', '#', '¤', '<', '¥', 'µ', '×', '$', '¶', '£', '©',
'°', '+', '÷', '±', '>', '¬', '®', '%'}    
    
    
    
#Table 3-2. Mathematical set operations: these methods either produce a new set or update
#the target set in place, if it’s mutable
Math symbol     Python operator Method                                  Description
S ∩ Z           s & z           s.__and__(z)                            Intersection of s and z
                z & s           s.__rand__(z)                           Reversed & operator
                                s.intersection(it, …)                   Intersection of s and all sets built from iterables it, etc.
                s &= z          s.__iand__(z) s                         updated with intersection of s and z
                                s.intersection_update(it, …)            s updated with intersection of s and all sets built from iterables it, etc.
S ∪ Z           s | z           s.__or__(z)                             Union of s and z
                z | s           s.__ror__(z)                            Reversed |
                                s.union(it, …)                          Union of s and all sets built from iterables it, etc.
                s |= z          s.__ior__(z)                            s updated with union of s and z
                                s.update(it, …)                         s updated with union of s and all sets built from iterables it, etc.
S \ Z           s - z           s.__sub__(z)                            Relative complement or difference between s and z
                z - s           s.__rsub__(z)                           Reversed - operator
                                s.difference(it, …)                     Difference between s and all sets built from iterables it, etc.
                s -= z          s.__isub__(z)                           s updated with difference between s and z
                                s.difference_update(it, …)              s updated with difference between s and all sets built from iterables it, etc.
S ∆ Z           s ^ z           s.__xor__(z)                            Symmetric difference (the complement of the intersection s & z)
                z ^ s           s.__rxor__(z)                           Reversed ^ operator
                                s.symmetric_difference(it)              Complement of s & set(it)
                s ^= z          s.__ixor__(z)                           s updated with symmetric difference of s and z
                                s.symmetric_difference_update(it, …)    s updated with symmetric difference of s and all sets built from iterables it, etc.        
        
        
#Table 3-3 lists set predicates: operators and methods that return True or False.
#Table 3-3. Set comparison operators and methods that return a bool
Math symbol     Python operator     Method                          Description
S ∩ Z = ∅                           s.isdisjoint(z)                 s and z are disjoint (no elements in common)
e ∈ S           e in s              s.__contains__(e)               Element e is a member of s
S ⊆ Z           s <= z              s.__le__(z)                     s is a subset of the z set
                                    s.issubset(it)                  s is a subset of the set built from the iterable it
S ⊂ Z           s < z               s.__lt__(z)                     s is a proper subset of the z set
S ⊇ Z           s >= z              s.__ge__(z)                     s is a superset of the z set
                                    s.issuperset(it)                s is a superset of the set built from the iterable it
S ⊃ Z           s > z               s.__gt__(z)                     s is a proper superset of the z set        
        
        
#Table 3-4. Additional set methods
                set frozenset
s.add(e)        ●                       Add element e to s
s.clear()       ●                       Remove all elements of s
s.copy()        ●   ●                   Shallow copy of s
s.discard(e)    ●                       Remove element e from s if it is present
s.__iter__()    ●   ●                   Get iterator over s
s.__len__()     ●   ●                   len(s)
s.pop()         ●                       Remove and return an element from s, raising KeyError if s is empty
s.remove(e)     ●                       Remove element e from s, raising KeyError if e not in s        
        
        
        

#Table 3-5. Methods implemented by frozenset, dict_keys, and dict_items
                            frozenset   dict_keys   dict_items      Description
s.__and__(z)                ●           ●           ●               s & z (intersection of s and z)
s.__rand__(z)               ●           ●           ●               Reversed & operator
s.__contains__()            ●           ●           ●               e in s
s.copy()                    ●                                       Shallow copy of s
s.difference(it, …)         ●                                       Difference between s and iterables it, etc.
s.intersection(it, …)       ●                                       Intersection of s and iterables it, etc.
s.isdisjoint(z)             ●           ●           ●               s and z are disjoint (no elements in common)
s.issubset(it)              ●                                       s is a subset of iterable it
s.issuperset(it)            ●                                       s is a superset of iterable it
s.__iter__()                ●           ●           ●               Get iterator over s
s.__len__()                 ●           ●           ●               len(s)
s.__or__(z)                 ●           ●           ●               s | z (union of s and z)
s.__ror__()                 ●           ●           ●               Reversed | operator
s.__reversed__()                        ●           ●               Get iterator over s in reverse order
s.__rsub__(z)               ●           ●           ●               Reversed - operator
s.__sub__(z)                ●           ●           ●               s - z (difference between s and z)
s.symmetric_difference(it)  ●                                       Complement of s & set(it)
s.union(it, …)              ●                                       Union of s and iterables it, etc.
s.__xor__()                 ●           ●           ●               s ^ z (symmetric difference of s and z)
s.__rxor__()                ●           ●           ●               Reversed ^ operator        
        
        
d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)
d1.keys() & d2.keys()
{'b', 'd'}        
        
        
s = {'a', 'e', 'i'}
d1.keys() & s
{'a'}
d1.keys() | s
{'a', 'c', 'b', 'd', 'i', 'e'}        
        
        
