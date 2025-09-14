def gcd(a: int, b: int) -> int:
  
    if not isinstance(a, int) or not isinstance(b, int):
        print(f"Error: gcd expects integers, got a={type(a).__name__}, b={type(b).__name__}")
        return None

    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    a = -a if a < 0 else a
    b = -b if b < 0 else b

    if b == 0:
        return a

    return gcd(b, a % b)

if __name__ == "__main__":
    print("gcd(54, 24) =", gcd(54, 24))    
    print("gcd(48, 18) =", gcd(48, 18))    
    print("gcd(101, 10) =", gcd(101, 10))  
    print("gcd(-27, 9) =", gcd(-27, 9))    
    print("gcd(0, 5)   =", gcd(0, 5))      
    print("gcd(0, 0)   =", gcd(0, 0))      
    print("gcd(3.5, 2) =", gcd(3.5, 2))   