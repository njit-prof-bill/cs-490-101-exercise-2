def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm with recursion (no loops).
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both arguments must be integers")
        return None
    
    a = abs(a)
    b = abs(b)
    
    if a == 0 and b == 0:
        print("Error: GCD of (0, 0) is undefined")
        return None
    elif a == 0:
        return b
    elif b == 0:
        return a

    return gcd(b, a % b)


# Test cases
if __name__ == "__main__":
    print("Testing GCD function:")
    print("=" * 30)
    
    print(f"gcd(54, 24) = {gcd(54, 24)}")  # Expected: 6
    print(f"gcd(48, 18) = {gcd(48, 18)}")  # Expected: 6
    print(f"gcd(101, 10) = {gcd(101, 10)}")  # Expected: 1
    
    # Edge cases
    print(f"gcd(17, 13) = {gcd(17, 13)}")  # Prime numbers, expected: 1
    print(f"gcd(12, 0) = {gcd(12, 0)}")  # One zero, expected: 12
    print(f"gcd(0, 15) = {gcd(0, 15)}")  # One zero, expected: 15
    print(f"gcd(0, 0) = {gcd(0, 0)}")  # Both zero, expected: None with error
    