#!/usr/bin/env python3
"""
Generates charts for Fibonacci algorithm analysis.
Creates multiple visualizations comparing iterative, recursive, and DP approaches.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_charts():
    """Generate multiple charts for the report."""

    # Load timing data
    timings_df = pd.read_csv('timings_fib_python.csv')
    ops_df = pd.read_csv('ops_fib_python.csv')

    # Chart 1: Recursive vs DP timing (log scale)
    plt.figure(figsize=(10, 6))
    plt.plot(timings_df['N'], timings_df['Recursive'], label='Recursive', marker='o', color='red')
    plt.plot(timings_df['N'], timings_df['DP'], label='Dynamic Programming', marker='s', color='blue')
    plt.yscale('log')
    plt.xlabel('n (Fibonacci index)')
    plt.ylabel('Time (seconds, log scale)')
    plt.title('Recursive vs Dynamic Programming: Time Complexity Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('recursive_vs_dp_timing.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Chart 2: All three algorithms timing (linear scale)
    plt.figure(figsize=(10, 6))
    plt.plot(timings_df['N'], timings_df['Iterative'], label='Iterative', marker='^', color='green')
    plt.plot(timings_df['N'], timings_df['Recursive'], label='Recursive', marker='o', color='red')
    plt.plot(timings_df['N'], timings_df['DP'], label='Dynamic Programming', marker='s', color='blue')
    plt.xlabel('n (Fibonacci index)')
    plt.ylabel('Time (seconds)')
    plt.title('All Algorithms: Time Comparison (Linear Scale)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('all_algorithms_timing_linear.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Chart 3: Operations count comparison
    plt.figure(figsize=(10, 6))
    plt.plot(ops_df['N'], ops_df['Iterative'], label='Iterative', marker='^', color='green')
    plt.plot(ops_df['N'], ops_df['Recursive'], label='Recursive', marker='o', color='red')
    plt.plot(ops_df['N'], ops_df['DP'], label='Dynamic Programming', marker='s', color='blue')
    plt.xlabel('n (Fibonacci index)')
    plt.ylabel('Operations Count')
    plt.title('Operations Count Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('operations_count_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Chart 4: Big O theoretical vs empirical (log-log plot)
    plt.figure(figsize=(10, 6))

    # Theoretical curves
    n_vals = np.array(timings_df['N'])
    plt.loglog(n_vals, n_vals, label='O(n) - Linear', linestyle='--', color='green', alpha=0.7)
    plt.loglog(n_vals, 2**n_vals, label='O(2^n) - Exponential', linestyle='--', color='red', alpha=0.7)

    # Empirical data (scaled for visualization)
    scale_factor = 1e6  # Scale to make visible on log-log plot
    plt.loglog(timings_df['N'], timings_df['Iterative'] * scale_factor + 1, label='Iterative (empirical)', marker='^', color='green')
    plt.loglog(timings_df['N'], timings_df['Recursive'] * scale_factor + 1, label='Recursive (empirical)', marker='o', color='red')
    plt.loglog(timings_df['N'], timings_df['DP'] * scale_factor + 1, label='DP (empirical)', marker='s', color='blue')

    plt.xlabel('n (log scale)')
    plt.ylabel('Time/Operations (log scale)')
    plt.title('Theoretical Big O vs Empirical Performance')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('big_o_theoretical_vs_empirical.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Charts generated successfully!")

if __name__ == "__main__":
    generate_charts()
