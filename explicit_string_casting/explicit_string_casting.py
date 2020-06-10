"""
EXPLICIT STRING CASTING

b'foo bar' : results bytes in Python 3
'foo bar' : results str
r'foo bar' : results so called raw string, where escaping special characters is
not necessary, everything is taken verbatim as you typed
"""

normal_string = 'pawel \n loves \t coding'
print(normal_string)
##pawel 
## loves 	 coding

raw_string = r'pawel \n loves \t coding'
print(raw_string)
##pawel \n loves \t coding

