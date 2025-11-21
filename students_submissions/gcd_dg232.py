def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm recursively.

    Returns:
        int: The GCD of a and b, or None if input is invalid.
    """
    # Check for invalid input
    if not isinstance(a, int) or not isinstance(b, int):
        print("This is error, both inputs must be integers.")
        return None
    
    # Handle edge cases
    if a == 0 and b == 0:
        print("this is error, GCD is undefined for a = 0 and b = 0.")
        return None
    
    # Make numbers positive (GCD is always non-negative)
    a, b = abs(a), abs(b)

    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(54, 24))    
    print(gcd(48, 18))    
    print(gcd(101, 10))   
    print(gcd(-36, 60))  
    print(gcd(0, 5))      
    print(gcd(0, 0))      
    print(gcd(13, 17))    