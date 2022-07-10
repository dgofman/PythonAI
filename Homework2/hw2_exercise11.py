'''
4. Write a loop that counts the number of lowercase characters that appear in the string referenced by mystring.

>> python hw2_exercise11.py
Number of lowercase characters: 430
'''

from lorem_ipsum import LoremIpsum

class CountLowercases(LoremIpsum):

    def __init__(self):
        LoremIpsum.__init__(self)

def main():
    c = CountLowercases()
    c.count()
    print("Number of lowercase characters:", c.lower)

if __name__ == "__main__":
    main()