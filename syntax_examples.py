# Importing modules
import math
import random
import sys
import pandas as pd

from matplotlib.lines import Line2D

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
from   plotnine import *

wells_oi = mask_SAdata[(mask_SAdata['Target'] == target) & (mask_SAdata['Molecule Name'] == molecule)]['well'].unique()

myCol = ["#1F77B4FF", "#FF7F0EFF", "#2CA02CFF", "#D62728FF", 
         "#9467BDFF", "#8C564BFF", "#E377C2FF", "#7F7F7FFF", 
         "#BCBD22FF", "#17BECFFF", "#AEC7E8FF", "#FFBB78FF", 
         "#98DF8AFF", "#FF9896FF", "#C5B0D5FF", "#C49C94FF", 
         "#F7B6D2FF", "#C7C7C7FF", "#DBDB8DFF", "#9EDAE5FF"]

style = theme(text             = element_text(family = "Droid Sans", size = 10),
              title            = element_text(size = 18, face = "bold"),
              axis_title       = element_text(size = 10, face = "bold"),
              legend_title     = element_text(size = 12, face = "bold"),
              legend_key       = element_rect(fill  = 'white'),
              axis_text        = element_text(color = 'grey'),
              axis_ticks_major = element_line(color = 'grey'),
              panel_grid_major = element_blank(),
              panel_grid_minor = element_blank(), 
              panel_background = element_rect(fill = "White", color = "Green", size = 20),
              panel_border     = element_rect(fill = "White", color = "grey", size = 1),
              strip_background = element_blank()
              )


# Defining a function
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")


print(f"\n Targets found on this plate:")
print(mask_SAdata['Target'].unique())


# Conditional statements
if __name__ == "__main__":
    # Variables
    message = "Hello, World!"
    age = 25
    is_student = True

    # Basic input and output
    print(message)
    name = input("Enter your name: ")
    greet(name = name)

    # Control structures
    if age < 18:
        print("You are a minor.")
    elif age >= 18 and age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

    # Loops
    for i in range(5):
        print(f"Count: {i}")

    while is_student:
        print("You are a student.")
        break

    # Lists and loops
    colors = ["red", "green", "blue"]
    for color in colors:
        print(f"Color: {color}")

    # Dictionaries
    student = {"name": "Alice", "age": 20, "grade": "A"}
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    # Functions with default arguments
    def add(x, y = 10):
        return x + y

    result = add(5)
    print(f"Result: {result}")

    # Exception handling
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    finally:
        print("Cleanup")

    # Classes and objects
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

    person1 = Person("Bob", 30)
    person1.greet()

    # File I/O
    with open("sample.txt", "w") as file:
        file.write("This is a sample file.")

    with open("sample.txt", "r") as file:
        content = file.read()
        print(f"File Content: {content}")

    # Math and random module usage
    print(f"Square root of 25: {math.sqrt(25)}")
    print(f"Random number between 1 and 10: {random.randint(1, 10)}")

# Exiting the program
sys.exit(0)
