# Alejandro Serna CS490 HW2


def gcd(a: int, b: int) -> int:
    if a | b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None
    elif b == 0:
        return abs(a)
    return gcd(b, a % b)


# Test Cases
if __name__ == "__main__":
    print(gcd(54, 24))  # Expected output: 6
    print(gcd(48, 18))  # Expected output: 6
    print(gcd(101, 10))  # Expected output: 1
    print(gcd(-48, 18))  # 6
    print(gcd(48, -18))  # 6
    print(gcd(-48, -18))  # 6
    print(gcd(0, 7))   # 7
    print(gcd(5, 0))   # 5
    print(gcd(13, 7))  # 1
    print(gcd(25,25)) # 25
    print(gcd(0, 0)) # Can't have 0 bc undefined 
