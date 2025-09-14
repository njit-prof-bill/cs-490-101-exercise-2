def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Input is not an int")
        return None
    if a == 0 and b == 0:
        print("Error: GCD is undefined. ")
        return None
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(48, 18))
    print(gcd(-48, 18))
    print(gcd(0, 25))
    print(gcd(0, 0))
