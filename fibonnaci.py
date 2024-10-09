#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def get_fibonacci(limit):
    fib_seq = []
    a = 0
    b = 1
    while a < limit:	
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers less than a limit.")
    parser.add_argument("limit", type=int, help= "Upper limit for Fibonacci numbers")
    parser.add_argument("output_file", type=str, help= "Output file to write Fibonacci numbers")
    
    args = parser.parse_args()

    fib_numbers = get_fibonacci(args.limit) # get fibonacci numbers

    # writing Fibonacci numbers to file
    try:
        with open(args.output_file, "w") as f:
            for number in fib_numbers:
                f.write(f"{number}\n")
        print(f"Fibonacci numbers under {args.limit} have been written to {args.output_file}")
    except IOError as e:
        print(f"Error while writing to the file: {e}")
