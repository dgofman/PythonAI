'''
5. Look at the following function header:
def my_function(a, b, c):
Now look at the following call to my_function:
my_function(3, 2, 1)
When this call executes, what value will be assigned to a?
What value will be assigned to b?
What value will be assigned to c?

>> python hw1_exercise5.py
<< a=3, b=2, c=1
'''

def my_function(a, b, c):
  print("a={}, b={}, c={}".format(a, b, c)) # a=3, b=2, c=1

def main():
    my_function(3, 2, 1)

if __name__ == "__main__":
    main()
