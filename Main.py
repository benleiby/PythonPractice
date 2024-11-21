import math

# Question 1: Defining Functions (10 points)
# Write a Python function multiply_and_add that takes three arguments: two integers a and b, and
# a string op. The function should:
# Return the product of a and b if op is "multiply".
# Return the sum of a and b if op is "add".
# Raise a ValueError if op is anything else.

def multiply_and_add(a, b, op):

    if op == "multiply":
        return a * b
    elif op == "add":
        return a + b
    else:
        raise ValueError()

# Test

print(multiply_and_add(10, 5, "multiply"))
print(multiply_and_add(10, 5, "add"))

# Question 2: Conditional Statements (10 points)
# Write a Python function grade_category that takes an integer score (0-100) as input and returns a
# string representing the grade category:

# "A" for scores 90 and above,
# "B" for scores 80-89,
# "C" for scores 70-79,
# "D" for scores 60-69,
# "F" for scores below 60.
# If the input score is not in the range 0-100, raise a ValueError.

def grade_category(score):

    if score > 100 or score < 0:
        raise ValueError
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 60:
        return "F"

# Test

for x in range(101):
    print("Score: " + str(x) + " |Grade: " + grade_category(x))

# Question 3: Loops (10 points)
# Write a Python function reverse_string that takes a string s as input and returns the reversed
# version of the string using a for loop. Do not use Python's slicing capabilities ([::-1]).

def reverse_string(s):

    rev = list()

    for i in range(len(s)):
        rev.append(s[len(s) - i - 1])

    return "".join(rev)

# Test

print(reverse_string("this is crazy"))

# Question 4: Lists and List Comprehensions (10 points)
# Write a Python expression (not a function) using a list comprehension that generates a list of squares
# of all even numbers between 1 and 20 (inclusive).

result = [math.pow(x, 2) for x in range(1, 20)]
print(result)

# Question 5: Dictionaries (10 points)
# Write a Python function word_count that takes a string s and returns a dictionary where the keys
# are words in s and the values are the number of times each word appears. Assume words are
# separated by spaces, and the function should be case-insensitive.



