#Example 4-1. Encoding and decoding
s = 'café'
len(s) 
4
b = s.encode('utf8') 
b
b'caf\xc3\xa9' 
len(b) 
5
b.decode('utf8') 
'café'


#Example 4-2. A five-byte sequence as bytes and as bytearray
cafe = bytes('café', encoding='utf_8') 
cafe
b'caf\xc3\xa9'
cafe[0] 
99
cafe[:1] 
b'c'
cafe_arr = bytearray(cafe)
cafe_arr 
bytearray(b'caf\xc3\xa9')
cafe_arr[-1:] 
bytearray(b'\xa9')


bytes.fromhex('31 4B CE A9')
b'1K\xce\xa9'


#Example 4-3. Initializing bytes from the raw data of an array
import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) 
octets = bytes(numbers) 
octets
b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'


#Example 4-4. The string “El Niño” encoded with three codecs producing very different
#byte sequences
for codec in ['latin_1', 'utf_8', 'utf_16']:
... print(codec, 'El Niño'.encode(codec), sep='\t')
...
latin_1 b'El Ni\xf1o'
utf_8 b'El Ni\xc3\xb1o'
utf_16 b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'


#Figure 4-1 demonstrates a variety of codecs generating bytes from characters like the
#letter “A” through the G-clef musical symbol. Note that the last three encodings are
#variable-length, multibyte encodings.


Example 4-5. Encoding to bytes: success and error handling
city = 'São Paulo'
city.encode('utf_8') 
b'S\xc3\xa3o Paulo'
city.encode('utf_16')
b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
city.encode('iso8859_1') 
b'S\xe3o Paulo'
city.encode('cp437') 
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
 return codecs.charmap_encode(input,errors,encoding_map)
UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
position 1: character maps to <undefined>
city.encode('cp437', errors='ignore') 
b'So Paulo'
city.encode('cp437', errors='replace') 
b'S?o Paulo'
city.encode('cp437', errors='xmlcharrefreplace') 
b'S&#227;o Paulo'


#Example 4-6 illustrates how using the wrong codec may produce gremlins or a UnicodeDecodeError.
Example 4-6. Decoding from str to bytes: success and error handling
octets = b'Montr\xe9al' 
octets.decode('cp1252') 
'Montréal'
octets.decode('iso8859_7') 
'Montrιal'
octets.decode('koi8_r') 
'MontrИal'
octets.decode('utf_8') 
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:
invalid continuation byte
octets.decode('utf_8', errors='replace') 
'Montr�al'


SyntaxError: Non-UTF-8 code starting with '\xe1' in file ola.py on line
 1, but no encoding declared; see https://python.org/dev/peps/pep-0263/
 for details


#Example 4-7. ola.py: “Hello, World!” in Portuguese
# coding: cp1252
print('Olá, Mundo!')


$ chardetect 04-text-byte.asciidoc
04-text-byte.asciidoc: utf-8 with confidence 0.99


u16 = 'El Niño'.encode('utf_16')
u16
b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'


list(u16)
[255, 254, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]


u16le = 'El Niño'.encode('utf_16le')
list(u16le)
[69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]
u16be = 'El Niño'.encode('utf_16be')
list(u16be)
[0, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111]


#Example 4-8. A platform encoding issue (if you try this on your machine, you may or may not see the problem)
open('cafe.txt', 'w', encoding='utf_8').write('café')
4
open('cafe.txt').read()
'cafÃ©'


#Example 4-9. Closer inspection of Example 4-8 running on Windows reveals the bug and how to fix it
fp = open('cafe.txt', 'w', encoding='utf_8')
fp 
<_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf_8'>
fp.write('café') 
4
fp.close()
import os
os.stat('cafe.txt').st_size 
5
fp2 = open('cafe.txt')
fp2 
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='cp1252'>
fp2.encoding 
'cp1252'
fp2.read()
'cafÃ©'
fp3 = open('cafe.txt', encoding='utf_8') 
fp3
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='utf_8'>
fp3.read()
'café'
fp4 = open('cafe.txt', 'rb') 
fp4 
<_io.BufferedReader name='cafe.txt'>
fp4.read() 
b'caf\xc3\xa9'


#Example 4-10. Exploring encoding defaults

import locale
import sys

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(f'{expression:>30} -> {value!r}')



$ python3 default_encodings.py
 locale.getpreferredencoding() -> 'UTF-8'
 type(my_file) -> <class '_io.TextIOWrapper'>
 my_file.encoding -> 'UTF-8'
 sys.stdout.isatty() -> True
 sys.stdout.encoding -> 'utf-8'
 sys.stdin.isatty() -> True
 sys.stdin.encoding -> 'utf-8'
 sys.stderr.isatty() -> True
 sys.stderr.encoding -> 'utf-8'
 sys.getdefaultencoding() -> 'utf-8'
 sys.getfilesystemencoding() -> 'utf-8'


#Example 4-11. Default encodings on Windows 10 PowerShell (output is the same on cmd.exe)
> chcp 
Active code page: 437
> python default_encodings.py 
 locale.getpreferredencoding() -> 'cp1252' 
 type(my_file) -> <class '_io.TextIOWrapper'>
 my_file.encoding -> 'cp1252' 
 sys.stdout.isatty() -> True 
 sys.stdout.encoding -> 'utf-8' 
 sys.stdin.isatty() -> True
 sys.stdin.encoding -> 'utf-8'
 sys.stderr.isatty() -> True
 sys.stderr.encoding -> 'utf-8'
 sys.getdefaultencoding() -> 'utf-8'
 sys.getfilesystemencoding() -> 'utf-8'



Z:\>python default_encodings.py > encodings.log


#Example 4-12. stdout_check.py

import sys
from unicodedata import name

print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdout.encoding:', sys.stdout.encoding)
print()

test_chars = [
 '\N{HORIZONTAL ELLIPSIS}', # exists in cp1252, not in cp437
 '\N{INFINITY}', # exists in cp437, not in cp1252
 '\N{CIRCLED NUMBER FORTY TWO}', # not in cp437 or in cp1252
]

for char in test_chars:
 print(f'Trying to output {name(char)}:')
 print(char)


locale.getpreferredencoding(do_setlocale=True)
Return the encoding used for text data, according to user preferences. User pref‐
erences are expressed differently on different systems, and might not be available
programmatically on some systems, so this function only returns a guess. […]


s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
s1, s2
('café', 'café')
len(s1), len(s2)
(4, 5)
s1 == s2
False


from unicodedata import normalize
s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
len(s1), len(s2)
(4, 5)
len(normalize('NFC', s1)), len(normalize('NFC', s2))
(4, 4)
len(normalize('NFD', s1)), len(normalize('NFD', s2))
(5, 5)
normalize('NFC', s1) == normalize('NFC', s2)
True
normalize('NFD', s1) == normalize('NFD', s2)
True


from unicodedata import normalize, name
ohm = '\u2126'
name(ohm)
'OHM SIGN'
ohm_c = normalize('NFC', ohm)
name(ohm_c)
'GREEK CAPITAL LETTER OMEGA'
ohm == ohm_c
False
normalize('NFC', ohm) == normalize('NFC', ohm_c)
True


from unicodedata import normalize, name
half = '\N{VULGAR FRACTION ONE HALF}'
print(half)
½
normalize('NFKC', half)
'1⁄2'
Normalizing Unicode for Reliable Comparisons | 141
for char in normalize('NFKC', half):
... print(char, name(char), sep='\t')
...
1 DIGIT ONE
⁄ FRACTION SLASH
2 DIGIT TWO
four_squared = '4²'
normalize('NFKC', four_squared)
'42'
micro = 'µ'
micro_kc = normalize('NFKC', micro)
micro, micro_kc
('µ', 'μ')
ord(micro), ord(micro_kc)
(181, 956)
name(micro), name(micro_kc)
('MICRO SIGN', 'GREEK SMALL LETTER MU')


micro = 'µ'
name(micro)
'MICRO SIGN'
micro_cf = micro.casefold()
name(micro_cf)
'GREEK SMALL LETTER MU'
micro, micro_cf
('µ', 'μ')
eszett = 'ß'
name(eszett)
'LATIN SMALL LETTER SHARP S'
eszett_cf = eszett.casefold()
eszett, eszett_cf
('ß', 'ss')


#Example 4-13. normeq.py: normalized Unicode string comparison

"""
Utility functions for normalized Unicode string comparison.

Using Normal Form C, case sensitive:

 s1 = 'café'
 s2 = 'cafe\u0301'
 s1 == s2
 False
 nfc_equal(s1, s2)
 True
 nfc_equal('A', 'a')
 False

Using Normal Form C with case folding:

 s3 = 'Straße'
 s4 = 'strasse'
 s3 == s4
 False
 nfc_equal(s3, s4)
 False
 fold_equal(s3, s4)
 True
 fold_equal(s1, s2)
 True
 fold_equal('A', 'a')
 True

"""

from unicodedata import normalize

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)
    
def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
        normalize('NFC', str2).casefold())


#Example 4-14. simplify.py: function to remove all combining marks

import unicodedata
import string

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt) 
    shaved = ''.join(c for c in norm_txt
                    if not unicodedata.combining(c)) 
    return unicodedata.normalize('NFC', shaved)


#Example 4-15. Two examples using shave_marks from Example 4-14
order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
shave_marks(order)
'“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”' 
Greek = 'Ζέφυρος, Zéfiro'
shave_marks(Greek)
'Ζεφυρος, Zefiro'


#Example 4-16. Function to remove combining marks from Latin characters (import
#statements are omitted as this is part of the simplify.py module from Example 4-14)
def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt) 
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base: 
            continue # ignore diacritic on Latin base char
        preserve.append(c) 
        # if it isn't a combining char, it's a new base char
        if not unicodedata.combining(c): 
            latin_base = c in string.ascii_letters
    shaved = ''.join(preserve)
    return unicodedata.normalize('NFC', shaved)


#Example 4-17. Transform some Western typographical symbols into ASCII (this
#snippet is also part of simplify.py from Example 4-14)

single_map = str.maketrans("""‚ƒ„ˆ‹‘’“”•–—˜›""", 
 """'f"^<''""---~>""")

multi_map = str.maketrans({ 
 '€': 'EUR',
 '…': '...',
 'Æ': 'AE',
 'æ': 'ae',
 'Œ': 'OE',
 'œ': 'oe',
 '™': '(TM)',
 '‰': '<per mille>',
 '†': '**',
 '‡': '***',
})

multi_map.update(single_map) 

def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map) 

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt)) 
    no_marks = no_marks.replace('ß', 'ss') 
    return unicodedata.normalize('NFKC', no_marks)


#Example 4-18. Two examples using asciize from Example 4-17
order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
dewinize(order)
'"Herr Voß: - ½ cup of OEtker(TM) caffè latte - bowl of açaí."' 
asciize(order)
'"Herr Voss: - 1⁄2 cup of OEtker(TM) caffe latte - bowl of acai."'


fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted(fruits)
['acerola', 'atemoia', 'açaí', 'caju', 'cajá']


['açaí', 'acerola', 'atemoia', 'cajá', 'caju']


#Example 4-19. locale_sort.py: using the locale.strxfrm function as the sort key

import locale
my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(my_locale)
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)


'pt_BR.UTF-8'
['açaí', 'acerola', 'atemoia', 'cajá', 'caju']


#Example 4-20. Using the pyuca.Collator.sort_key method

import pyuca
coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
sorted_fruits
['açaí', 'acerola', 'atemoia', 'cajá', 'caju']


#Example 4-21. cf.py: the character finder utility

#!/usr/bin/env python3
import sys
import unicodedata

START, END = ord(' '), sys.maxunicode + 1 

def find(*query_words, start=START, end=END): 
    query = {w.upper() for w in query_words} 
    for code in range(start, end):
        char = chr(code) 
        name = unicodedata.name(char, None) 
        if name and query.issubset(name.split()): 
            print(f'U+{code:04X}\t{char}\t{name}') 
def main(words):
    if words:
        find(*words)
    else:
        print('Please provide words to find.')

if __name__ == '__main__':
    main(sys.argv[1:])


#Example 4-22. Demo of Unicode database numerical character metadata (callouts describe each column in the output)

import unicodedata
import re

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print(f'U+{ord(char):04x}', 
        char.center(6), 
        're_dig' if re_digit.match(char) else '-', 
        'isdig' if char.isdigit() else '-', 
        'isnum' if char.isnumeric() else '-', 
        f'{unicodedata.numeric(char):5.2f}', 
        unicodedata.name(char), 
        sep='\t')


#Example 4-23. ramanujan.py: compare behavior of simple str and bytes regular expressions

import re

re_numbers_str = re.compile(r'\d+') 
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+') 
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef" 
 " as 1729 = 1³ + 12³ = 9³ + 10³.") 

text_bytes = text_str.encode('utf_8') 

print(f'Text\n {text_str!r}')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str)) 
print(' bytes:', re_numbers_bytes.findall(text_bytes)) 
print('Words')
print(' str :', re_words_str.findall(text_str)) 
print(' bytes:', re_words_bytes.findall(text_bytes))


#Example 4-24. listdir with str and bytes arguments and results
os.listdir('.') 
['abc.txt', 'digits-of-π.txt']
os.listdir(b'.') 
[b'abc.txt', b'digits-of-\xcf\x80.txt']























































