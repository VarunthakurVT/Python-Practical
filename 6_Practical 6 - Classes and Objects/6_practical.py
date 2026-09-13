
# Q1 ans-

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def Display(self):
        print(f"{self.name}, {self.id}")

class Emp(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
    
    def Print(self):
        print("Emp class called")

emp_details = Emp("Mayank", 103)
emp_details.Display()
print("fix using super() to call parent class __init__")
print()




# Q2 ans-

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"

if is_anagram(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams")
else:
    print(f"'{str1}' and '{str2}' are not anagrams")

str3 = "hello"
str4 = "world"

if is_anagram(str3, str4):
    print(f"'{str3}' and '{str4}' are anagrams")
else:
    print(f"'{str3}' and '{str4}' are not anagrams")

print()




# Q3 ans-

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == num

test_numbers = [153, 370, 9474, 123, 1634, 8208]

for num in test_numbers:
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

print()



# Q4 ans-
class Vehicle:
    color = "white"
    
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = 0
    
    def assign_seating_capacity(self, capacity):
        self.seating_capacity = capacity
    
    def display(self):
        print(f"Max Speed: {self.max_speed} kmph")
        print(f"Mileage: {self.mileage} kmpl")
        print(f"Color: {self.color}")
        print(f"Seating Capacity: {self.seating_capacity}")

print("\nTask-1,2,3,4: Vehicle class with attributes and methods")
print("-" * 80)

car1 = Vehicle(200, 20)
car1.assign_seating_capacity(5)

car2 = Vehicle(180, 25)
car2.assign_seating_capacity(4)

print("\nCar 1 Details:")
car1.display()

print("\nCar 2 Details:")
car2.display()
print("\nTask-5: Two Vehicle objects created with specified properties")
print("-" * 80)
print("Car 1: Max Speed = 200 kmph, Mileage = 20 kmpl, Seating = 5")
print("Car 2: Max Speed = 180 kmph, Mileage = 25 kmpl, Seating = 4")

