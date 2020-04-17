""" Example presenting all functions of class 'str' """

example = "thiS was a Rea8ly nice \n\tweekend, however& to LOO!"

print("original string = ", example)
print("str.capitalize() = ", example.capitalize())
print("str.casefold() = ", example.casefold())
print("str.count('a', 2, -1) = ", example.count('a', 2, -1))
print("str.find('w', 10) = ", example.find('w', 10))
print("str.format example = {0} is {1} in {2}".format("Herborn", 
	"city", "Germany"))
print("str.index('was') = ", example.index('was'))
print(" Pawel ".join("123"))
print("str.lower() = ", example.lower())
print("example of lstrip = ", '   spacious   '.lstrip())
print("example of lstrip = ", 'www.example.com'.lstrip('cmowz.'))

y = ​ "This is lazy\t\n"
print(y.strip()) ​ # Remove Whitespace: 'This is lazy'
print(​ "DrDre"​ .lower()) ​ # Lowercase: 'drdre'
print(​ "attention"​ .upper()) ​ # Uppercase: 'ATTENTION'
print(​ "smartphone"​ .startswith(​ "smart"​ )) ​ # True
print(​ "smartphone"​ .endswith(​ "phone"​ )) ​ # True
print(​ "another"​ .find(​ "other"​ )) ​ # Match index: 2
print(​ "cheat"​ .replace(​ "ch"​ , ​ "m"​ )) ​ # 'meat'
print(​ ','​ .join([​ "F"​ , ​ "B"​ , ​ "I"​ ])) ​ # 'F,B,I'
print(len(​ "Rumpelstiltskin"​ )) ​ # String length: 15
print(​ "ear"​ ​ in​ ​ "earth"​ ) ​ # Contains: True

intab = 'abc'
outtab = '123'
trantab = ''.maketrans(intab, outtab)
'alba is a cat'.translate(trantab)