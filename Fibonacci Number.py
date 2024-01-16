#!/usr/bin/env python3
import time

def fibonacci_naive(n: int) -> int:
	if n < 2:
		return n
	else:
		return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

def fibonacci_memo(n: int) -> int:
	memo = {} # {key_0: value_0, key_1: value_1, ...}
	def fibonacci(n):
		if n not in memo:
			if n < 2:
				memo[n] = n
			else:
				memo[n] = fibonacci(n-1) + fibonacci(n-2)
		return memo[n]
	
	return fibonacci(n)

start = time.time()
fibonacci_naive(40)
end = time.time()
elapsed_time = end - start
print("Naive time: ", elapsed_time, " sec")

start = time.time()
fibonacci_memo(40)
end = time.time()
elapsed_time = end - start
print("Memo time: ", elapsed_time, " sec")
