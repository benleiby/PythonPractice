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

# Question 3: Loops (10 points)
# Write a Python function reverse_string that takes a string s as input and returns the reversed
# version of the string using a for loop. Do not use Python's slicing capabilities ([::-1]).

def reverse_string(s):

    rev = list()

    for i in range(len(s)):
        rev.append(s[len(s) - i - 1])

    return "".join(rev)

# Question 4: Lists and List Comprehensions (10 points)
# Write a Python expression (not a function) using a list comprehension that generates a list of squares
# of all even numbers between 1 and 20 (inclusive).

result = [math.pow(x, 2) for x in range(1, 20)]

# Question 5: Dictionaries (10 points)
# Write a Python function word_count that takes a string s and returns a dictionary where the keys
# are words in s and the values are the number of times each word appears. Assume words are
# separated by spaces, and the function should be case-insensitive.

def word_count(s):

    res = {}

    for word in s.split(" "):

        if not res.__contains__(word):
            res[word] = 1
        else:
            res[word] = res[word] + 1

    return res

# Question 6: Errors and Exceptions (10 points)
# Write a Python function safe_divide that takes two arguments a and b and returns the result of
# dividing a by b. If b is zero, return the string "Division by zero error".

def safe_divide(a, b):

    if b == 0:
        return "Division by zero error"

    return a / b

# Question 7: Python Syntax Exploration (Bonus - 5 points)
# Write a Python one-liner (using lambda functions, list comprehensions, or any other feature of
# Python syntax) that filters a list of integers to include only numbers that are divisible by both 3 and 5.

mylist = [5, 5, 5, 5]
filtered = filter(lambda x : x % 3 == 0 and x % 5 == 0, mylist)

# Advanced Problems:

# 1. Function with Nested Loops (10 points)
# Write a Python function find_pairs that takes a list of integers and an integer target as
# arguments. The function should return a list of tuples, where each tuple contains two distinct
# from the list that add up to the target value. Each pair should only appear once in the
# result (i.e., the pair (3, 7) and (7, 3) should not both appear). If no such pairs exist, return an empty
# list.

def find_pairs(nums, target):

    complements = [target - x for x in nums]
    pairs = []

    for i in range(len(complements)):
        if complements[i] in nums and complements.index(complements[i]) != i:
            pair = (min(complements[i], nums[i]), max(complements[i], nums[i]))
            if pair not in pairs:
                pairs.append(pair)

    return pairs




