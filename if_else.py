# Conditional statements allow us to perform different calculations or actions based on conditions.

# If statements:
# An if statement will run the indented block of code if the condition evaluates to True.
# == is the comparison operator, which checks if two values are equal. For example:
if 1 + 1 == 2:
    print("1 + 1 is 2!")

# If-else statements:
# An if-else statement runs the code in the if block if the condition is True,
# otherwise, it runs the code in the else block.
# Try running the code below. Then update `favAnimal` to another animal and run it again!
favAnimal = "cat"
if favAnimal == "cat":
    print("I love cats too!")
else:
    print(favAnimal + " is also a good animal!")

# If-elif-else statements:
# These allow you to check multiple conditions.
weather = "sunny"
if weather == "raining":
    print("Bring an umbrella!")
elif weather == "snow":
    print("Bring a snow jacket; it's cold!")
else:
    print("Put on shorts and a T-shirt!")

# Bringing it all together:
tides = [
    {"location": "Seattle, WA", "date": "2025-01-22", "time": "6:30 AM", "tide": "High", "height": 11.2},
    {"location": "Seattle, WA", "date": "2025-01-22", "time": "12:45 PM", "tide": "Low", "height": 1.8},
    {"location": "Seattle, WA", "date": "2025-01-22", "time": "6:50 PM", "tide": "High", "height": 10.5},
    {"location": "Seattle, WA", "date": "2025-01-23", "time": "1:15 AM", "tide": "Low", "height": 2.3},
]

# Initialize variables to store the total heights for high and low tides
highTide = 0
lowTide = 0
highTideCount = 0
lowTideCount = 0

# Iterate through the tides list to calculate the total height for high and low tides
for tideData in tides:
    if tideData["tide"] == "High":
        highTide += tideData["height"]
        highTideCount += 1
    elif tideData["tide"] == "Low":
        lowTide += tideData["height"]
        lowTideCount += 1

# Calculate the average heights for high and low tides
highTideAverage = highTide / highTideCount
lowTideAverage = lowTide / lowTideCount

# Print the results using concatenation
print("High Tide Average: " + str(round(highTideAverage, 2)) + " ft")
print("Low Tide Average: " + str(round(lowTideAverage, 2)) + " ft")

# Exercise
# Gather the dictionaries for each of your group members into a list.
# Loop through the list and perform a conditional statement on each element.
# For example, you can check if any group members have similar hobbies
# or find the oldest or youngest member in the group.