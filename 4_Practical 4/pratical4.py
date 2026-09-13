#Q1. Write a Python program to check if a player Lionel Messi has more than 10 achievements. If the condition is true, print the player's name, sport, and achievements 
# else print does not have more than 10 achievements.

dataset = [
    {"name": "Serena Williams", "sport": "Tennis", "achievements": 23},
    {"name": "Lionel Messi", "sport": "Soccer", "achievements": 7},
    {"name": "Michael Phelps", "sport": "Swimming", "achievements": 23},
    {"name": "Usain Bolt", "sport": "Athletics", "achievements": 8},
    {"name": "Roger Federer", "sport": "Tennis", "achievements": 20},
    {"name": "Cristiano Ronaldo", "sport": "Soccer", "achievements": 5}
]

for player in dataset:
    if player["name"] == "Lionel Messi":
        if player["achievements"] > 10:
            print(f"{player['name']}, {player['sport']}, {player['achievements']}")
        else:
            print(f"{player['name']} does not have more than 10 achievements")

##Q2. Write a Python program to check if a player belongs to the sport Tennis or has exactly 20 achievements. 
# If the condition is true, print a success message.

for player in dataset:
    if player["sport"] == "Tennis" or player["achievements"] == 20:
        print(f"Success! {player['name']} meets the criteria.")

#Q3. Write a Python program to check if a player has less than 10 achievements and does not play Soccer. 
# Print their details if they meet the criteria.
for player in dataset:
    if player["achievements"] < 10 and player["sport"] != "Soccer":
        print(f"{player['name']}, {player['sport']}, {player['achievements']}")

# Q4. Write a Python program in a Jupyter Notebook that takes an integer input (1 to 9999) from
#  the user and determines the following using branching statements:
# 1. If the number is even or odd.
# 2. If the number is a palindrome (reads the same forward and backward).
# 3. If the number is divisible by the sum of its digits.
num_str = input("Enter an integer (1 to 9999): ")
num = int(num_str)

if 1 <= num <= 9999:
    # 1. Even or Odd
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
        
    # 2. Palindrome
    if num_str == num_str[::-1]:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")
        
    # 3. Divisible by sum of digits
    digit_sum = sum(int(digit) for digit in num_str)
    if num % digit_sum == 0:
        print(f"{num} is divisible by the sum of its digits ({digit_sum})")
    else:
        print(f"{num} is not divisible by the sum of its digits ({digit_sum})")
else:
    print("Number out of range.")

#Q5. Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range(-5, 6):
    print(i)
# Q6. Write a for loop that prints out the following list:
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for square in squares:
    print(square)

#Q7. Write a while loop to copy the strings 'orange' of the list squares to the list new_squares.
#  Stop and exit the loop if the value on the list is not 'orange'
squares = ['orange', 'orange', 'purple', 'orange', 'blue'] 
new_squares = []
i = 0

while i < len(squares) and squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1

print(new_squares)

# Q8. The following is a list of animals in a National Zoo.
# Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]
# Your brother needs to write an essay on the animals whose names are made of 7 letters. 
# Help him find those animals through a while loop and create a separate list of such animals.
animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]
seven_letter_animals = []
i = 0

while i < len(animals):
    if len(animals[i]) == 7:
        seven_letter_animals.append(animals[i])
    i += 1

print(seven_letter_animals)