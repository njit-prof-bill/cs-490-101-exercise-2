def gcd(a: int, b: int) -> int:
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
    pass

print(gcd(48, 18))  
print(gcd(54, 24))  
print(gcd(101, 103)) 
print(gcd(0, 7))    
print(gcd(13, 17))