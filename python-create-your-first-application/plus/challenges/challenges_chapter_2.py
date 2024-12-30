# Exercises

# 1 - Ask the user to enter a number and then use an if-else structure to determine if the number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

"""
2 - Ask the user their age and, based on that, use an if-elif-else structure to classify the age into categories according to the following conditions:

    - Child: 0 to 12 years;
    - Teenager: 13 to 18 years;
    - Adult: above 18 years.
"""

age = int(input("How old are you?"))
if age < 0:
    print("Invalid age")
elif 0 <= age <= 12:
    print("Child")
elif 13 <= age < 18:
    print("Teenager")
else:
    print("Adult")

# 3 - Ask for a username and password and use an if-else structure to verify if the provided username and password match the expected values set by you.
default_user = "admin"
default_password = "1234"

user = input("Enter username: ")
password = input("Enter password: ")

if user == default_user and password == default_password:
    print("Access granted")
else:
    print("Access denied")

"""
4 - Ask the user for the coordinates (x, y) of any point and use an if-elif-else structure to determine which quadrant of the Cartesian plane the point is located in, according to the following conditions:

    - First Quadrant: x and y values must be greater than zero;
    - Second Quadrant: x value is less than zero and y value is greater than zero;
    - Third Quadrant: x and y values must be less than zero;
    - Fourth Quadrant: x value is greater than zero and y value is less than zero;
    - Otherwise: the point is located on the axis or origin.
"""

x_coordinate = float(input("Enter the x coordinate: "))
y_coordinate = float(input("Enter the y coordinate: "))

if x_coordinate > 0 and y_coordinate > 0:
    print("First Quadrant")
elif x_coordinate < 0 and y_coordinate > 0:
    print("Second Quadrant")
elif x_coordinate < 0 and y_coordinate < 0:
    print("Third Quadrant")
elif x_coordinate > 0 and y_coordinate < 0:
    print("Fourth Quadrant")
else:
    print("The point is located on the axis or origin.")