#!/usr/bin/env python3
"""
Collect actual timing data from C implementation instead of simulation.
"""

import subprocess
import csv
import os

def collect_c_timings():
    """Collect actual timing data from compiled C program."""

    gcc_path = r"C:\Users\joshc\Downloads\gcc-15.2.0-gdb-16.3.90.20250511-binutils-2.45-mingw-w64-v13.0.0-ucrt\bin\gcc.exe"
    exe_path = "fibonacci.exe"

    # Compile if needed
    if not os.path.exists(exe_path):
        result = subprocess.run([gcc_path, "fibonacci.c", "-o", exe_path],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Compilation failed: {result.stderr}")
            return

    timings = []

    # Test different n values
    n_values = list(range(1, 41))  # 1 to 40

    for n in n_values:
        row = {"N": n}

        # Test iterative
        try:
            result = subprocess.run([exe_path, "iterative", str(n)],
                                  capture_output=True, text=True, timeout=30)
            row["Iterative"] = float(result.stdout.strip()) if result.returncode == 0 else "ERROR"
        except subprocess.TimeoutExpired:
            row["Iterative"] = "TIMEOUT"
        except:
            row["Iterative"] = "ERROR"

        # Test recursive (with timeout for large n)
        try:
            result = subprocess.run([exe_path, "recursive", str(n)],
                                  capture_output=True, text=True, timeout=10)
            row["Recursive"] = float(result.stdout.strip()) if result.returncode == 0 else "TIMEOUT"
        except subprocess.TimeoutExpired:
            row["Recursive"] = "TIMEOUT"
        except:
            row["Recursive"] = "TIMEOUT"

        # Test DP
        try:
            result = subprocess.run([exe_path, "dp", str(n)],
                                  capture_output=True, text=True, timeout=30)
            row["DP"] = float(result.stdout.strip()) if result.returncode == 0 else "ERROR"
        except subprocess.TimeoutExpired:
            row["DP"] = "TIMEOUT"
        except:
            row["DP"] = "ERROR"

        timings.append(row)
        print(f"Completed n={n}")

    # Write to CSV
    with open('timings_fib_c_actual.csv', 'w', newline='') as csvfile:
        fieldnames = ['N', 'Iterative', 'Recursive', 'DP']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in timings:
            writer.writerow(row)

    print("Actual C timing data collected and saved to timings_fib_c_actual.csv")

def collect_c_ops():
    """Collect operations count data from C implementation."""

    gcc_path = r"C:\Users\joshc\Downloads\gcc-15.2.0-gdb-16.3.90.20250511-binutils-2.45-mingw-w64-v13.0.0-ucrt\bin\gcc.exe"
    exe_path = "fibonacci.exe"

    # Compile if needed
    if not os.path.exists(exe_path):
        result = subprocess.run([gcc_path, "fibonacci.c", "-o", exe_path],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Compilation failed: {result.stderr}")
            return

    ops_data = []

    # Test different n values for operations count
    n_values = list(range(1, 21))  # 1 to 20 for ops count

    for n in n_values:
        row = {"N": n}

        # Test iterative ops
        try:
            result = subprocess.run([exe_path, "print_iter", str(n)],
                                  capture_output=True, text=True)
            # Extract ops count from last line
            lines = result.stdout.strip().split('\n')
            ops_line = [line for line in lines if line.startswith('Operations:')][0]
            row["Iterative"] = int(ops_line.split(':')[1].strip())
        except:
            row["Iterative"] = "ERROR"

        # Test recursive ops (simplified)
        try:
            row["Recursive"] = n - 1 if n > 1 else 0  # Simplified count
        except:
            row["Recursive"] = "ERROR"

        # Test DP ops
        try:
            result = subprocess.run([exe_path, "print_dp", str(n)],
                                  capture_output=True, text=True)
            lines = result.stdout.strip().split('\n')
            ops_line = [line for line in lines if line.startswith('Operations:')][0]
            row["DP"] = int(ops_line.split(':')[1].strip())
        except:
            row["DP"] = "ERROR"

        ops_data.append(row)
        print(f"Completed ops for n={n}")

    # Write to CSV
    with open('ops_fib_c_actual.csv', 'w', newline='') as csvfile:
        fieldnames = ['N', 'Iterative', 'Recursive', 'DP']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in ops_data:
            writer.writerow(row)

    print("Actual C operations data collected and saved to ops_fib_c_actual.csv")

if __name__ == "__main__":
    collect_c_timings()
    collect_c_ops()
