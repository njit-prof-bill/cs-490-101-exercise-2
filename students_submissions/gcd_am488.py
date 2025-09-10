def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Validate argument types
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: gcd() requires two integers.")
        return None

    # gcd(0, 0) is undefined
    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    # Ensure nonnegative values
    a, b = abs(a), abs(b)

    # Base case
    if b == 0:
        return a

    # Recursive step
    return gcd(b, a % b)

    pass


# Test cases
#print(gcd(54, 24))  # Expected output: 6
#print(gcd(48, 18))  # Expected output: 6
#print(gcd(101, 10))  # Expected output: 1
#print(gcd("hello", 10))  # Expected output: 1
#print(gcd(0, 0))  # Expected output: 1


