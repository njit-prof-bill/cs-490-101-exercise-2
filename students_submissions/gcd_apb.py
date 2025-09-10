def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if not isinstance(a, int) or not isinstance(b, int):
        print("ERROR: Values must be on type integer only")
        return None
    
    if b == 0:
        return a
    else:
        return gcd(abs(b), abs(a % b))

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
