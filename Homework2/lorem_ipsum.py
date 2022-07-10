class LoremIpsum:
    __mystring = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    1 2, buckle my shoe!
    3 4, knock at the door!
    5 6, picking up sticks!
    7 8, don't be late!
    9 10, let's say it again!
    """

    def __init__(self):
        self.spaces = 0
        self.digits = 0
        self.lower  = 0

    def count(self):
        for i in self.__mystring:
            self.spaces += 1 if i.isspace() else 0
            self.digits += 1 if i.isdigit() else 0
            self.lower += 1 if i.islower() else 0