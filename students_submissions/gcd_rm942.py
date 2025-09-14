def gcd(a: int, b: int) -> int:
    if a < b:
        temp = a
        a = b
        b = temp
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
    
print(gcd(100,30))
print(gcd(34,1))
print(gcd(120,60))