'''
3. Write a loop that counts the number of digits that appear in the string referenced by mystring.

>> python hw2_exercise10.py
Number of digits: 11
'''

from lorem_ipsum import LoremIpsum

class CountDigits(LoremIpsum):

    def __init__(self):
        LoremIpsum.__init__(self)

def main():
    c = CountDigits()
    c.count()
    print("Number of digits:", c.digits)

if __name__ == "__main__":
    main()