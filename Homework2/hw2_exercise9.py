'''
2. Write a loop that counts the number of space characters that appear in the string referenced by mystring.

>> python hw2_exercise9.py
Number of space characters: 138
'''

from lorem_ipsum import LoremIpsum

class CountSpaces(LoremIpsum):

    def __init__(self):
        LoremIpsum.__init__(self)

def main():
    c = CountSpaces()
    c.count()
    print("Number of space characters:", c.spaces)

if __name__ == "__main__":
    main()