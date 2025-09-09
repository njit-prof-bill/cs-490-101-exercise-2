def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        raise ValueError("undefined output, both inputs are zero")
    elif a == 0:
        return b
    elif b == 0:
        return a
    
    a, b = max(a, b), min(a, b)
    remainder = a % b
    while remainder != 0:
        a, b = b, remainder
        remainder = a % b
    
    return b

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1