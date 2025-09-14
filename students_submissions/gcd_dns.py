def gcd(a: int, b: int) -> int:

    if not isinstance(a, int) or not isinstance(b, int):
        print(f"Error: Both arguments must be integers. Got {type(a)} and {type(b)}")
        return None

    if a == 0 and b == 0:
        print("Error: GCD is undefined for a = 0 and b = 0")
        return None

    a, b = abs(a), abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)

if __name__ == "__main__":
    print(gcd(54, 24))   # Expected: 6
    print(gcd(48, 18))   # Expected: 6
    print(gcd(101, 10))  # Expected: 1
    print(gcd(-54, 24))  # Expected: 6 (negatives handled)
