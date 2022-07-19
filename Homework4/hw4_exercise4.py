"""
4. Ackermann’s Function

Ackermann’s Function is a recursive mathematical algorithm that can be used to test how well a
system optimizes its performance of recursion. Design a function ackermann(m, n), which
solves Ackermann’s function. Use the following logic in your function:

If m = 0 then return n + 1
If n = 0 then return ackermann(m – 1, 1)
Otherwise, return ackermann(m – 1, ackermann(m, n – 1))

Once you’ve designed your function, test it by calling it with small values for m and n.

>> python hw4_exercise4.py 1 1
3

>> python hw4_exercise4.py 2 1
5

>> python hw4_exercise4.py 3 1
13

>> python hw4_exercise4.py 4 1
 RecursionError: maximum recursion depth exceeded in comparison
"""

import sys

recursionlimit = 200 #sys.getrecursionlimit()

def ackermann(m: int, n: int):
    if n > recursionlimit:
        return n #limit recursive calls (m = 4, n = 1 infinite calls)

    #print(''.ljust(n, "*")) #debug line
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

def main(argv):
    m = 1
    n = 1
    if len(argv) > 2:
        m = int(argv[1])
        n = int(argv[2])
    
    result = ackermann(m, n)
    if result > recursionlimit:
        print(f"\033[91m RecursionError: maximum recursion depth exceeded in comparison\033[00m")
    else:
        print(result)

if __name__ == "__main__":
    main(sys.argv)