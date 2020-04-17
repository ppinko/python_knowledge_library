"""
duck typing - this term comes from the saying:
“If it walks like a duck, and it quacks like a duck,
then it must be a duck.”

Duck typing is a concept related to dynamic typing, where
the type or the class of an object is less important than
the methods it defines. When you use duck typing, you do
not check types at all. Instead, you check for the presence
of a given method or attribute.
"""

class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide2 = Pycharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

print("------------")

lap1.code(ide2)
