"""
2. Largest List Item
Design a function that accepts a list as an argument and returns the largest value in the list. The
function should use recursion to find the largest item.

>> python hw4_exercise2.py

The largest value in the list: 9
"""

def largestItem(list, maxItem = -1):
    if list:
        return largestItem(list, max(maxItem, list.pop(0)))
    return maxItem

def main():
    maxItem = largestItem([1, 6, 2, 5, 8, 3, 9, 7, 4])
    print("The largest value in the list:", maxItem)

if __name__ == "__main__":
    main()