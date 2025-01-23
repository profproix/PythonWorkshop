import csv

# Download a CSV file from https://catalog.data.gov/dataset/
# Move the CSV file to the project directory. The file should be on the same level as the Python files.

def read_data(filename):
    with open(filename, 'r') as file:
        # Create a CSV reader to read the file. This essentially loads all the data from the CSV into the reader.
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        data = []  # Initialize an empty list to store the data

        for row in reader:
            # For each row, create a variable for each column and assign the data by index in the order of its appearance
            # Example: date = row[0]

            # Add a key-value pair for each column and assign the value to the variable you created above
            data.append({
                # Example: 'date': date
            })

    return data


# Call the function and pass the name of the CSV file
data = read_data("Enter csv file name here")
print(data)
# Your data should now be saved as dictionaries within a list.
# Check that the data prints correctly to the console. If it does not, reach out for help.
# Once your data is properly formatted, use the skills you learned in this lesson to perform calculations on your data.
# You can refer to Python arithmetic operators here: https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp
# If you are more advanced, consider using a Python library for more complex calculations: https://www.geeksforgeeks.org/data-analysis-with-python/
# Be prepared to share your code and calculations. Your results should print to the console.