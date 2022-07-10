'''
4. Examine the following function header, then write a statement that calls the function, passing 12 as an argument.
def show_value(quantity):

>> python hw1_exercise4.py
<< Quantity accepted!

>> python hw1_exercise4.py 12
<< Quantity accepted!

>> python hw1_exercise4.py 10
<< Unexpected quantity: 10

>> python hw1_exercise4.py hello_world
<< Unexpected quantity: hello_world
'''

from sys import argv

QUANTITY = 12

def show_value(quantity):
    assert quantity == QUANTITY
    print("Quantity accepted!")

def main(argv):
    try:
        val = argv[1]
    except (IndexError): 
        val = QUANTITY
    
    try:
        show_value(int(val))
    except (ValueError, AssertionError):
        print("Unexpected quantity: {}".format(val))

if __name__ == "__main__":
    main(argv)