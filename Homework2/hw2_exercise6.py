'''
2. What will the following code display?

>> python hw2_exercise6.py

This code caused a ValueError.
The end.
'''

def main():
    try:
        x = float('abc123')
        print('The conversion is complete.')
    except IOError:
        print('This code caused an IOError.')
    except ValueError:
        print('This code caused a ValueError.')
        print('The end.')

if __name__ == "__main__":
    main()