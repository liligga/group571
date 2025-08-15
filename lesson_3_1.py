from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав гав")

puppy = Dog()
puppy.make_sound()
doggo = Dog()
doggo.make_sound()