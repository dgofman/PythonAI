'''
1. What is encapsulation?
    https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)

In object-oriented programming (OOP), encapsulation refers to the bundling of data with the methods that operate on that data, or the restricting of direct access 
to some of an object's components. Encapsulation is used to hide the values or state of a structured data object inside a class, preventing direct access to them 
by clients in a way that could expose hidden implementation details or violate state invariance maintained by the methods.

2. Why should an object’s data attributes be hidden from code outside the class?
    https://programs.wiki/wiki/python_-private-properties-and-private-methods.html

A private attribute and private method are defined in the parent class, which means that the private attribute and private method are the privacy of the parent class. 
Since it is the privacy of the parent class, we cannot access the privacy of the parent class outside the methods of the child class.
In vernacular, private properties and private methods are the object's privacy, 
Since it is privacy, private attributes are attributes that do not want to be disclosed to the outside world.

3. What is the difference between a class and an instance of a class?
    https://en.wikipedia.org/wiki/Instance_(computer_science)

In object-oriented programming (OOP), an instance is a concrete occurrence of any object, existing usually during the runtime of a computer program. 
Formally, "instance" is synonymous with "object" as they are each a particular value (realization), and these may be called an instance object; "instance" 
emphasizes the distinct identity of the object. The creation of an instance is called instantiation.

In class-based programming, objects are created from classes by subroutines called constructors, and destroyed by destructors. 
An object is an instance of a class, and may be called a class instance or class object; instantiation is then also known as construction. 

4. The following statement calls an object’s method. What is the name of the method? What is the name of the variable that references the object?
   wallet.get_dollar()
What is the name of the method? - "get_dollar"
What is the name of the variable that references the object? - "wallet"

5. When the __init__ method executes, what does the self parameter reference to?
    https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/

"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. 
This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

6. In a Python class, how do you hide an attribute from code outside the class?
    http://ion.scottexteriors.com/wiki-https-docs.python.org/3/tutorial/classes.html#tut-private

“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. 
However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API 
(whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, 
called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, 
where classname is the current class name with leading underscore(s) stripped.


7. How do you call the following methods (which are also referred to magic methods): __str__, __init__, __call__
    __str__ - https://www.pythontutorial.net/python-oop/python-__str__/

To customize the string representation of a class instance, the class needs to implement the __str__ magic method.
Internally, Python will call the __str__ method automatically when an instance calls the str() method.
Note that the print() function converts all non-keyword arguments to strings by passing them to the str() before displaying the string values.

    __init__ - https://www.pythontutorial.net/python-oop/python-__init__/
When you create a new object of a class, Python automatically calls the __init__() method to initialize the object’s attributes.

    __call__ - https://www.geeksforgeeks.org/__call__-in-python/
The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function. 
When the instance is called as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).

Exercise 1:

Suppose my_car is the name of a variable that references an object, and go is the name of a
method. Write a statement that uses the my_car variable to call the go method. (You do not have to pass any arguments to the go method.)

>> python hw3_exercise1.py

Distance 32 miles
'''
import math

class Car:
    # approximate radius of earth in miles
    R = 3960

    def __init__(self, make: str, model: str, year: int):
        self._make = make
        self._model = model
        self._year = year
    
    def destination(self, start_point: tuple, end_point: tuple):
        self.start_point = start_point
        self.end_point = end_point
    
    def go(self):
        lat1 = math.radians(self.start_point[0])
        lon1 = math.radians(self.start_point[1])
        lat2 = math.radians(self.end_point[0])
        lon2 = math.radians(self.end_point[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        print("Distance {:.0f} miles".format(self.R * c))

def main():
    SanFrancisco = (37.7577627, -122.4726194) #latitude longitude
    Sunnyvale = (37.3958499, -122.0939077)    #latitude longitude
    my_car = Car("Toyota", "RAV4 Prime", 2022)
    my_car.destination(SanFrancisco, Sunnyvale)
    my_car.go()

if __name__ == "__main__":
    main()