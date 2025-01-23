# Data Types
# In Python, we have different ways to categorize data, called "data types."
# Let’s go over a few of the most common ones!

## Primitive Data Types

# Integer
# These are just whole numbers, like the ones you’d count with.
1
42

# Float
# If a number has a decimal point, it’s a float. Think of things like prices or measurements.
0.99
3.14

# Boolean
# This is a fancy way of saying True or False. It’s super useful for making decisions in your code.
True
False

# String
# Strings are just text! You can put them in single or double quotes—it’s your choice.
"Hello World"
'python'

## Non-Primitive Data Types
# Now we’re getting into the cool stuff! These data types can hold multiple pieces of data.

# Lists
# A list is like a container where you can keep things in order. You can mix and match data types, too.
[1, 2, 3, 4]
["a", True, 10.01]

# Dictionaries
# A dictionary is another container, but instead of just a list of items, it pairs things together.
# For example, you can use it to store information about a character, like their name, species, and age.
{
    "name": "Bilbo Baggins",
    "species": "Hobbit",
    "home": "Bag End, Hobbiton",
    "story": "The Hobbit and The Lord of the Rings",
    "age": 131
}

## Variables
# Think of variables as little boxes where you can store data for later.
# The name of the variable should describe what’s inside to keep things clear.

# Here’s an example:
name = "Bilbo Baggins"  # This variable holds a name, so we called it "name."

# You can also store more complex data, like this dictionary full of Gandalf’s info:
character_info = {
    "name": "Gandalf the Gray",
    "species": "Maia",
    "home": "Valinor (originally), often found wandering Middle-earth",
    "story": "The Hobbit and The Lord of the Rings",
    "age": "Over 10,000 years (timeless being)"
}

#Exercise:
#Make a list containing your favorite movies
# Make a dictionary with the keys name, degree_program, favorite_book and give each key values.


# Accessing and manipulating variables
greeting = "Hello world"  # Here, we’re creating a variable called 'greeting' and setting it to "Hello world."
print(greeting)  # This prints the current value of 'greeting' to the console.

# Now, let’s change the value of 'greeting.'
greeting = "Hi!"
print(greeting)  # When we print it again, we’ll see the updated value.

# How to run this code:
# You can click the green play button in the top left corner of your Python editor to run it.

# What does the print function do?
# The `print` function is built into Python. It takes whatever you give it and displays it in the console.

# How does this work step by step?
# Python runs your script line by line from top to bottom.
# 1. First, we set 'greeting' to "Hello world" and print it.
# 2. Then, we change 'greeting' to "Hi!" and print it again.
# By running the code, you can see how the value of the variable changes in real-time.

# Accessing and updating values in lists
tolkien_books = [
    "The Hobbit",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King",
    "The Silmarillion",
]

# Accessing values in a list
# To get a value from a list, use its position (index) along with the variable name.
# Remember, Python lists start counting from 0!
print(tolkien_books[0])  # This prints the first book, "The Hobbit"
print(tolkien_books[2])  # This prints the third book, "The Two Towers"

# Run the code to see what prints to the console!

# Updating a value in the list
# To change a value, access it by its position and assign it a new value.
tolkien_books[4] = "The Fall of Gondolin"  # Replacing "The Silmarillion" with "The Fall of Gondolin"
print(tolkien_books)  # Let's see how the list looks now!

# Adding new items to the end of the list
# You can use the .append() method to add an item to the end of the list.
tolkien_books.append("The Silmarillion")  # Adding "The Silmarillion" back to the list
print(tolkien_books)  # Check out the updated list!
# Getting the length of a list
# If you want to know how many items are in a list, you can use the len() function.
print(len(tolkien_books))  # This prints the number of books in the 'tolkien_books' list.

# More information on Python lists:
# Intro: https://www.w3schools.com/python/python_lists.asp
# Access: https://www.w3schools.com/python/python_lists_access.asp
# Updating: https://www.w3schools.com/python/python_lists_change.asp
# Add: https://www.w3schools.com/python/python_lists_add.asp
# Remove: https://www.w3schools.com/python/python_lists_remove.asp

# Working with dictionaries
# Accessing elements in a dictionary using their keys
character_info_two = {
    "name": "Frodo Baggins",
    "species": "Hobbit",
    "home": "Bag End, Hobbiton",
    "story": "The Lord of the Rings",
    "age": 50
}

# Accessing specific values using keys
print(character_info_two["name"])  # Prints Frodo's name
print(character_info_two["home"])  # Prints Frodo's home

# Updating values in a dictionary
character_info_two["age"] = 53  # Updates Frodo's age to reflect his age at the end of the series
print(character_info_two)  # Run the code to see the updated dictionary

# Adding a new key-value pair to the dictionary
# You can add a new key by specifying the key name and assigning it a value.
character_info_two["role"] = "Ring-bearer"
print(character_info_two)  # Run the code to see the updated dictionary with the new key-value pair

# More information on Python dictionaries:
# Intro: https://www.w3schools.com/python/python_dictionaries.asp
# Access: https://www.w3schools.com/python/python_dictionaries_access.asp
# Updating: https://www.w3schools.com/python/python_dictionaries_change.asp
# Add: https://www.w3schools.com/python/python_dictionaries_add.asp
# Remove: https://www.w3schools.com/python/python_dictionaries_remove.asp

#Exersise
# Part 1: Lists
# Create a list of your favorite hobbies.
# Access and print the first and third items in your list.
# Add a new hobby to the end of the list.
# Replace the second item in your list with another hobby.
# Print the updated list and its length.
# Part 2: Dictionaries
# Create a dictionary about yourself with the following keys:
# name
# age
# favorite_color
# hobbies (use the list you created in Part 1 as the value for this key)
# Access and print the value associated with the favorite_color key.
# Update your age key with a new value.
# Add a new key-value pair for favorite_food and assign it a value.
# Print the updated dictionary.