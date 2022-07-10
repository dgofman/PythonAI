'''
3. What will the following code display?

>> python hw2_exercise7.py

An error happened.
The end.
'''

def main():
    try:
        x = float('abc123')
        print(x)
    except IOError:
        print('This code caused an IOError.')
    except ZeroDivisionError:
        print('This code caused a ZeroDivisionError.')
    except:
        print('An error happened.')

    print('The end.')

if __name__ == "__main__":
    main()