#Parent class
class Dog:
    #Class attribute
    species = 'mammal'


    #Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    