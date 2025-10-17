#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

/**
 * Computes the nth Fibonacci number using an iterative approach.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * @param n The index of the Fibonacci number to compute (n >= 0)
 * @return The nth Fibonacci number
 */
long long fib_iterative(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

/**
 * Computes the nth Fibonacci number using a recursive approach.
 * Time Complexity: O(2^n) due to exponential branching
 * Space Complexity: O(n) for recursion stack
 * @param n The index of the Fibonacci number to compute (n >= 0)
 * @return The nth Fibonacci number
 */
long long fib_recursive(int n) {
    if (n <= 1) return n;
    return fib_recursive(n - 1) + fib_recursive(n - 2);
}

/**
 * Computes the nth Fibonacci number using dynamic programming with memoization.
 * Time Complexity: O(n)
 * Space Complexity: O(n) for memoization array
 * @param n The index of the Fibonacci number to compute (n >= 0)
 * @return The nth Fibonacci number
 */
long long *memo;
long long fib_dp(int n) {
    if (memo[n] != -1) return memo[n];
    if (n <= 1) return memo[n] = n;
    return memo[n] = fib_dp(n - 1) + fib_dp(n - 2);
}

// Print series iteratively with operations count
void print_series_iterative(int n, long long *ops) {
    *ops = 0;
    long long a = 0, b = 1;
    printf("1: 0\n");
    if (n >= 1) printf("2: 1\n");
    for (int i = 3; i <= n; i++) {
        long long c = a + b;
        printf("%d: %lld\n", i, c);
        a = b;
        b = c;
        (*ops)++;
    }
}

// Print series recursively (not efficient, but for completeness)
void print_series_recursive(int n, long long *ops) {
    *ops = 0;
    for (int i = 1; i <= n; i++) {
        printf("%d: %lld\n", i, fib_recursive(i));
        (*ops) += (i > 1) ? 1 : 0; // simplistic
    }
}

// Print series DP
void print_series_dp(int n, long long *ops) {
    *ops = 0;
    memo = (long long *)malloc((n + 1) * sizeof(long long));
    for (int i = 0; i <= n; i++) memo[i] = -1;
    for (int i = 1; i <= n; i++) {
        printf("%d: %lld\n", i, fib_dp(i));
        (*ops)++;
    }
    free(memo);
}

// Timing function
double time_function(long long (*func)(int), int n) {
    clock_t start = clock();
    func(n);
    clock_t end = clock();
    return (double)(end - start) / CLOCKS_PER_SEC;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <method> <n>\n", argv[0]);
        return 1;
    }
    char *method = argv[1];
    int n = atoi(argv[2]);

    if (strcmp(method, "iterative") == 0) {
        double time = time_function(fib_iterative, n);
        printf("%.6f\n", time);
    } else if (strcmp(method, "recursive") == 0) {
        double time = time_function(fib_recursive, n);
        printf("%.6f\n", time);
    } else if (strcmp(method, "dp") == 0) {
        memo = (long long *)malloc((n + 1) * sizeof(long long));
        for (int i = 0; i <= n; i++) memo[i] = -1;
        double time = time_function(fib_dp, n);
        printf("%.6f\n", time);
        free(memo);
    } else if (strcmp(method, "print_iter") == 0) {
        long long ops = 0;
        print_series_iterative(n, &ops);
        printf("Operations: %lld\n", ops);
    } else if (strcmp(method, "print_rec") == 0) {
        long long ops = 0;
        print_series_recursive(n, &ops);
        printf("Operations: %lld\n", ops);
    } else if (strcmp(method, "print_dp") == 0) {
        long long ops = 0;
        print_series_dp(n, &ops);
        printf("Operations: %lld\n", ops);
    } else {
        printf("Invalid method\n");
    }
    return 0;
}
