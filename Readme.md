# Introduction to Python

Welcome to the first of two Python workshops for ArcGIS! This workshop focuses on the fundamentals of the Python programming language, laying a solid foundation for writing scripts in the second workshop, which will focus on ArcGIS-specific applications.

## Learning Outcomes
- Create a Python script.
- Understand and use Python's primitive data types (e.g., integers, strings, and floats).
- Work with more complex data structures like lists and dictionaries to store and organize data.
- Use variables effectively to store and manage data.
- Perform analysis and calculations on data using python.

## Schedule

| Estimated Time | Activity                |
|----------------|-------------------------|
| 15 minutes     | Intro and Getting Set Up|
| 30 minutes     | Data Types              |
| 20 minutes     | Exercise                |
| 15 minutes     | Break                   |
| 30 minutes     | Loops                   |
| 20 minutes     | Exercise                |
| 30 minutes     | If-Else Statements      |
| 20 minutes     | Exercise                |
| 15 minutes     | Break                   |
| 75 minutes     | Project                 |
| 30 minutes     | Presentations           |
| -              | End                     |

## 



### Environment Setup
1. **Download Python**: Install the latest version of Python from [python.org](https://www.python.org/).
2. **Download PyCharm**: Get PyCharm (Community Edition) from [jetbrains.com](https://www.jetbrains.com/pycharm/).
3. **Pull Starter Code from GitHub**: Clone the repository with the starter code using GitHub. [Clone down code](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#clone-repo)

## What is a Script?

A script is a sequence of instructions written in a programming language, like Python, designed to perform a specific task. Unlike an application, which is a complex software program with various features, a script typically focuses on automating a particular process or solving a single problem.

For example, in this workshop, you will learn how to write scripts to manipulate data, perform calculations, and build simple tools that can enhance workflows in ArcGIS.

## What is Python
Python is an open-source programming language, first released in 1991, that is used in a variety of industries and tasks, including data analytics, web development, machine learning, artificial intelligence, and scripting.

Compared to other programming languages, Python is often considered beginner-friendly and highly readable. With just a little Python knowledge, you can start writing scripts to automate tasks for your project. 

## Readable code 
Before even hopping into writing python let's see if you can parse, what it's doing just by reading it. 

``` 
# Q1: What do you think this `import csv` statement is doing?
import csv 

# `read_tide_data` is a function. It's a set of contained Python instructions that can be run and reused over and over again. Everything indented under the function is considered "inside" of the function or "in scope"

# Q2: What do you think the `read_tide_data` function is doing?
def read_tide_data(filename):
    
    with open(filename, 'r') as file:  
        #This reader is giving us access to read the file. It is essentially putting all of the data from the csv into reader.       
        reader = csv.reader(file)
        next(reader)

        tide_data = []
        
        # Q3: What do you think this block of code is doing?
        # Try reading it as "for every row in reader"
        for row in reader:
     
            date = row[0]  
            time = row[1]  
            tide_level = float(row[2])  
            
            # Q4: What is going on here?
            tide_data.append({
                'date': date,
                'time': time,
                'tide_level': tide_level
            })

    return tide_data


filename = 'tide_data.csv'
tide_data = read_tide_data(filename)

# Q5: What do you think this block of code is doing?
# It's very similar to the code we saw earlier in `for row in reader:`
for entry in tide_data:
    print(f"Date: {entry['date']}, Time: {entry['time']}, Tide Level: {entry['tide_level']} meters")
``` 

<details>
  <summary>Answers</summary>

1. This is an import statement that gives us access to Python's built-in csv module, which helps us work with CSV files.    

2. The read_tide_data function allows us to programmatically open and extract data from the CSV file. While the csv module provides the tools to read the file, the function is responsible for "reading" the tide data, parsing it, and giving us access to the data in a structured way.     

3. This block of code is called a loop. Similar to the function, everything indented under the loop is considered inside it. The loop runs the indented code a specific number of times. In this case, it runs once for every row in reader. For example, if there are 10 rows of data, the loop will run 10 times; if there are 100 rows, it will run 100 times.    

4. This part is a little tricky. The reader object is not very user-friendly to work with directly, so we break it into smaller, manageable pieces. The variable row acts as a container, holding one row of data at a time from reader. We then extract individual values from the row—date, time, and tide_level—and organize them into a data structure called a "dictionary." The dictionary uses keys ('date', 'time', 'tide_level') to make the data easier to access and use later.     

5. This is another loop. The variable tide_data contains the parsed data from the CSV file, and this loop prints each row to the console.     
</details>

## Read and complete the exercises in the files listed below
1. data_types.py
2. loops.py
3. if_else.py
4. project.py 
