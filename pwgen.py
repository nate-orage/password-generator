#!/home/nate/python/python_env/bin/python3
#ASCII Characters: https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
'''Password Generator'''

import random
#
# A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122))#Random lowercase letter
lowercaseLetter2=chr(random.randint(97,122))#Random lowercase letter
digit1=chr(random.randint(48,57))#Random integer generator
digit2=chr(random.randint(48,57))#Random integer generator
punctuationSign1=(random.randint(33,47))#Random Punctuation
punctuationSign2=(random.randint(33,47))#Random Punctuation


#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2) + str(punctuationSign1) + str(punctuationSign2) # + ....
password = shuffle(password)

#Ouput
print(password)