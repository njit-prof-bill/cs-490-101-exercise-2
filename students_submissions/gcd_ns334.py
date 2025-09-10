def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive, no loops).

    Returns:
        int: The GCD of a and b, or None if input is invalid.
    """

    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: gcd() requires both arguments to be integers.")
        return None

    
    a, b = abs(a), abs(b)

    
    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(54,24))
print(gcd(48,18))
print(gcd(101,10))

