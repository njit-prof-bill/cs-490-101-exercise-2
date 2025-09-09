def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None

    a = abs(a)
    b = abs(b)

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(f"Testing gcd(54, 0): Expected=54, Got={gcd(54, 0)}")

print(f"Testing gcd(-48, 18): Expected=6, Got={gcd(-48, 18)}")

print(f"Testing gcd(12345, 1): Expected=1, Got={gcd(12345, 1)}")
print(f"Testing gcd(1, 99): Expected=1, Got={gcd(1, 99)}")
print(f"Testing gcd(-10, 1): Expected=1, Got={gcd(-10, 1)}")

print(f"Testing gcd(13, 17): Expected=1, Got={gcd(13, 17)}")

print(f"Testing gcd(20, 20): Expected=20, Got={gcd(20, 20)}")
print(f"Testing gcd(-20, 20): Expected=20, Got={gcd(-20, 20)}")
print(f"Testing gcd(-20, -20): Expected=20, Got={gcd(-20, -20)}")

print(f"Testing gcd(10, 5.5): Expected=None, Got={gcd(10, 5.5)}")
print(f"Testing gcd(10, None): Expected=None, Got={gcd(10, None)}")
