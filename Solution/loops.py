# Loops allow us to repeat the same code again and again.
tides = [
    {"location": "Seattle, WA", "date": "2025-01-22", "time": "6:30 AM", "tide": "High", "height": 11.2},
    {"location": "Seattle, WA", "date": "2025-01-22", "time": "12:45 PM", "tide": "Low", "height": 1.8},
    {"location": "Seattle, WA", "date": "2025-01-22", "time": "6:50 PM", "tide": "High", "height": 10.5},
    {"location": "Seattle, WA", "date": "2025-01-23", "time": "1:15 AM", "tide": "Low", "height": 2.3},
]

# In the code below, we are going to calculate the average tide height from the list above.

# This variable stores the sum of the tide heights.
total_tide_height = 0

# This loop runs once for every item in the tides list (4 times in this case).
# During each loop, the current item is stored in the `tideData` variable.
for tideData in tides:
    # Add the current tide height to the running total.
    total_tide_height += tideData["height"]
    # Print the current sum of tide heights.
    print(f"Tide Height Sum: {total_tide_height}")

# Here, we calculate the average tide height by dividing the total height by the number of items in the list.
# Average = sum / number of elements.
average_tide_height = total_tide_height / len(tides)

# Print the average tide height.
# The str will convert our float number to a string so we can print it
print(f"Average Tide Height: " + str(average_tide_height))

# Exercise
# Given the list below, use a loop to find the total average grade for the class and convert it to a percentage.
# The answer should be 78.40%
# Explore these Python arithmetic operators to learn how to perform the calculations needed for this exercise.
# https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp
grades = [0.78, 0.88, 0.40, 0.87, 0.99]

# Initialize a variable to store the total sum of grades


# Loop through each grade in the list and calculate the total

# Calculate the average grade


# Convert the average to a percentage


# Print the average grade as a percentage
