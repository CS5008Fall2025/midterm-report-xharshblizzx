#!/usr/bin/env python3
"""
Generates charts for Fibonacci algorithm analysis including C vs Python comparison.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_comparison_chart():
    """Generate C vs Python comparison chart."""

    # Load data
    python_df = pd.read_csv('timings_fib_python.csv')
    c_df = pd.read_csv('timings_fib_c.csv')

    # Create comparison chart
    plt.figure(figsize=(12, 8))

    # Filter out TIMEOUT values
    c_df_clean = c_df.copy()
    c_df_clean['Recursive'] = pd.to_numeric(c_df_clean['Recursive'], errors='coerce')

    # Plot comparison for n=20, 30, 35
    n_compare = [20, 30, 35]
    methods = ['Iterative', 'Recursive', 'DP']
    x = np.arange(len(methods))
    width = 0.35

    for i, n in enumerate(n_compare):
        plt.subplot(1, 3, i+1)

        py_times = python_df[python_df['N'] == n][methods].iloc[0]
        c_times = c_df_clean[c_df_clean['N'] == n][methods].iloc[0]

        plt.bar(x - width/2, py_times, width, label='Python', alpha=0.8, color='blue')
        plt.bar(x + width/2, c_times, width, label='C (simulated)', alpha=0.8, color='orange')

        plt.xlabel('Algorithm')
        plt.ylabel('Time (seconds)')
        plt.title(f'n = {n}')
        plt.xticks(x, methods, rotation=45)
        plt.legend()
        plt.yscale('log')

    plt.tight_layout()
    plt.savefig('c_vs_python_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("C vs Python comparison chart generated!")

if __name__ == "__main__":
    generate_comparison_chart()
