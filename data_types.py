import math

# ------------------------
# Data Types
# ------------------------

# In Python, we have different ways to categorize data, called "data types."
# Let’s go over a few of the most common ones!

## Primitive Data Types

# Integer - Whole numbers
1
42

# Float - Numbers with decimals (e.g., prices, measurements)
0.99
3.14

# Boolean - Represents True or False values
True
False

# String - Text, enclosed in single or double quotes
"Hello World"
'python'

# ------------------------
# Statements and Variables
# ------------------------

# Statements are lines of code that perform an action, such as assigning a variable.

# Variables store data for later use.
greeting = "Hello world"  # Creating a variable 'greeting' and assigning a value.

# The `print` function displays output in the console.
print(greeting)  # Output: "Hello world"

# Updating the variable
greeting = "Hi!"
print(greeting)  # Output: "Hi!"

# ------------------------
# String Functions
# ------------------------

name = "rose"
print(name.upper())      # Output: "ROSE"
print(name.lower())      # Output: "rose"
print(name.title())      # Output: "Rose"
print(name.capitalize()) # Output: "Rose"

# ------------------------
# Expressions and Arithmetic Operators
# ------------------------

# Expressions evaluate to a value
print(1 + 1)  # Output: 2

# Using variables in expressions
num1 = 100
num2 = 2000
sum_result = num1 + num2
print(sum_result)  # Output: 2100

# Subtraction
difference = 100 - 10

# Multiplication
tax = 0.10
price = 75
total_price = tax * price

# Division
number_of_people = 4
cost_per_person = total_price / number_of_people

# Modulus (remainder operator)
is_even = 10 % 2  # 0 means even

# Exponents
exponent_result = 5 ** 5

# ------------------------
# Basic Math Functions
# ------------------------

print(abs(709.90 * 2343.845027834))
print(pow(3, 2))  # Same as 3 ** 2
print(round(0.23450943875, 4))

score1 = 324 + 2345.656 + 43543.453 + 34543.34
score2 = 7355 + 346.346 + 934543.834

print(max(score1, score2))  # Larger value
print(min(score1, score2))  # Smaller value

# Using the math module
print(math.sqrt(25))       # Square root
print(math.ceil(45.32453)) # Round up
print(math.floor(563.756)) # Round down

# ------------------------
# Non-Primitive Data Types
# ------------------------

# Lists - Ordered collection of items
num_list = [1, 2, 3, 4]
random_list = ["a", True, 10.01]

# Dictionaries - Key-value pairs
bilbo = {
    "name": "Bilbo Baggins",
    "species": "Hobbit",
    "home": "Bag End, Hobbiton",
    "story": "The Hobbit and The Lord of the Rings",
    "age": 131
}

# ------------------------
# Accessing and Updating Lists
# ------------------------

tolkien_books = [
    "The Hobbit",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King",
    "The Silmarillion"
]

# Accessing values using index
print(tolkien_books[0])  # Output: "The Hobbit"
print(tolkien_books[2])  # Output: "The Two Towers"

# Updating values
tolkien_books[4] = "The Fall of Gondolin"
print(tolkien_books)

# Adding items
tolkien_books.append("The Silmarillion")
print(tolkien_books)

# Getting the length of the list
print(len(tolkien_books))

# ------------------------
# Working with Dictionaries
# ------------------------

character_info_two = {
    "name": "Frodo Baggins",
    "species": "Hobbit",
    "home": "Bag End, Hobbiton",
    "story": "The Lord of the Rings",
    "age": 50
}

# Accessing values
print(character_info_two["name"])  # Output: "Frodo Baggins"
print(character_info_two["home"])  # Output: "Bag End, Hobbiton"

# Updating values
character_info_two["age"] = 53
print(character_info_two)

# Adding a new key-value pair
character_info_two["role"] = "Ring-bearer"
print(character_info_two)

# ------------------------
# Accessing Nested Values
# ------------------------

character_info_list = [
    {
        "name": "Frodo Baggins",
        "species": "Hobbit",
        "home": "Bag End, Hobbiton",
        "age": 50,
        "books": ["The Fellowship of the Ring", "The Two Towers", "The Return of the King"]
    },
    {
        "name": "Gandalf",
        "species": "Maia (Wizard)",
        "home": "Valinor (originally)",
        "age": "Over 10,000",
        "books": ["The Hobbit", "The Fellowship of the Ring", "The Two Towers", "The Return of the King"]
    }
]

# Accessing nested values
print(character_info_list[1]["name"])  # Output: "Gandalf"
print(character_info_list[1]["books"][0])  # Output: "The Hobbit"

# ------------------------
# Exercise 📝
# ------------------------

# Part 1: Lists
# 1. Create a list of your favorite hobbies.
# 2. Access and print the first and third items.
# 3. Add a new hobby to the list.
# 4. Replace the second item with another hobby.
# 5. Print the updated list and its length.

# Part 2: Dictionaries
# 1. Create a dictionary about yourself with:
#    - name
#    - age
#    - favorite_color
#    - hobbies (use the list from Part 1)
# 2. Access and print your favorite_color.
# 3. Update your age.
# 4. Add a new key-value pair for favorite_food.
# 5. Print the updated dictionary.
# 6. Access and print a specific hobby from the dictionary.

# ------------------------
# List and Dictionary Functions
# ------------------------

print(len(character_info_list))  # Returns the number of elements

# Correct way to append dictionaries to a list
character_info_list.append({
    "name": "Éowyn",
    "species": "Human (Rohirrim)",
    "home": "Rohan",
    "age": 24,
    "books": ["The Two Towers", "The Return of the King"]
})

num_list = [1, 2, 3, 4, 1, 3, 7, 1]
num_list.remove(3)  # Removes first occurrence of 3
print(num_list.count(1))  # Counts occurrences of 1

num_list.sort()  # Sorts the list in ascending order
print(num_list)

# Dictionary operations
gollum = {
    "name": "Gollum (Sméagol)",
    "species": "Hobbit (Stoor)",
    "home": "Gladden Fields",
    "age": "~589",
    "books": ["The Hobbit", "The Fellowship of the Ring", "The Two Towers", "The Return of the King"],
    "has_ring": False
}

print(len(gollum))
print(gollum.keys())
print(gollum.values())
print(gollum.items())
gollum.pop("has_ring")
print(gollum)
