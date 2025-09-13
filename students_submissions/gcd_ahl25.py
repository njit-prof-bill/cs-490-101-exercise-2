def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    
    Returns None if inputs are not valid.
    """

    # input validation
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Inputs must be integers.")
        return None

    # handle negative numbers (GCD is always non-negative)
    a, b = abs(a), abs(b)

    # base case: if b is 0, GCD is a
    if b == 0:
        return a

    # recursive case
    return gcd(b, a % b)


#test cases
if __name__ == "__main__":
    print(gcd(54, 24))   # expected output: 6
    print(gcd(48, 18))   # expected output: 6
    print(gcd(101, 10))  # expected output: 1 (prime number case)
    print(gcd(-48, 18))  # expected output: 6 (handles negative)
    print(gcd("a", 18))  # expected error message + None