def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if not all(isinstance(x, int) for x in (a, b)):
        print("All inputs must be integers.")
        return None
    
    if a == 0 and b == 0:
        print("GCD is undefined for a = 0 and b = 0.")
        return None

    a, b = abs(a), abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(54, 24))     # Expected: 6
print(gcd(48, 18))     # Expected: 6
print(gcd(101, 10))    # Expected: 1
print(gcd(0, 0))       # Expected: None
print(gcd(0, 5))       # Expected: 5
print(gcd(5, 0))       # Expected: 5
print(gcd(-48, 18))    # Expected: 6
print(gcd(270, 192))   # Expected: 6
print(gcd(1, 1))       # Expected: 1
print(gcd("a", 10))    # Expected: None
