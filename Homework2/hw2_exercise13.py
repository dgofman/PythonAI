'''
1. Alphabetic Telephone Number Translator
Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their
customers to remember. On a standard telephone, the alphabetic letters are mapped to numbers in the following fashion:
A, B, and C = 2
D, E, and F = 3
G, H, and I = 4
J, K, and L = 5
M, N, and O = 6
P, Q, R, and S = 7
T, U, and V = 8
W, X, Y, and Z = 9
Write a program that asks the user to enter a 10-character telephone number in the format XXXXXX-XXXX. 
The application should display the telephone number with any alphabetic characters that appeared in the original translated to their numeric equivalent. 
For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663

>> python hw2_exercise13.py 555-GET-FOOD
555-438-3663

>> python hw2_exercise13.py HELLOWORLD  
435-569-6753

>> python hw2_exercise13.py pyt-hon-1234 
798-466-1234
'''

import sys

class Telephone:
    __letters_map = {
        **dict.fromkeys(['A', 'B', 'C'], 2),
        **dict.fromkeys(['D', 'E', 'F'], 3),
        **dict.fromkeys(['G', 'H', 'I'], 4),
        **dict.fromkeys(['J', 'K', 'L'], 5),
        **dict.fromkeys(['M', 'N', 'O'], 6),
        **dict.fromkeys(['P', 'Q', 'R', 'S'], 7),
        **dict.fromkeys(['T', 'U', 'V'], 8),
        **dict.fromkeys(['W', 'X', 'Y', 'Z'], 9)
    }
    
    def letter2number(self, str):
        chars = list(str.upper().replace('-', ''))
        for index, c in enumerate(chars):
            num = self.__letters_map.get(c)
            if num:
                chars[index] = num
        return "{}{}{}-{}{}{}-{}{}{}{}".format(*chars)

def main(argv):
    t = Telephone()
    print(t.letter2number(argv[1]))

if __name__ == "__main__":
    main(sys.argv)