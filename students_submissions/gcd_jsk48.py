def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    #both zero
    if a == 0 and b == 0:
        return None
    # Handling negatives 
    a, b = abs(a), abs(b)
    # base case 
    if b == 0:
        return a
    return gcd(b, a % b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
