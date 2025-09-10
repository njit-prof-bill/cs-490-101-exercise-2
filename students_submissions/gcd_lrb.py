def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    a = abs(a)
    b = abs(b)

    if a==0 and b==0:
        print("Division by Zero Error")
        return None
    if b==0:
        return a
    a, b = b, a % b
    return gcd(a, b)