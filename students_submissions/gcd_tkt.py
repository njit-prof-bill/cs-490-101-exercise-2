def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    
    if a == 0 and b == 0:
        print("Error: GCD(0, 0) is undefined.")
        return None

    a, b = abs(a), abs(b)

    if b == 0: # base case
        return a
    return gcd(b, a % b) # recursive
    
# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1