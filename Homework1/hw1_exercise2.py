'''
>> python hw1_exercise2.py

<< The script is called: hw1_exercise2.py
<< Your first variable is: David
<< Your second variable is: Gofman
<< Your third variable is: Python For AI Basics -2022

>> python hw1_exercise2.py Hello World !

<< The script is called: hw1_exercise2.py
<< Your first variable is: Hello
<< Your second variable is: World
<< Your third variable is: !
'''

from sys import argv

#arg2, arg3, arg4 are optional sys arguments
def printArgs(arg1, arg2 = "David", arg3 = "Gofman", arg4 = "Python For AI Basics -2022"):
    script, first, second, third = [arg1, arg2, arg3, arg4]
    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)

def main(argv):
    printArgs(*argv)

if __name__ == "__main__":
    main(argv)