#!/home/nate/python/python_env/bin/python3
# ASCII Characters: https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
"""Password Generator"""

import random
import time
import string
from typing import final, no_type_check
import ast

#
# A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)


# Dictionary with all uppercase and lowercase letters
def build_alphabet():
    uppercase = []
    lowercase = []
    alphabet = {}
    for i in string.ascii_uppercase:
        uppercase.append(i)
    for i in string.ascii_lowercase:
        lowercase.append(i)
    for i in uppercase:
        alphabet[i] = i
    for i in lowercase:
        alphabet[i] = i
    return alphabet


# Asks user to specify how many characters they want the password to be
alphabet = build_alphabet()
prompt = "How many characters should your password consist of? Please enter a value of 8 or more: "
error = "Please enter a whole number. Decimals and letters are not allowed. "

# Test to check if the user input a whole number. It will loop if it receives a str or float.
def test_whole_num(x):
    x = input(prompt)
    try:
        if type(x) == float:
            return test_whole_num(x)
        elif int(x):
            return x
    except ValueError:
        if type(x) == str:
            return test_whole_num(x)


x = ""
x = test_whole_num(x)
print(x)
x = int(x)


# # Deny any value less than 8 and greater than 20
# def check_requirement():
#   if int_conversion <= 8:
#     print(f'A password containing {int_conversion} characters cannot be created. Please sprcify a value of at least 8.')
#   elif int_conversion >= 8:
#     print(f'A password containing {int_conversion} characters cannot be created. Please sprcify a value less than 20.')
#   elif type(int_conversion) != int:
#     print(f'A password containing {int_conversion} characters cannot be created. Please sprcify a whole number that is greater than 8 and less than 20.')
#   else:
#     print(f'Your password will contain {int_conversion} characters.')

# print(f'Your password will contain {int_conversion} characters')

# # #Main program starts here
# # uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
# # uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
# # lowercaseLetter1=chr(random.randint(97,122))#Random lowercase letter
# # lowercaseLetter2=chr(random.randint(97,122))#Random lowercase letter
# # digit1=chr(random.randint(48,57))#Random integer generator
# # digit2=chr(random.randint(48,57))#Random integer generator
# # punctuationSign1=(random.randint(33,47))#Random Punctuation
# # punctuationSign2=(random.randint(33,47))#Random Punctuation

# # #Generate password using all the characters, in random order
# # password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2) + str(punctuationSign1) + str(punctuationSign2) # + ....
# # password = shuffle(password)

# # #Ouput
# # print(password)
