class Animal(object):
   def __init__(self, name: str, legs_number: int, is_scary: bool) -> None:
       self.is_scary = is_scary
       self.legs_number = legs_number
       self.name = name
 
class Mammal(Animal):
   def __init__(self, name: str, legs_number: int, is_scary: bool, walks_on_2_feet: bool = False) -> None:
       super().__init__(name=name, legs_number=legs_number, is_scary=is_scary)
       self.walks_on_2_feet = walks_on_2_feet
 
   def uses_all_legs_to_move(self) -> bool:
       if (self.legs_number == 2 and self.walks_on_2_feet) or (not self.walks_on_2_feet):
           return True
       elif self.legs_number > 2 and not self.walks_on_2_feet:
           return False
       else:
           raise AttributeError("Are you sure it's a mammal?")
 
class Insect(Animal):
   def __init__(self, name: str, legs_number: int) -> None:
       super().__init__(name=name, legs_number=legs_number, is_scary=True)
 
def check_how_scary(animal_object: Animal) -> str:
   if not animal_object.is_scary:
       return "Not scary at all"
   elif animal_object.is_scary and animal_object.legs_number < 4:
       return "A bit scary"
   else:
       return "Run for your lives! It's a demogorgon!"

spider = Insect('urszula', 4)
print(check_how_scary(spider))