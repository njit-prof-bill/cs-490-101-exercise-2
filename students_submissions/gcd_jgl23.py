def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a == 0 and b == 0:
        print("There is an error. The GCD of 0 and 0 is undefined")
        return None
    
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(56, 98))    
print(gcd(48, 18))    
print(gcd(101, 103))  
print(gcd(7, 7))      
    