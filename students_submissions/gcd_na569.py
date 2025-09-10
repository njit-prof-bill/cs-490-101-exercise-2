def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    if a == 0 and b == 0:
        print("Error: GCD is undefined for a = 0 and b = 0.")
        return None

    # Use absolute values to handle negative numbers
    a, b = abs(a), abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(0, 0))        # Error: GCD is undefined...
print(gcd("a", 10))     # Error: Both inputs must be integers.
