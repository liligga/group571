class Animal:
    def speak(self):
        print('Animal is speaking')

class Dog(Animal):
    def speak(self):
        super().speak()
        print('Гав гав')

class Cat(Animal):
    def speak(self):
        super().speak()
        print('Мяу мяу')

class CatDog(Cat, Dog):
    def speak(self):
        super().speak()
        print('мяу гав')

kotopes = CatDog()
kotopes.speak()
print(CatDog.mro()) # method resolution order

cat_1 = Cat()
cat_1.speak()
print(Cat.mro())