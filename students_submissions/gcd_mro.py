def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here

    #Handle Non-Integers
    if not isinstance(a,int) or not isinstance(b,int):
        print("Error. Both Numbers must be integers.")
        return None 
    
    #Handle Negative Numbers

    a = abs(a)
    b = abs(b)

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test cases
print(gcd(5.4, 24))  # Expected output: Error
print(gcd('a', 24))  # Expected output: Error

print(gcd(48, 18))  # Expected output: 6

print(gcd(17, 13))  # Expected output: 1
print(gcd(17, 34))  # Expected output: 17

print(gcd(-101, 10))  # Expected output: 1

print(gcd(7, 0))  # Expected output: 7
print(gcd(0, 0))  # Expected output: 0
