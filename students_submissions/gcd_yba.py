def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive, no loops).
    """
    # Validate input
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    
    # Handle negative numbers
    a, b = abs(a), abs(b)
    
    # Base case
    if b == 0:
        return a
    
    # Recursive call
    return gcd(b, a % b)

# Test cases
print(gcd(54, 24))   # Expected output: 6
print(gcd(48, 18))   # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(-27, 9))   # Expected output: 9
print(gcd(0, 5))     # Expected output: 5
print(gcd(0, 0))     # Expected output: 0
