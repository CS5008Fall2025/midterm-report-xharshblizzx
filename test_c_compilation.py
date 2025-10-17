#!/usr/bin/env python3
"""
Test script to verify C compilation and basic functionality.
"""

import subprocess
import sys
import os

def test_c_compilation():
    """Test if C code compiles and runs basic functionality."""

    gcc_path = r"C:\Users\joshc\Downloads\gcc-15.2.0-gdb-16.3.90.20250511-binutils-2.45-mingw-w64-v13.0.0-ucrt\bin\gcc.exe"

    # Check if GCC exists
    if not os.path.exists(gcc_path):
        print("GCC not found at expected path")
        return False

    try:
        # Compile the C code
        result = subprocess.run([gcc_path, "fibonacci.c", "-o", "fibonacci.exe"],
                              capture_output=True, text=True, cwd=".")

        if result.returncode != 0:
            print(f"Compilation failed: {result.stderr}")
            return False

        print("C code compiled successfully")

        # Test basic functionality
        result = subprocess.run(["fibonacci.exe", "iterative", "10"],
                              capture_output=True, text=True, cwd=".")

        if result.returncode == 0:
            print(f"C iterative test passed: {result.stdout.strip()}")
            return True
        else:
            print(f"C test failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"Error testing C compilation: {e}")
        return False

if __name__ == "__main__":
    success = test_c_compilation()
    sys.exit(0 if success else 1)
