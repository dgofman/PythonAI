'''
True or False

1. Polymorphism allows you to write methods in a subclass that have the same name as methods in the superclass.
True. Example: https://www.geeksforgeeks.org/polymorphism-in-python/


2. It is not possible to call a superclass’s _ _init_ _ method from a subclass’s __init__ method.
True. Example: https://www.geeksforgeeks.org/__init__-in-python/

3. A subclass can have a method with the same name as a method in the superclass.
True. Example: https://www.geeksforgeeks.org/polymorphism-in-python/


4. Only the _ _init_ _ method can be overridden.
False. 

5. You cannot use the isinstance function to determine whether an object is an instance of a
subclass of a class.
False. Example: https://www.geeksforgeeks.org/type-isinstance-python/


1. Look at the following class definition. What is the name of the superclass? What is the name of the subclass?

class Tiger(Felis):
    What is the name of the superclass? - Felis
    What is the name of the subclass? - Tiger

Coding:

1. Employee and ProductionWorker Classes
Write an Employee class that keeps data attributes for the following pieces of information:
Employee name
Employee number
Next, write a class named ProductionWorker that is a subclass of the Employee class. The
ProductionWorker class should keep data attributes for the following information:
Shift number (an integer, such as 1, 2, or 3)
Hourly pay rate
The workday is divided into two shifts: day and night. The shift attribute will hold an integer
value representing the shift that the employee works. The day shift is shift 1 and the night shift
is shift 2. Write the appropriate accessor and mutator methods for each class.
Once you have written the classes, write a program that creates an object of the
ProductionWorker class and prompts the user to enter data for each of the object’s data
attributes. Store the data in the object, then use the object’s accessor methods to retrieve it and display it on the screen.

>> python hw3_exercise4.py

Initialize:
Employee Name: David Gofman
Employee Number: 1001
Shift: Unknown Shift
Pay Rate: 0.0


Day Rate:
Employee Name: David Gofman
Employee Number: 1001
Shift: Day Shift
Pay Rate: 20.9


Night Rate:
Employee Name: David Gofman
Employee Number: 1001
Shift: Night Shift
Pay Rate: 25.5
'''
from enum import Enum

class Shift(Enum):
    DAY = (1, "Day Shift")
    NIGHT = (2, "Night Shift")
    UNKNOWN = (3, "Unknown Shift")

    def __str__(self):
        return self.value[1]

class Employee:
    def __init__(self, name: str, number: int):
        self.__name = name
        self.__number = number
    
    def __str__(self):
       return "Employee Name: {}\nEmployee Number: {}".format(self.__name , self.__number)
       
class ProductionWorker(Employee):
    def __init__(self, name: str, number: int):
        Employee.__init__(self, name, number)
        self.__shift = Shift.UNKNOWN
        self.__rate = 0.0
        
    def __str__(self):
       return "{}\nShift: {}\nPay Rate: {}".format(Employee.__str__(self), self.shift, self.rate)

    @property
    def shift(self):
        return self.__shift
    
    @shift.setter
    def shift(self, shift):
        self.__shift = shift

    @property
    def rate(self):
        return self.__rate
    
    @rate.setter
    def rate(self, rate):
        self.__rate = rate

def main():
    emp = ProductionWorker("David Gofman", 1001)
    print("\n\nInitialize:\n{}".format(emp))
    emp.shift = Shift.DAY
    emp.rate = 20.90
    print("\n\nDay Rate:\n{}".format(emp))
    emp.shift = Shift.NIGHT
    emp.rate = 25.50
    print("\n\nNight Rate:\n{}".format(emp))

if __name__ == "__main__":
    main()