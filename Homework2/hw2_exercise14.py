'''
2. Sentence Capitalizer
Write a program with a function that accepts a string as an argument and returns a copy of the string with the first character of each sentence capitalized. 
For instance, if the argument is “hello. my name is Joe. what is your name?” the function should return the string “Hello. My name is Joe. What is your name?” 
The program should let the user enter a string and then pass it to the function. The modified string should be displayed.

>> python hw2_exercise14.py hello. my name is Joe. what is your name? please.   
Hello. My name is Joe. What is your name? Please.

>> python hw2_exercise14.py hi!     my name is David.    glad to meet you.
Hi! My name is David. Glad to meet you.
'''

import sys
import re

class Capitalizer:

    def toCapitalize(self, str):
        end_chars = ['.', '!', '?']
        list = re.split('(\W)', str)
        isCapitalize = True
        for index, s in enumerate(list):
            char = s[0] if len(s) > 0 else ''
            if not isCapitalize and end_chars.count(char):
                isCapitalize = True
            elif isCapitalize and char.isalpha():
                list[index] = char.upper() + s[1:]
                isCapitalize = False
        return ''.join(list)

def main(argv):
    str = " ".join(argv[1:])
    c = Capitalizer()
    print(c.toCapitalize(str))

if __name__ == "__main__":
    main(sys.argv)