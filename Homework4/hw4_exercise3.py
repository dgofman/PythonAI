"""
3. Sum of Numbers
Design a function that accepts an integer argument and returns the sum of all the integers from 1 up to the number passed as an argument. For example, if 50 is passed as an argument, the
function will return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.

>> python hw4_exercise3.py

The sum of 50 = 1275

>> python hw4_exercise3.py 10

The sum of 10 = 55
"""
from sys import argv

def sumNumbers(max: int, sum = 0):
    sum += max
    if max > 1:
        return sumNumbers(max - 1, sum)
    return sum

def main(argv):
    max = 50
    if len(argv) == 2:
        max = int(argv[1])
    print("The sum of {} = {}".format(max, sumNumbers(max)))

if __name__ == "__main__":
    main(argv)
