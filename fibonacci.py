import sys
import time
from functools import lru_cache

def fib_iterative(n):
    """
    Computes the nth Fibonacci number using an iterative approach.

    Time Complexity: O(n) - performs n iterations
    Space Complexity: O(1) - uses constant space with only a few variables

    Args:
        n (int): The index of the Fibonacci number to compute (n >= 0)

    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_recursive(n):
    """
    Computes the nth Fibonacci number using a recursive approach.

    Time Complexity: O(2^n) - exponential due to redundant recursive calls
    Space Complexity: O(n) - recursion stack depth

    Args:
        n (int): The index of the Fibonacci number to compute (n >= 0)

    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

@lru_cache(maxsize=None)
def fib_dp(n):
    """
    Computes the nth Fibonacci number using dynamic programming with memoization.

    Time Complexity: O(n) - each subproblem solved once
    Space Complexity: O(n) - memoization cache stores up to n values

    Args:
        n (int): The index of the Fibonacci number to compute (n >= 0)

    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fib_dp(n - 1) + fib_dp(n - 2)

# Print series iteratively with operations count
def print_series_iterative(n):
    ops = 0
    a, b = 0, 1
    print("1: 0")
    if n >= 1:
        print("2: 1")
    for i in range(3, n + 1):
        c = a + b
        print(f"{i}: {c}")
        a, b = b, c
        ops += 1
    print(f"Operations: {ops}")

# Print series recursively (not efficient, but for completeness)
def print_series_recursive(n):
    ops = 0
    for i in range(1, n + 1):
        print(f"{i}: {fib_recursive(i)}")
        ops += 1 if i > 1 else 0
    print(f"Operations: {ops}")

# Print series DP
def print_series_dp(n):
    ops = 0
    for i in range(1, n + 1):
        print(f"{i}: {fib_dp(i)}")
        ops += 1
    print(f"Operations: {ops}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python fibonacci.py <method> <n>")
        return
    method = sys.argv[1]
    n = int(sys.argv[2])

    if method == "iterative":
        start = time.time()
        result = fib_iterative(n)
        end = time.time()
        print(f"{end - start:.6f}")
    elif method == "recursive":
        start = time.time()
        result = fib_recursive(n)
        end = time.time()
        print(f"{end - start:.6f}")
    elif method == "dp":
        start = time.time()
        result = fib_dp(n)
        end = time.time()
        print(f"{end - start:.6f}")
    elif method == "print_iter":
        print_series_iterative(n)
    elif method == "print_rec":
        print_series_recursive(n)
    elif method == "print_dp":
        print_series_dp(n)
    else:
        print("Invalid method")

if __name__ == "__main__":
    main()
