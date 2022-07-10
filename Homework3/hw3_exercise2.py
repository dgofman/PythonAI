'''
2. Write a class definition named Book. The Book class should have data attributes for a book’s
title, the author’s name, and the publisher’s name. The class should also have the following:
An _ _init_ _ method for the class. The method should accept an argument for each of the data attributes.
Accessor and mutator methods for each data attribute.
An _ _str_ _ method that returns a string indicating the state of the object.

>> python hw3_exercise2.py

Title: Cracking the Coding Interview, Author: Gayle Laakmann McDowell, Publisher: CareerCup
Title: Python for Dummies, Author: Stef Maruch, Publisher: Wiley & Sons, Incorporated, John
'''

class Book:
    def __init__(self, title: str='', author: str='', publisher: str=''):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    def __str__(self):
       return "Title: {}, Author: {}, Publisher: {}".format(self.title, self.author, self.publisher)

def main():
    book1 = Book()
    book1.title = "Cracking the Coding Interview"
    book1.author = "Gayle Laakmann McDowell"
    book1.publisher = "CareerCup"
    print(book1)

    book2 = Book("Python for Dummies", "Stef Maruch", "Wiley & Sons, Incorporated, John")
    print(book2)

if __name__ == "__main__":
    main()