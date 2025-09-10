def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if type(a) != int or type(b) != int:
        print("ERROR: Both a and b must be of integer type. Value of a: ", a, "Value of b: ", b)
        return None

    if b == 0:
        return a
    else:
        return gcd(abs(b), abs(a%b))

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
