#!/home/nate/python/python_env/bin/python3
# ASCII Characters: https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
"""Password Generator
    By: Nate Orage"""

from typing import Counter, final, no_type_check
import secrets
import string


def pw_gen(x):
    prompt = "\nHow many characters should your password consist of? Please enter a value of 8 or more: "
    error = "\nPlease enter a whole number. Decimals and letters are not allowed. "
    x = input(prompt)
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    combined = lowercase + uppercase + num + symbols
    # Input Validation
    try:
        if type(x) == float:
            return pw_gen(x)
        elif int(x) >= 8:
            x = int(x)
            password = "".join(secrets.choice(combined) for i in range(x))
            print(
                f"Your password is:\n{password}\nYour password consists of {x} characters. Please keep it safe."
            )
        elif int(x) < 8:
            return pw_gen(x)
    except ValueError:
        if type(x) == str:
            return pw_gen(x)


x = ""
pw_gen(x)
