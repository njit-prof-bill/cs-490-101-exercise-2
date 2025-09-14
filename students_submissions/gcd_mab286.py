def gcd(a: int, b: int) -> int:

    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    pass

    # Check for invalid types
    if not isinstance(a, int) or not isinstance(b, int):
        print("Invalid Type Error: Only Integers are valid")
        return

    # Base case: if b is 0, gcd is a (absolute value to handle negatives)
    if b == 0:
        return abs(a)

    # Recursive step
    return gcd(b, a % b)

# Test Cases
print(gcd(10, 20))   # 10
print(gcd(12, 18))   # 6
print(gcd(7, 13))    # 1  (primes)
print(gcd(-8, 12))   # 4  (handles negatives)
print(gcd("a", 5))   # Error message + returns None
