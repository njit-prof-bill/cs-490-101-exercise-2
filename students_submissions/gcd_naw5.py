def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a == 0 and b == 0:
        print("Error - GCD is undefined when both a and b are 0")
        return None

    a, b = abs(a), abs(b)

    #basecase
    if b == 0:
        return a

    return gcd(b, a % b)
  
    pass

'''
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(1, 1)) 
'''

