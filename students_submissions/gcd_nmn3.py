def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("error: inputs must be integers")
        return None

    a, b = abs(a), abs(b)

    if a == 0 and b == 0:
        print("error: gcd undefined")
        return None

    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(54, 24))
    print(gcd(-42, 56))
    print(gcd(101, 10))
    print(gcd(0, 25))
    print(gcd(0, 0))
    print(gcd("a", 5))
