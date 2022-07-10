'''
3. Prime Number List
Please write the is_prime function. Write another program that displays all of the prime numbers from 1 to 100. The program should have a loop that calls the is_prime function.

>> python hw1_exercise9.py
<< [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(max):
    prime_numbers = []
    for num in range(1, max):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

def main():
    print(getPrimeNumbers(100))

if __name__ == "__main__":
    main()
