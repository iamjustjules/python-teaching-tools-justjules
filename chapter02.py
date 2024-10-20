message = "Hello Python world!"
print(message)


message = "Hello Python Crash Course world!"
print(message)


# an errror will occur if you run this code
message = "Hello Python Crash Course reader!"
print(message)


name = "ada lovelace"
print(name.title())


name = "Ada Lovelace"
print(name.upper())
print(name.lower())


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)


print("Python")
#Python
print("\tPython")
#   Python


print("Languages:\nPython\nC\nJavaScript")
Languages:
#Python
#C
#JavaScript


print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
#   Python
#   C
#   JavaScript


favorite_language = 'python '
favorite_language
#'python '
favorite_language.rstrip()
#'python'
favorite_language
#'python '


favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language
#'python'


favorite_language = ' python '
favorite_language.rstrip()
#' python'
favorite_language.lstrip()
#'python '
favorite_language.strip()
#'python'


nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
#'nostarch.com'


simple_url = nostarch_url.removeprefix('https://')


message = "One of Python's strengths is its diverse community."
print(message)


# if you use single quotes, Python can’t identify where the string should end:
#message = 'One of Python's strengths is its diverse community.'
print(message)


#message = 'One of Python's strengths is its diverse community.'
print(message)
#You’ll see the following output:
# File "apostrophe.py", line 1
#   message = 'One of Python's strengths is its diverse community.'
#SyntaxError: unterminated string literal (detected at line 1)


2 + 3
#5
3 - 2
#1
2 * 3
#6
3 / 2
#1.5


3 ** 2
#9
3 ** 3
#27
10 ** 6
#1000000


2 + 3*4
#14
(2 + 3) * 4
#20


0.1 + 0.1
#0.2
0.2 + 0.2
#0.4
2 * 0.1
#0.2
2 * 0.2
#0.4


0.2 + 0.1
#0.30000000000000004
3 * 0.1
#0.30000000000000004


4/2
#2.0


1 + 2.0
#3.0
2 * 3.0
#6.0
3.0 ** 2
#9.0


universe_age = 14_000_000_000
print(universe_age)
#14000000000


x, y, z = 0, 0, 0


MAX_CONNECTIONS = 5000


#Say hello to everyone.
print("Hello Python people!")


import this
#The Zen of Python, by Tim Peters
#Beautiful is better than ugly.



