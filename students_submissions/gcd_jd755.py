def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if b == 0:
        if a == 0:
            print("Error: The GCD of 0 and 0 is undefined.")
            return None
        return a
    
    remainder = abs(a) % abs(b)

    return gcd(b, remainder)

# Test cases
#print(gcd(54, 24))  # Expected output: 6
#print(gcd(48, 18))  # Expected output: 6
#print(gcd(101, 10))  # Expected output: 1

#print(gcd(0, 0)) # Expected output: None/undefined

#print(gcd(100, 0)) # Expected output: 100
#print(gcd(0, 100)) # Expected output: 100

#print(gcd(-54, -24)) # Expected output: 6

#print(gcd(5, 7)) # Expected output: 1
#print(gcd(89, 83)) # Expected output: 1