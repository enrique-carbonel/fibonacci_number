# fibonacci_number
Calculation of the 40th Fibonacci number using two different methods. This project was made for my Systems Programming for Engineers class.

SHEBANG LINE: This line specifies the interpreter to be used for running the script. In this case, it suggests using the Python 3 interpreter.

IMPORTING THE TIME MODULE: The time module is used to measure the execution time of the functions.

NAIVE RECURSIVE FIBONACCI FUNCTION: This calculates the nth Fibonacci number by recursively summing the (n-1)th and (n-2)th Fibonacci numbers. This approach has an exponential time complexity and is not efficient for large values of n.

MEMOIZED RECURSIVE FIBONACCI FUNCTION: The code stores previously computed Fibonacci numbers in a dictionary (memo) to avoid redundant calculations. If the Fibonacci number for a particular n is already computed, it retrieves it from the memo instead of recalculating. This results in a significant improvement in performance compared to the naive approach.

TIMING EXECUTION OF EACH FUNCTION: This measures and prints the time taken by each method to calculate the 40th Fibonacci number. The times are printed in seconds.

this script demostrates the significant performance improvement achieved by using memoization in recursive algorithms, particularly evident in the context of calculating Fibonacci numbers.
