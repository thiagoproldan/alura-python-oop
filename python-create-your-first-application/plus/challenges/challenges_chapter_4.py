# Exercises

# 1 - Create a dictionary representing information about a person, such as name, age, and city.
person = {
    "name": "Thiago",
    "age": 25,
    "city": "São Paulo"
}

"""
2 - Using the dictionary created in item 1:

    - Modify the value of one of the items in the dictionary (e.g., update the person's age);
    - Add a profession field for this person;
    - Remove an item from the dictionary.
"""

# Updating dictionary values
person["age"] = 26
person["profession"] = "Data Scientist"
del person["city"]  # Removes the key and value
print(person)

# 3 - Create a dictionary showing numbers from 1 to 5 and their respective squares.
squares = {x: x ** 2 for x in range(1, 6)}

# 4 - Create a dictionary and check if a specific key exists within it.
dictionary = {
    "name": "Thiago",
    "age": 25,
    "city": "São Paulo"
}

if "name" in dictionary:
    print("The key 'name' exists in the dictionary.")
else:
    print("The key 'name' does not exist in the dictionary.")

# 5 - Write code that counts the frequency of each word in a sentence using a dictionary.
sentence = "Python is a powerful and easy-to-learn programming language."
word_count = {}
words = sentence.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
