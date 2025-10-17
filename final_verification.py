#!/usr/bin/env python3
"""
Final verification script to ensure all components are working correctly.
"""

import os
import subprocess
import sys

def verify_c_compilation():
    """Verify C code compiles and runs correctly."""
    gcc_path = r"C:\Users\joshc\Downloads\gcc-15.2.0-gdb-16.3.90.20250511-binutils-2.45-mingw-w64-v13.0.0-ucrt\bin\gcc.exe"

    if not os.path.exists(gcc_path):
        print("❌ GCC not found")
        return False

    try:
        # Compile
        result = subprocess.run([gcc_path, "fibonacci.c", "-o", "fibonacci.exe"],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Compilation failed: {result.stderr}")
            return False

        # Test basic functionality
        result = subprocess.run(["fibonacci.exe", "iterative", "10"],
                              capture_output=True, text=True)
        if result.returncode != 0 or "0.000000" not in result.stdout:
            print(f"❌ C test failed: {result.stderr}")
            return False

        print("✅ C compilation and basic test passed")
        return True
    except Exception as e:
        print(f"❌ C verification error: {e}")
        return False

def verify_python_tests():
    """Verify Python tests pass."""
    try:
        result = subprocess.run([sys.executable, "test_fibonacci.py"],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Python tests failed: {result.stderr}")
            return False

        if "All correctness tests passed!" not in result.stdout:
            print("❌ Python tests did not pass")
            return False

        print("✅ Python tests passed")
        return True
    except Exception as e:
        print(f"❌ Python test error: {e}")
        return False

def verify_data_files():
    """Verify all required data files exist."""
    required_files = [
        'timings_fib_python.csv',
        'ops_fib_python.csv',
        'timings_fib_c_actual.csv',
        'ops_fib_c_actual.csv',
        'README.md'
    ]

    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print(f"❌ Missing files: {missing}")
        return False

    print("✅ All required data files present")
    return True

def verify_charts():
    """Verify chart files were generated."""
    chart_files = [
        'c_vs_python_actual_comparison.png',
        'big_o_theoretical_vs_empirical_actual.png'
    ]

    missing = []
    for file in chart_files:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print(f"❌ Missing chart files: {missing}")
        return False

    print("✅ All chart files generated")
    return True

def main():
    """Run all verifications."""
    print("🔍 Running final verification checks...\n")

    checks = [
        verify_c_compilation,
        verify_python_tests,
        verify_data_files,
        verify_charts
    ]

    passed = 0
    total = len(checks)

    for check in checks:
        if check():
            passed += 1
        print()

    print(f"📊 Verification Results: {passed}/{total} checks passed")

    if passed == total:
        print("🎉 All verifications passed! Report is ready for submission.")
        return True
    else:
        print("⚠️  Some checks failed. Please review and fix issues.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
