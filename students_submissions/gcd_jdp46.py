def gcd(a: int, b: int) -> int:

    if not isinstance(a, int) or not isinstance(b, int):
        print("Requires integers")
        return None

    if a == 0 and b == 0:
        print("Undefined for 0, 0")
        return None

    a, b = abs(a), abs(b) # for negatives

    if b == 0:
        return a

    return gcd(b, a % b) # recursive step
