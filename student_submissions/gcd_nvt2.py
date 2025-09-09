def gcd(a: int, b: int) -> int:
    # cannot use loops, therefore use recursion
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))