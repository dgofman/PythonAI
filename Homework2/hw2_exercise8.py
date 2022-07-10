'''
1. Assume choice references a string. The following if statement determines whether choice is equal to ‘Y’ or ‘y’:
if choice == 'Y' or choice == 'y':
Rewrite this statement so it only makes one comparison, and does not use the or operator.
(Hint: use either the upper or lower methods.)


>> python hw2_exercise8.py
Do you want to continue? (y/n)y
Do you want to continue? (y/n)Y
Do you want to continue? (y/n)n
Thanks!
'''

def main():
    while True:
        choice = input("Do you want to continue? (y/n)")
        if choice.upper() != 'Y':
            break
    print("Thanks!")


if __name__ == "__main__":
    main()