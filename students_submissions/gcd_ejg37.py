def gcd(a: int, b: int) -> int:

    if type(a) is not int or type(b) is not int:
        print("Both not integers")
        return None

    if a == 0 and b == 0:
        print("GCD is 0, 0")
        return None

    if a < 0 or b < 0:
        print("Can't be a negative number")
        return None

    if b == 0:
        return a
    
    return gcd(b, a % b)


print(gcd(54, 24))  
print(gcd(48, 18))  
print(gcd(101, 10)) 