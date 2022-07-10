'''
6. What will the following program display?

>> python hw1_exercise6.py
<< 1 3.4
<< 0 0
<< 1 3.4
'''

def main():
  x = 1
  y = 3.4
  print(x, y) # x=1, y=3.4
  change_us(x, y)
  print(x, y) # x=1, y=3.4

def change_us(a, b):
  a = 0
  b = 0
  print(a, b) # a=0, b=0

if __name__ == "__main__":
    main()
