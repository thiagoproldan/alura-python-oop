"""
1 - Create a list for each of the following pieces of information:

    - List of numbers from 1 to 10;
    - List with four names;
    - List with the year you were born and the current year.
"""

# Creating lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["João", "Maria", "José", "Ana"]
years = [1999, 2024]

# 2 - Create a list and use a for loop to iterate over all elements in the list.
for number in numbers:
    print(f"The number is {number}")

# 3 - Use a for loop to calculate the sum of odd numbers from 1 to 10.
odd_sum = 0
for number in numbers:
    if number % 2 != 0:  # If the number is odd
        odd_sum += number

print(f"The sum of the odd numbers is {odd_sum}")

# 4 - Use a for loop to print numbers from 1 to 10 in descending order.

# Using range with step
for number in range(10, 0, -1):
    print(number)

# Using reversed()
for number in reversed(range(1, 11)):
    print(number)

# Using sorted() with reverse=True
for number in sorted(numbers, reverse=True):
    print(number)

# Using slicing
for number in numbers[::-1]:
    print(number)

# 5 - Ask the user for a number and then use a for loop to print the multiplication table for that number, from 1 to 10.
multiplier = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{multiplier} x {i} = {multiplier * i}")

# 6 - Create a list of numbers and use a for loop to calculate the sum of all elements. Use a try-except block to handle possible exceptions.
numbers_with_error = [1, 2, 3, 4, "potato", 6, 7, 8, 9, 10] # Simulating an error

sum_total = 0
for number in numbers_with_error:
    try:
        sum_total += number
    except TypeError:
        print(f"The element '{number}' is not an integer.")

# 7 - Build a code that calculates the average of the values in a list. Use a try-except block to handle division by zero in case the list is empty.
values = [10, 20, 30, 40, 50]

try:
    average = sum(values) / len(values)  # sum() adds up all elements, len() returns the list size.
except ZeroDivisionError:
    print("The list is empty.")
except TypeError:
    print("The list contains elements that are not numbers.")
else:
    print(f"The average of the values is {average}")
finally:
    print("End of program.")