import subprocess
import csv
import sys

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "TIMEOUT", "", -1

def test_fibonacci():
    # Skip C compilation since gcc not available, focus on Python
    methods = ["iterative", "recursive", "dp"]
    n_values = list(range(1, 41))  # Up to 40 for timing

    # Python timings
    with open("timings_fib_python.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["N", "Iterative", "Recursive", "DP"])
        for n in n_values:
            row = [n]
            for method in methods:
                stdout, stderr, code = run_command(f"python fibonacci.py {method} {n}")
                if code == 0:
                    row.append(stdout)
                else:
                    row.append("TIMEOUT")
            writer.writerow(row)

    # Operations for small n
    n_ops = 20
    with open("ops_fib_python.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["N", "Iterative", "Recursive", "DP"])
        for n in range(1, n_ops + 1):
            row = [n]
            for method in ["print_iter", "print_rec", "print_dp"]:
                stdout, stderr, code = run_command(f"python fibonacci.py {method} {n}")
                if code == 0:
                    lines = stdout.split('\n')
                    ops_line = [line for line in lines if "Operations:" in line]
                    if ops_line:
                        ops = ops_line[0].split(": ")[1]
                        row.append(ops)
                    else:
                        row.append("N/A")
                else:
                    row.append("TIMEOUT")
            writer.writerow(row)

if __name__ == "__main__":
    test_fibonacci()
