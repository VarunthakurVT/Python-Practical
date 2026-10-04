# Magic Methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
print(p1)


# Inheritance 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal):
    pass

d1 = Dog("Rex")
d1.speak()

# Polymorphism 

class Cat:
    def sound(self):
        print("Meow")

class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")

c1 = Cat()
f1 = Fox()

c1.sound()
f1.sound()

# Encapsulation
class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

s1 = ScoreBoard(0)
print(s1.get_score())

