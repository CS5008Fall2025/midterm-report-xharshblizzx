#!/usr/bin/env python3
"""
Generate charts using actual C timing data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_actual_charts():
    """Generate charts using actual collected C data."""

    # Load actual C data
    c_timings = pd.read_csv('timings_fib_c_actual.csv')
    c_ops = pd.read_csv('ops_fib_c_actual.csv')
    py_timings = pd.read_csv('timings_fib_python.csv')
    py_ops = pd.read_csv('ops_fib_python.csv')

    # Filter out TIMEOUT and ERROR values for plotting
    c_timings_clean = c_timings.replace(['TIMEOUT', 'ERROR'], np.nan).astype(float)
    py_timings_clean = py_timings.replace(['TIMEOUT', 'ERROR'], np.nan).astype(float)

    # Chart 1: C vs Python timing comparison
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(c_timings_clean['N'], c_timings_clean['Iterative'], 'b-', label='C Iterative', linewidth=2)
    plt.plot(py_timings_clean['N'], py_timings_clean['Iterative'], 'b--', label='Python Iterative', linewidth=2)
    plt.plot(c_timings_clean['N'], c_timings_clean['DP'], 'g-', label='C DP', linewidth=2)
    plt.plot(py_timings_clean['N'], py_timings_clean['DP'], 'g--', label='Python DP', linewidth=2)
    plt.plot(c_timings_clean['N'], c_timings_clean['Recursive'], 'r-', label='C Recursive', linewidth=2)
    plt.plot(py_timings_clean['N'], py_timings_clean['Recursive'], 'r--', label='Python Recursive', linewidth=2)
    plt.xlabel('N')
    plt.ylabel('Time (seconds)')
    plt.title('C vs Python: All Algorithms Timing Comparison')
    plt.legend()
    plt.yscale('log')

    # Chart 2: Operations count comparison
    plt.subplot(2, 2, 2)
    plt.plot(c_ops['N'], c_ops['Iterative'], 'b-', label='C Iterative', linewidth=2)
    plt.plot(py_ops['N'], py_ops['Iterative'], 'b--', label='Python Iterative', linewidth=2)
    plt.plot(c_ops['N'], c_ops['DP'], 'g-', label='C DP', linewidth=2)
    plt.plot(py_ops['N'], py_ops['DP'], 'g--', label='Python DP', linewidth=2)
    plt.plot(c_ops['N'], c_ops['Recursive'], 'r-', label='C Recursive', linewidth=2)
    plt.plot(py_ops['N'], py_ops['Recursive'], 'r--', label='Python Recursive', linewidth=2)
    plt.xlabel('N')
    plt.ylabel('Operations Count')
    plt.title('C vs Python: Operations Count Comparison')
    plt.legend()

    # Chart 3: C algorithms comparison
    plt.subplot(2, 2, 3)
    plt.plot(c_timings_clean['N'], c_timings_clean['Iterative'], 'b-', label='Iterative', linewidth=2)
    plt.plot(c_timings_clean['N'], c_timings_clean['DP'], 'g-', label='DP', linewidth=2)
    plt.plot(c_timings_clean['N'], c_timings_clean['Recursive'], 'r-', label='Recursive', linewidth=2)
    plt.xlabel('N')
    plt.ylabel('Time (seconds)')
    plt.title('C: Algorithm Performance Comparison')
    plt.legend()
    plt.yscale('log')

    # Chart 4: Speedup ratios
    plt.subplot(2, 2, 4)
    speedup_iter = py_timings_clean['Iterative'] / c_timings_clean['Iterative']
    speedup_dp = py_timings_clean['DP'] / c_timings_clean['DP']
    speedup_rec = py_timings_clean['Recursive'] / c_timings_clean['Recursive']

    plt.plot(c_timings_clean['N'], speedup_iter, 'b-', label='Iterative Speedup', linewidth=2)
    plt.plot(c_timings_clean['N'], speedup_dp, 'g-', label='DP Speedup', linewidth=2)
    plt.plot(c_timings_clean['N'], speedup_rec, 'r-', label='Recursive Speedup', linewidth=2)
    plt.xlabel('N')
    plt.ylabel('Python/C Time Ratio')
    plt.title('C Speedup vs Python (Higher = C faster)')
    plt.legend()
    plt.yscale('log')

    plt.tight_layout()
    plt.savefig('c_vs_python_actual_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Actual C vs Python comparison chart saved as c_vs_python_actual_comparison.png")

    # Generate additional charts for report
    # Big O theoretical vs empirical
    plt.figure(figsize=(10, 6))

    n_vals = np.array(c_timings_clean['N'])
    theoretical_iter = n_vals  # O(n)
    theoretical_dp = n_vals  # O(n)
    theoretical_rec = 2**n_vals  # O(2^n)

    # Normalize for comparison
    empirical_iter = c_timings_clean['Iterative'] / c_timings_clean['Iterative'].max()
    empirical_dp = c_timings_clean['DP'] / c_timings_clean['DP'].max()
    empirical_rec = c_timings_clean['Recursive'] / c_timings_clean['Recursive'].max()

    theoretical_iter_norm = theoretical_iter / theoretical_iter.max()
    theoretical_dp_norm = theoretical_dp / theoretical_dp.max()
    theoretical_rec_norm = theoretical_rec / theoretical_rec.max()

    plt.plot(n_vals, empirical_iter, 'b-', label='Empirical Iterative', linewidth=2)
    plt.plot(n_vals, theoretical_iter_norm, 'b--', label='Theoretical Iterative O(n)', linewidth=2)
    plt.plot(n_vals, empirical_dp, 'g-', label='Empirical DP', linewidth=2)
    plt.plot(n_vals, theoretical_dp_norm, 'g--', label='Theoretical DP O(n)', linewidth=2)
    plt.plot(n_vals, empirical_rec, 'r-', label='Empirical Recursive', linewidth=2)
    plt.plot(n_vals, theoretical_rec_norm, 'r--', label='Theoretical Recursive O(2^n)', linewidth=2)

    plt.xlabel('N')
    plt.ylabel('Normalized Time')
    plt.title('C: Theoretical vs Empirical Complexity Analysis')
    plt.legend()
    plt.yscale('log')

    plt.savefig('big_o_theoretical_vs_empirical_actual.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Theoretical vs empirical chart saved as big_o_theoretical_vs_empirical_actual.png")

if __name__ == "__main__":
    generate_actual_charts()
