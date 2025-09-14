def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm recursively (no loops).
    Returns None on invalid input.
    """
    try:
        # Validate inputs
        if not isinstance(a, int) or not isinstance(b, int):
            print("Error: inputs must be integers")
            return None

        # Convert to absolute values so negatives work
        a, b = abs(a), abs(b)

        # Edge case: both zero
        if a == 0 and b == 0:
            print("Error: gcd(0, 0) is undefined")
            return None

        # Base case
        if b == 0:
            return a
        return gcd(b, a % b)

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# -------------------------
# Basic Test Cases
# -------------------------
if __name__ == "__main__":
    print(gcd(54, 24))   # Expected: 6
    print(gcd(48, 18))   # Expected: 6
    print(gcd(101, 10))  # Expected: 1
    print(gcd(-42, 56))  # Expected: 14
    print(gcd(0, 7))     # Expected: 7
    print(gcd(0, 0))     # Expected: None
