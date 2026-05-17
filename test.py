class Dog:
    def __init__ (self, name):
        self.name = name
    def bark (self):
        print(self.name + " says Woof woof!")

dog = Dog("Jason")
dog.bark()