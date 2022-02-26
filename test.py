print(1)
class Animal:
    def __init__(self, name, sound):
        print(2)
        self.name = name
        self.sound = sound
        print(3)
    def hello(self):
        print(4)
        print(self.name, self.sound)
        print(5)

print(6)
dog = Animal('dog', 'bark')
print(7)
dog.hello()
print(dog)
import pygame