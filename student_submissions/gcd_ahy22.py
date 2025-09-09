def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if(a==0 or b==0):
        print("One of the inputs cannot be zero")
        return None
    else:
        return gcd_helper(abs(max(a,b)), abs(min(a,b)))
    pass

def gcd_helper(big: int, small: int) -> int:
    quotient = big // small
    remainder = big % small
    if(remainder == 0):
        return small
    else:
        return gcd_helper(small, remainder)

# should be 2
print(gcd(11284,874))

# should be error
print(gcd(0,5))

# should be 10
print(gcd(-250,10))

# should be 14
print(gcd(42,56))

# should be 32
print(gcd(7966496, 314080416))