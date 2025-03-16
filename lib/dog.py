#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed





#additional pracice:
#the __init__ magic method runs when an object is instantiated.
#To provide objects with unique attributes upon instantiation, we use the __init__ method.
#__init__ can also be modified to take more arguments. This allows us to customize the behavior of unique objects

# class Dog:

#     def __init__(self, name):
#         self.name = name
#         print(f"{name} is born!")
    
#     def bark(self):
#         print("Woof!")

#     def showing_self(self):
#         return self
    
    # fido is fido.showing_self()
    # True
    
    # Here we have a method that takes in two arguments, an instance of the Dog class and an owner's name.
    # def adopt(dog, owner_name):
    #     dog.owner = owner_name

    #Instead of writing a function that is not associated to any particular object and that takes in certain objects as arguments, we can simply teach our Dog instances how to get adopted.

    # we use the self keyword inside of the get_adopted() instance method to refer to whichever dog this method is being called on. We set that dog's owner equal to owner_name just as we would assign any other variable!

    # Think about it: if self refers to the object on which the method is being called, and if that object is an instance of the Dog class, then we can call any of our other instance methods on self.

#     def get_adopted(self, owner_name):
#         self.owner = owner_name

# fido = Dog("Fido")
# fido.name  

# snoopy = Dog("Snoopy")
# snoopy.name

# fido.breed = "Dalmation"
# snoopy.breed = "Beagle"

# fido.owner = "Sophie"

# adopt(fido, "Sophie")

# fido.showing_self()




