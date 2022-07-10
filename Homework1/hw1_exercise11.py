'''
5. Passing by reference: 
In class, we talked about passing by value.  For the mutable objects, like list, Python is passing by reference. Run the sample code and try to understand why.

Now write a function that passes the following arguments, and show if they are passing by reference:

Pass a tuple:  like (1,2,3,4)
Pass a string: like “hello world”
Pass a set, like {“apple”, “banna”, “orange”)
Pass a dictionary { “john”: 30, “Doe”: 40, “Henry”: 50}


>> python hw1_exercise11.py
<< reassign, no content change on list= [0]
<< content changed [0, 1]
<< original value:  (1, 2, 3, 4), expected changes:  [1, 2, 3] , actual changes:  (1, 2, 3, 4)
<< original value:  ['hello_world'], expected changes:  [] , actual changes:  []
<< original value:  {'orange', 'banna', 'apple'}, expected changes:  {'banna', 'apple'} , actual changes:  {'banna', 'apple'}
<< original value:  {'john': 30, 'Doe': 40, 'Henry': 50}, expected changes:  {'Doe': 40, 'Henry': 50} , actual changes:  {'Doe': 40, 'Henry': 50}
'''

def reassign(list):
  list = [0, 1]   #list is the local variable, will not change the arg value

def append(list):
  list.append(1)  #the arg is not changed, but the content changed

def change(val, remove):
    if type(val) is tuple:
        val = list(val)
    val.pop(*remove)
    return val

def main():
    list = [0]
    reassign(list)
    print ("reassign, no content change on list=", list)

    append(list)
    print ("content changed", list)

    val1 = (1, 2, 3, 4)
    print("original value: ", val1, end="")
    print(", expected changes: ", change(val1, []), ", actual changes: ", val1, end="\n") #tuple is immutable

    val2 = ["hello_world"]
    print("original value: ", val2, end="")
    print(", expected changes: ", change(val2, []), ", actual changes: ", val2, end="\n")

    val3 = {"apple", "banna", "orange"}
    print("original value: ", val3, end="")
    print(", expected changes: ", change(val3, []), ", actual changes: ", val3, end="\n")

    val4 = {"john": 30, "Doe": 40, "Henry": 50}
    print("original value: ", val4, end="")
    print(", expected changes: ", change(val4, ["john"]), ", actual changes: ", val4, end="\n")

if __name__ == "__main__":
    main()
