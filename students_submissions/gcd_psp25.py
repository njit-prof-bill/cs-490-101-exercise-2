
def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    # Validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None

    # Handle both zero case (undefined GCD)
    if a == 0 and b == 0:
        print("Error: GCD is undefined when both numbers are zero.")
        return None

    # Work with absolute values (GCD is always non-negative)
    a, b = abs(a), abs(b)

    # Base case: when second number is zero
    if b == 0:
        return a

    # Recursive case
    return gcd(b, a % b)

# Test Cases
print(gcd(54, 24))    # Expected output: 6
print(gcd(48, 18))    # Expected output: 6
print(gcd(101, 10))   # Expected output: 1
print(gcd(0, 25))     # Expected output: 25
print(gcd(17, 0))     # Expected output: 17
print(gcd(0, 0))      # Expected output: None
print(gcd(-36, 24))   # Expected output: 12
print(gcd(-81, -27))  # Expected output: 27
print(gcd(100, 25))   # Expected output: 25
print(gcd("a", 5))    # Expected output: None
