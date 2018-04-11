import stdio
import sys


# Returns True if pwd is a valid password and False otherwise.
def is_valid(pwd):
    upper_case = 0
    lower_case = 0
    number = 0
    symbol = 0
    pwd = pwd.strip(' ')
    if(len(pwd) >= 8):
        for i in pwd:
            if i.isupper():
                upper_case += 1
            elif i.islower():
                lower_case += 1
            elif i.isdigit():
                number += 1
            else:
                 symbol += 1
        if(upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0):
            return True
        else:
           return False
    else:
        return False


# Test client [DO NOT EDIT]. Reads a password string as command-line argument
# and writes True if it's valid and False otherwise.
def _main():
    pwd = sys.argv[1]
    stdio.writeln(is_valid(pwd))

if __name__ == '__main__':
    _main()
