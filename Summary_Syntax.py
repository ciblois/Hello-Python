# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:10:44 2020

@author: Cinthya
"""


#Codecademy - Python Syntax

print("A print statement is the easiest way to get your Python program to communicate with you. Being able to command this communication will be one of the most valuable tools in your programming toolbox.")
print("________________________________________________________________")

print("Text in Python is considered a specific type of data called a string. A string, so named because they’re a series of letters, numbers, or symbols connected in order — as if threaded together by string. Example:")
print ("This is " + "a good string")

print("________________________________________________________________")

print("As we get more familiar with the Python programming language, we run into errors and exceptions. These are complaints that Python makes when it doesn’t understand what you want it to do. Everyone runs into these issues, so it is a good habit to read and understand them. Here are some common errors that we might run into when printing strings:")
print ("Mismatched quotes will cause a SyntaxError")
print ("Without quotes will cause a NameError")

print("________________________________________________________________")

print("Python uses variables to define things that are subject to change.")
print("int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)")
print("float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)")
print("str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals")

print("________________________________________________________________")

print("One thing computers are capable of doing exceptionally well is performing arithmetic. Examples:")
mirthful_addition = 12381 + 91817
amazing_subtraction = 981 - 312
trippy_multiplication = 38 * 902
happy_division = 540 / 45
sassy_combinations = 129 * 1345 + 120 / 6 - 12
print("mirthful_addition = 12381 + 91817")
print("amazing_subtraction = 981 - 312")
print("trippy_multiplication = 38 * 902")
print("happy_division = 540 / 45")
print("sassy_combinations = 129 * 1345 + 120 / 6 - 12")
print("Answers:")
print(mirthful_addition, amazing_subtraction, trippy_multiplication, happy_division, sassy_combinations)
print("Combinations of arithmetical operators follow the usual order of operations.")
sassy_combinations2 = 129 * ((1345 + 120) / 6) - 12
print("sassy_combinations = 129 * 1345 + 120 / 6 - 12")
print("sassy_combinations2 = 129 * ((1345 + 120) / 6) - 12")
print("Difference:")
print(sassy_combinations, sassy_combinations2)

print("Python also offers a companion to division called the modulo operator. The modulo operator is indicated by % and returns the remainder after division is performed.")
is_this_number_odd = 15 % 2
is_this_number_divisible_by_seven = 133 % 7
print("is_this_number_odd = 15 % 2")
print(is_this_number_odd)
print("is_this_number_divisible_by_seven = 133 % 7")
print(is_this_number_divisible_by_seven)
print("Changing the contents of a variable is one of the essential operations. As the flow of a program progresses, data should be updated to reflect changes that have happened.")

print("________________________________________________________________")

print ("Sometimes we have a need for variables that are either true or false. This datatype, which can only ever take one of two values, is called a boolean. In Python, we define booleans using the keywords True and False:")

print("________________________________________________________________")

print("Python automatically assigns a variable the appropriate datatype based on the value it is given. A variable with the value 7 is an integer, 7. is a float, \"7\" is a string. Sometimes we will want to convert variables to different datatypes. For example, if we wanted to print out an integer as part of a string, we would want to convert that integer to a string first. We can do that using str():")
age = 34
print("age = 34")
print("\"I am \" + str(age) + \" years old!\"")
print ("I am " + str(age) + " years old!")

print("________________________________________________________________")