# students_submissions/gcd_wfm8.py

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the (recursive) Euclidean algorithm. No loops allowed.

    On invalid input or undefined cases, prints an informative message
    and returns None.
    """
    if any(isinstance(x, bool) for x in (a, b)) or not (isinstance(a, int) and isinstance(b, int)):
        print(f"Error: gcd expects two integers.")
        return None
    
    a, b = abs(a), abs(b)

    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None
    def _rec(x: int, y: int) -> int:
        return x if y == 0 else _rec(y, x % y)

    return _rec(a, b)

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
