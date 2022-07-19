"""
Some problems can be solved through recursion only. True or False?
    True

Besides recursion, what other approach can you use to solve a problem that is repetitive in nature?
    Using loops is one of the options: https://wiki.python.org/moin/ForLoop


1. Recursive Lines
Write a recursive function that accepts an integer argument, n. The function should display n
lines of asterisks on the screen, with the first line showing 1 asterisk, the second line showing 2
asterisks, up to the nth line which shows n asterisks.

>> python hw4_exercise1.py

*
**
***

>> python hw4_exercise1.py 5

*
**
***
****
*****

>> python hw4_exercise1.py 5 $

$
$$
$$$
$$$$
$$$$$
"""
from sys import argv

def recursiveLines(width: int, fillchar = '*'):
    if width != 0:
        recursiveLines(width - 1, fillchar)
    print(''.ljust(width, fillchar))

def main(argv):
    if len(argv) == 3:
        recursiveLines(int(argv[1]), argv[2])
    elif len(argv) == 2:
        recursiveLines(int(argv[1]))
    else:
       recursiveLines(3) 

if __name__ == "__main__":
    main(argv)
