#!/usr/bin/env python3
"""
Test suite for Fibonacci implementations.
Validates correctness of iterative, recursive, and DP algorithms.
"""

def test_fibonacci_correctness():
    """Test that all implementations produce correct Fibonacci values."""
    from fibonacci import fib_iterative, fib_recursive, fib_dp

    # Known Fibonacci values
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    print("Testing Fibonacci correctness...")

    for n in range(len(expected)):
        iter_result = fib_iterative(n)
        rec_result = fib_recursive(n)
        dp_result = fib_dp(n)

        assert iter_result == expected[n], f"Iterative failed for n={n}: got {iter_result}, expected {expected[n]}"
        assert rec_result == expected[n], f"Recursive failed for n={n}: got {rec_result}, expected {expected[n]}"
        assert dp_result == expected[n], f"DP failed for n={n}: got {dp_result}, expected {expected[n]}"

        print(f"n={n}: All methods correct (F({n}) = {expected[n]})")

    print("All correctness tests passed!")

if __name__ == "__main__":
    test_fibonacci_correctness()
