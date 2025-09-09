def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a == 0 and b == 0:
        return 0

    a = abs(a)
    b = abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)

print()

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(0, 12))
print(gcd(0, 0))
print(gcd(-10, 15))
print(gcd(12, -18))
print(gcd(7, 7))
print(gcd(-5, -5))