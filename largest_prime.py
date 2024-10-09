#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import argparse
from fibonnaci import get_fibonacci

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number within a limit.")
    parser.add_argument("limit", type=int, help="The upper limit for Fibonacci numbers")

    args = parser.parse_args()
    
    fib_numbers = get_fibonacci(args.limit) # get Fibonacci numbers less than the given limit

    prime_fib = [n for n in fib_numbers if prime(n)] # get prime fibonacci numbers

	# find largest prime fibonacci number in sequence
    if prime_fib:	
        largest_prime = max(prime_fib)
        print(f"The largest prime Fibonacci number less than {args.limit} is {largest_prime}")
    else:
        print(f"There are no prime Fibonacci numbers less than {args.limit}.")