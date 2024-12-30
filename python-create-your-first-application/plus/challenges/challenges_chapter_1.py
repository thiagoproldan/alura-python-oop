"""
The `print()` function plays a fundamental role in printing text and variables to the console or another output location.
Throughout the different versions of Python, the syntax and features of this function have evolved, offering various ways to format and display messages.
To practice this function, we have created a list of activities (optional) focused on practice to further enhance your learning experience.
Let's practice!
"""

# Exercises

# 1 - Print the sentence: "Python at Alura's Programming School".
print("Python at Alura's Programming School")

# 2 - Print the sentence: "My name is {name} and I am {age} years old", where name and age need to be values stored in variables.
name = "Thiago"
age = 25

# Various ways to print the sentence
print("My name is", name, "and I am", age, "years old.")  # Concatenating
print(f"My name is {name} and I am {age} years old.")  # f-string
print("My name is {} and I am {} years old.".format(name, age))  # Format without indexes
print("My name is {0} and I am {1} years old.".format(name, age))  # Format with indexes
print("My name is %s and I am %d years old." % (name, age))  # %s and %d
print("My name is %s and I am %i years old." % (name, age))  # %s and %i

# 3 - Print the word: 'ALURA' so that each letter is on a new line, as shown below:
# A
# L
# U
# R
# A

# Different ways to achieve the output
print("A\nL\nU\nR\nA")  # Using \n
print("""
A
L
U
R
A
""")  # Using triple quotes

print("A")  # Using multiple print statements
print("L")
print("U")
print("R")
print("A")

print('A', 'L', 'U', 'R', 'A', sep='\n')  # Using sep

# 4 - Print the sentence: The rounded value of pi is: {rounded_pi}, where the value of pi needs to be stored in a variable and rounded to only two decimal places.
pi = 3.14159

# Various ways to round and print the value of pi
print(f"The rounded value of pi is: {pi:.2f}")  # f-string
print("The rounded value of pi is: {:.2f}".format(pi))  # Format with indexes
print("The rounded value of pi is: %.2f" % pi)  # %f
print("The rounded value of pi is: {0:.2f}".format(pi))  # Format without indexes
print("The rounded value of pi is:", round(pi, 2))  # Using round
