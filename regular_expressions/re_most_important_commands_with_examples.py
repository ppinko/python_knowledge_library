"""
Python makes regular expressions available through the re module.
"""

import re

"""
re.match(regex, string) - Matching is done from the start of the
string only.

Return:
- if found  -> match object
- not found -> None
"""

pattern = r"123"
pattern2 = r"125"
string = "123zzb"

match = re.match(pattern, string)
print(match, match.group())

match2 = re.match(pattern2, string)
if match2 is None:
    print('There is no {0} at the beginning of the string'.format(pattern2))

print('-----------------------------------')
"""
re.search(regex, string) - Matching is done in the entire string

Return:
- if found  -> match object
- not found -> None
"""

pattern = r'vel'
word = 'developer'
match = re.search(pattern, word)
if match:
    print('"{0}" found at the index {1}'.format(pattern, word.index(pattern)))
    print(match.group())

print("+++++++++++++++++++++++++++++++++++")

pattern = r"your base"
sentence = "All your base are belong to us."

match = re.search(pattern, sentence)
print(match.group())    # 'your base'

match = re.search(r"belong.*", sentence)
print(match.group())    # 'belong to us.'

# You can also search at the beginning of the string (use ^ )
# and at the end of the string (use $ )
# or both (use both ^ and $ )

match = re.search(r"^123", "123zzb")
print(match.group(0))   # '123'

match = re.search(r"777$", "zzb777")
print(match.group(0))   # '777'

match = re.search(r"^123$", "123")
print(match.group(0))

print('-----------------------------------')

"""
re.findall(regex, string) - Return a list of all non-overlapping matches
in the string.

Return:
- if found  -> list of matches
- not found -> []
"""

pattern = r'an'
sentence = 'banana is not an anaconda'

matches = re.findall(pattern, sentence)
print(matches)  # ['an', 'an', 'an', 'an']

matches = re.findall(r'123', sentence)
print(matches)  # []

print('-----------------------------------')

"""
Flags - can change the behaviour of the Regular Expression.
Flags can be set in two ways, through the flags keyword or
directly in the expression.
"""

m = re.search("b", "ABC")
print(m is None)    # Out: True

m = re.search("b", "ABC", flags=re.IGNORECASE)
print(m.group())    # Out: 'B'

m = re.search("a.b", "A\nBC", flags=re.IGNORECASE)
print(m is None)    # Out: True

m = re.search("a.b", "A\nBC", flags=re.IGNORECASE|re.DOTALL)
print(m.group())    # Out: 'A\nB'

"""
Common flags:

Flag                    Short Description
re.IGNORECASE , re.I    Makes the pattern ignore the case
re.DOTALL , re.S        Makes . match everything including newlines
re.MULTILINE , re.M     Makes ^ match the begin of a line and $ the end of a line
re.DEBUG                Turns on debug information
"""

print('-----------------------------------')

"""
REPLACEMENT

re.sub(pattern, repl, string, count=0, flags=0) - Return the string obtained by
replacing the leftmost non-overlapping occurrences of the pattern in string by the
replacement repl. 
"""

## Replacing strings
print(re.sub(r"t[0-9][0-9]", "foo", "my name t13 is t44 what t99 ever t44"))
# Out: 'my name foo is foo what foo ever foo'

## Using group references
print(re.sub(r"t([0-9])([0-9])", r"t\2\1", "t13 t19 t81 t25"))
# Out: 't31 t91 t18 t52'

## Using a replacement function
items = ["zero", "one", "two"]
print(re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))],
             "Items: a[0], a[1], something, a[2]"))
# Out: 'Items: zero, one, something, two'

print('-----------------------------------')

"""
SPLITTING A STRING

re.split(pattern, string, maxsplit=0, flags=0) - Split the source string by
the occurrences of the pattern, returning a list containing the resulting
substrings.
"""

data = re.split(r'\s+', 'James 94 Samantha 417 Scarlett 74')
print( data )
# Output: ['James', '94', 'Samantha', '417', 'Scarlett', '74']

print('-----------------------------------')

"""
GROUPING

Grouping is done with parentheses. Calling group() returns a string formed
of the matching parenthesized subgroups.
"""

match = re.search(r"^123", "123zzb")
print(match.group())    # Group without argument returns the entire match found
# '123'

print(match.group(0))   # Specifying 0 gives the same result as specifying no argument
# Out: '123'

""" Calling groups() returns a list of tuples containing the subgroups. """

sentence = "This is a phone number 672-123-456-9910"
pattern = r".*(phone).*?([\d-]+)"

match = re.match(pattern, sentence)

print(match.groups())  # The entire match as a list of tuples of the paranthesized subgroups
# Out: ('phone', '672-123-456-9910')

print(match.group())       # The entire match as a string
# Out: 'This is a phone number 672-123-456-9910'

print(match.group(0))      # The entire match as a string
# Out: 'This is a phone number 672-123-456-9910'

print(match.group(1))      # The first parenthesized subgroup.
# Out: 'phone'

print(match.group(2))      # The second parenthesized subgroup.
# Out: '672-123-456-9910'

print(match.group(1, 2))   # Multiple arguments give us a tuple.
# Out: ('phone', '672-123-456-9910')

print('-----------------------------------')

"""
ESCAPING SPECIAL CHARACTERS

Special characters (like the character class brackets [ and ] below) are
not matched literally.
"""

match = re.search(r'[b]', 'a[b]c')
print(match.group())
# Out: 'b'

""" By escaping the special characters, they can be matched literally """
match = re.search(r'\[b\]', 'a[b]c')
print(match.group())
# Out: '[b]'

""" The re.escape() function can be used to do this for you """

print(re.escape('a[b]c'))
# Out: 'a\\[b\\]c'

match = re.search(re.escape('a[b]c'), 'a[b]c')
print(match.group())
# Out: 'a[b]c'

""" The re.escape() function escapes all special characters, so it is useful
if you are composing a regular expression based on user input 
"""
username = 'A.C.' # suppose this came from the user
print(re.findall(r'Hi {}!'.format(username), 'Hi A.C.! Hi ABCD!'))
# Out: ['Hi A.C.!', 'Hi ABCD!']

print(re.findall(r'Hi {}!'.format(re.escape(username)), 'Hi A.C.! Hi ABCD!'))
# Out: ['Hi A.C.!']