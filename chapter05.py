Example 5-1. class/coordinates.py
class Coordinate:
 def __init__(self, lat, lon):
 self.lat = lat
 self.lon = lon
 
 
from coordinates import Coordinate
moscow = Coordinate(55.76, 37.62)
moscow
<coordinates.Coordinate object at 0x107142f10> 
location = Coordinate(55.76, 37.62)
location == moscow 
False
(location.lat, location.lon) == (moscow.lat, moscow.lon) 
True
 
 
from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
issubclass(Coordinate, tuple)
True
moscow = Coordinate(55.756, 37.617)
moscow
Coordinate(lat=55.756, lon=37.617) 
moscow == Coordinate(lat=55.756, lon=37.617) 
True
 
 
import typing
Coordinate = typing.NamedTuple('Coordinate',
... [('lat', float), ('lon', float)])
issubclass(Coordinate, tuple)
True
typing.get_type_hints(Coordinate)
{'lat': <class 'float'>, 'lon': <class 'float'>}

 
#Example 5-2. typing_namedtuple/coordinates.py
from typing import NamedTuple
class Coordinate(NamedTuple):
 lat: float
 lon: float
 def __str__(self):
 ns = 'N' if self.lat >= 0 else 'S'
 we = 'E' if self.lon >= 0 else 'W'
 return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

 
#Example 5-3. dataclass/coordinates.py
from dataclasses import dataclass
@dataclass(frozen=True)
class Coordinate:
 lat: float
 lon: float
 def __str__(self):
 ns = 'N' if self.lat >= 0 else 'S'
 we = 'E' if self.lon >= 0 else 'W'
 return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

 
 
#Table 5-1. Selected features compared across the three data class builders; x stands for an instance of a data class of that kind
                        namedtuple          NamedTuple          dataclass
mutable instances       NO                  NO                  YES
class statement syntax  NO                  YES                 YES
construct dict          x._asdict()         x._asdict()         dataclasses.asdict(x)
get field names         x._fields           x._fields           [f.name for f in dataclasses.fields(x)]
get defaults            x._field_defaults   x._field_defaults   [f.default for f in dataclasses.fields(x)]
get field types         N/A                 x.__annotations__   x.__annotations__
new instance with       x._replace(…)       x._replace(…)       dataclasses.replace(x, …)
changes 
new class at runtime    namedtuple(…)       NamedTuple(…)       dataclasses.make_dataclass(…)
 
 
#Example 5-4 shows how we could define a named tuple to hold information about a city.
Example 5-4. Defining and using a named tuple type
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates') 
Classic Named Tuples | 169
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) 
tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
139.691667))
tokyo.population 
36.933
tokyo.coordinates
(35.689722, 139.691667)
tokyo[1]
'JP'
 
 
#Example 5-5. Named tuple attributes and methods (continued from the previous example)
City._fields 
('name', 'country', 'population', 'location')
Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
delhi = City._make(delhi_data) 
delhi._asdict() 
{'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935,
'location': Coordinate(lat=28.613889, lon=77.208889)}
import json
json.dumps(delhi._asdict()) 
'{"name": "Delhi NCR", "country": "IN", "population": 21.935,
"location": [28.613889, 77.208889]}'
 
 
#Example 5-6. Named tuple attributes and methods, continued from Example 5-5
Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
Coordinate(0, 0)
Coordinate(lat=0, lon=0, reference='WGS84')
Coordinate._field_defaults
{'reference': 'WGS84'}

 
#Example 5-7. frenchdeck.doctest: Adding a class attribute and a method to Card, the namedtuple from “A Pythonic Card Deck” on page 5
Card.suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0) 
def spades_high(card): 
... rank_value = FrenchDeck.ranks.index(card.rank)
4 If you know Ruby, you know that injecting methods is a well-known but controversial technique among
Rubyists. In Python, it’s not as common, because it doesn’t work with any built-in type—str, list, etc. I con‐
sider this limitation of Python a blessing.
... suit_value = card.suit_values[card.suit]
... return rank_value * len(card.suit_values) + suit_value
...
Card.overall_rank = spades_high 
lowest_card = Card('2', 'clubs')
highest_card = Card('A', 'spades')
lowest_card.overall_rank() 
0
highest_card.overall_rank()
51

 
#Example 5-8. typing_namedtuple/coordinates2.py
from typing import NamedTuple
class Coordinate(NamedTuple):
 lat: float 
 lon: float
 reference: str = 'WGS84'
 
 
#Example 5-9. Python does not enforce type hints at runtime
import typing
class Coordinate(typing.NamedTuple):
... lat: float
... lon: float
...
trash = Coordinate('Ni!', None)
print(trash)
Coordinate(lat='Ni!', lon=None)
 
 
$ python3 nocheck_demo.py
Coordinate(lat='Ni!', lon=None)
 
 
$ mypy nocheck_demo.py
nocheck_demo.py:8: error: Argument 1 to "Coordinate" has
incompatible type "str"; expected "float"
nocheck_demo.py:8: error: Argument 2 to "Coordinate" has
incompatible type "None"; expected "float"

var_name: some_type
 
var_name: some_type = a_value
 
 
#Example 5-10. meaning/demo_plain.py: a plain class with type hints
class DemoPlainClass:
 a: int 
 b: float = 1.1 
 c = 'spam' 
 
 
from demo_plain import DemoPlainClass
DemoPlainClass.__annotations__
{'a': <class 'int'>, 'b': <class 'float'>}
DemoPlainClass.a
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
AttributeError: type object 'DemoPlainClass' has no attribute 'a'
DemoPlainClass.b
1.1
DemoPlainClass.c
'spam'
 
 
#Example 5-11. meaning/demo_nt.py: a class built with typing.NamedTuple
import typing
class DemoNTClass(typing.NamedTuple):
 a: int 
 b: float = 1.1 
 c = 'spam' 
 
 
from demo_nt import DemoNTClass
DemoNTClass.__annotations__
{'a': <class 'int'>, 'b': <class 'float'>}
DemoNTClass.a
<_collections._tuplegetter object at 0x101f0f940>
DemoNTClass.b
<_collections._tuplegetter object at 0x101f0f8b0>
DemoNTClass.c
'spam'
 
 
DemoNTClass.__doc__
'DemoNTClass(a, b)'

 
nt = DemoNTClass(8)
nt.a
8
nt.b
1.1
nt.c
'spam'
 
 
#Example 5-12. meaning/demo_dc.py: a class decorated with @dataclass

from dataclasses import dataclass

@dataclass
class DemoDataClass:
 a: int 
 b: float = 1.1 
 c = 'spam'
 
 
from demo_dc import DemoDataClass
DemoDataClass.__annotations__
{'a': <class 'int'>, 'b': <class 'float'>}
DemoDataClass.__doc__
'DemoDataClass(a: int, b: float = 1.1)'
DemoDataClass.a
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
AttributeError: type object 'DemoDataClass' has no attribute 'a'
DemoDataClass.b
1.1
DemoDataClass.c
'spam'

 
dc = DemoDataClass(9)
dc.a
9
dc.b
1.1
dc.c
'spam'

 
dc.a = 10
dc.b = 'oops'

dc.c = 'whatever'
dc.z = 'secret stash'
 
 
@dataclass(*, init=True, repr=True, eq=True, order=False,
 unsafe_hash=False, frozen=False)

 
#Table 5-2. Keyword parameters accepted by the @dataclass decorator 
Option              Meaning                 Default     Notes
init                Generate __init__       True        Ignored if __init__ is implemented by
                                                        user.
repr                Generate __repr__       True        Ignored if __repr__ is implemented by
                                                        user.
eq                  Generate __eq__         True        Ignored if __eq__ is implemented by
                                                        user.
order               Generate __lt__,        False       If True, raises exceptions if eq=False,
                    __le__, __gt__,                     or if any of the comparison methods that
                    __ge__                              would be generated are defined or inherited.                                                      
unsafe_hash         Generate __hash__       False       Complex semantics and several caveats—
                                                        see: dataclass documentation.
frozen              Make instances          False       Instances will be reasonably safe from
                    “immutable”                         accidental change, but not really
                                                        immutable.a 
 
 
#Example 5-13. dataclass/club_wrong.py: this class raises ValueError
@dataclass
class ClubMember:
 name: str
 guests: list = [] 
 
$ python3 club_wrong.py
Traceback (most recent call last):
 File "club_wrong.py", line 4, in <module>
 class ClubMember:
 ...several lines omitted...
ValueError: mutable default <class 'list'> for field guests is not allowed:
use default_factory
 
 
#Example 5-14. dataclass/club.py: this ClubMember definition works
from dataclasses import dataclass, field
@dataclass
class ClubMember:
 name: str
 guests: list = field(default_factory=list)
 
 
#Example 5-15. dataclass/club_generic.py: this ClubMember definition is more precise
from dataclasses import dataclass, field
@dataclass
class ClubMember:
 name: str
 guests: list[str] = field(default_factory=list)
 
 
#Table 5-3. Keyword arguments accepted by the field function
Option              Meaning                                         Default
default             Default value for field                         _MISSING_TYPEa
default_factory     0-parameter function used to produce a default  _MISSING_TYPE
init                Include field in parameters to __init__         True
repr                Include field in __repr__                       True
compare             Use field in comparison methods __eq__,         True
                    __lt__, etc.
hash                Include field in __hash__ calculation           None
metadata            Mapping with user-defined data; ignored by      None
                    the @dataclass

 
@dataclass
class ClubMember:
 name: str
 guests: list = field(default_factory=list)
 athlete: bool = field(default=False, repr=False)
 
 
Example 5-16. dataclass/hackerclub.py: doctests for HackerClubMember
"""
``HackerClubMember`` objects accept an optional ``handle`` argument::
 anna = HackerClubMember('Anna Ravenscroft', handle='AnnaRaven')
 anna
 HackerClubMember(name='Anna Ravenscroft', guests=[], handle='AnnaRaven')
If ``handle`` is omitted, it's set to the first part of the member's name::
More About @dataclass | 183
 leo = HackerClubMember('Leo Rochael')
 leo
 HackerClubMember(name='Leo Rochael', guests=[], handle='Leo')
Members must have a unique handle. The following ``leo2`` will not be created,
because its ``handle`` would be 'Leo', which was taken by ``leo``::
 leo2 = HackerClubMember('Leo DaVinci')
 Traceback (most recent call last):
 ...
 ValueError: handle 'Leo' already exists.
To fix, ``leo2`` must be created with an explicit ``handle``::
 leo2 = HackerClubMember('Leo DaVinci', handle='Neo')
 leo2
 HackerClubMember(name='Leo DaVinci', guests=[], handle='Neo')
"""
 
HackerClubMember.__doc__
"HackerClubMember(name: str, guests: list = <factory>, handle: str = '')"
 
 
#Example 5-17. dataclass/hackerclub.py: code for HackerClubMember
from dataclasses import dataclass
from club import ClubMember
184 | Chapter 5: Data Class Builders
@dataclass
class HackerClubMember(ClubMember): 
 all_handles = set() 
 handle: str = '' 
 def __post_init__(self):
 cls = self.__class__ 
 if self.handle == '': 
 self.handle = self.name.split()[0]
 if self.handle in cls.all_handles: 
 msg = f'handle {self.handle!r} already exists.'
 raise ValueError(msg)
 cls.all_handles.add(self.handle)
 
 
$ mypy hackerclub.py
hackerclub.py:37: error: Need type annotation for "all_handles"
(hint: "all_handles: Set[<type>] = ...")
Found 1 error in 1 file (checked 1 source file)

 
all_handles: ClassVar[set[str]] = set()

all_handles is a class attribute of type set-of-str, with an empty set as its default
value.
 
 
#Example 5-18. Example from the dataclasses module documentation
@dataclass
class C:
 i: int
 j: int = None
 database: InitVar[DatabaseType] = None
 def __post_init__(self, database):
 if self.j is None and database is not None:
 self.j = database.lookup('j')
c = C(10, database=my_database)
 
 
Example 5-19. dataclass/resource.py: code for Resource, a class based on Dublin Core
terms
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum, auto
from datetime import date
class ResourceType(Enum): 
 BOOK = auto()
 EBOOK = auto()
 VIDEO = auto()
@dataclass
class Resource:
 """Media resource description."""
 identifier: str 
 title: str = '<untitled>' 
 creators: list[str] = field(default_factory=list)
 date: Optional[date] = None 
 type: ResourceType = ResourceType.BOOK 
 description: str = ''
 language: str = ''
 subjects: list[str] = field(default_factory=list)

 
#Example 5-20. dataclass/resource.py: code for Resource, a class based on Dublin Core terms
 description = 'Improving the design of existing code'
 book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
 ... ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19),
 ... ResourceType.BOOK, description, 'EN',
 ... ['computer programming', 'OOP'])
 book # doctest: +NORMALIZE_WHITESPACE
 Resource(identifier='978-0-13-475759-9', title='Refactoring, 2nd Edition',
 creators=['Martin Fowler', 'Kent Beck'], date=datetime.date(2018, 11, 19),
 type=<ResourceType.BOOK: 1>, description='Improving the design of existing code',
 language='EN', subjects=['computer programming', 'OOP'])

 book # doctest: +NORMALIZE_WHITESPACE
 Resource(
 identifier = '978-0-13-475759-9',
 title = 'Refactoring, 2nd Edition',
 creators = ['Martin Fowler', 'Kent Beck'],
 date = datetime.date(2018, 11, 19),
 type = <ResourceType.BOOK: 1>,
 description = 'Improving the design of existing code',
 language = 'EN',
 subjects = ['computer programming', 'OOP'],
 )
 
 
Example 5-21. dataclass/resource_repr.py: code for __repr__ method
implemented in the Resource class from Example 5-19
 def __repr__(self):
 cls = self.__class__
 cls_name = cls.__name__
 indent = ' ' * 4
 res = [f'{cls_name}('] 
 for f in fields(cls): 
 value = getattr(self, f.name) 
 res.append(f'{indent}{f.name} = {value!r},') 
 res.append(')') 
 return '\n'.join(res)
 
 
case [str(name), _, _, (float(lat), float(lon))]:

 
match x:
 case float():
 do_something_with(x)
 
match x:
 case float: # DANGER!!!
 do_something_with(x)

 
case [str(name), _, _, (float(lat), float(lon))]:
 
 
Example 5-22. City class and a few instances
import typing
class City(typing.NamedTuple):
 continent: str
 name: str
 country: str
cities = [
 City('Asia', 'Tokyo', 'JP'),
 City('Asia', 'Delhi', 'IN'),
 City('North America', 'Mexico City', 'MX'),
 City('North America', 'New York', 'US'),
 City('South America', 'São Paulo', 'BR'),
]

 
def match_asian_cities():
 results = []
 for city in cities:
 match city:
 case City(continent='Asia'):
 results.append(city)
 return results

 
def match_asian_countries():
 results = []
 for city in cities:
 match city:
 case City(continent='Asia', country=cc):
 results.append(cc)
 return results
 
 
match city:
 case City(continent='Asia', country=country):
 results.append(country)
 
 
def match_asian_cities_pos():
 results = []
 for city in cities:
 match city:
 case City('Asia'):
 results.append(city)
 return results
 
 
def match_asian_countries_pos():
 results = []
 for city in cities:
 match city:
 case City('Asia', _, country):
 results.append(country)
 return results
 

City.__match_args__
('continent', 'name', 'country') 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 