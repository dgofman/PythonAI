'''
3. Write a function named times_ten. The function should accept an argument and display the
product of its argument multiplied times 10.

>> python hw1_exercise3.py
<< 50

>> python hw1_exercise3.py hello_world
<< 50

>> python hw1_exercise3.py 10
<< 100
'''

from sys import argv

def main(argv):
    try:
        val = int(argv[1])
    except (IndexError, ValueError): 
        val = 5 # default value
    
    times_ten = lambda : val * 10
    print(times_ten())

if __name__ == "__main__":
    main(argv)