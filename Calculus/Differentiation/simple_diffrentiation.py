# Simple Differentiation

def diffrentiate(a,n):
    
    # Given the polynomial ax^n the derrivative is given by n*ax^(n-1)
    if n == 0:
        return 0
    else:
        return a * n, n - 1
    
def main():
    print("Enter the coefficient a and the power n for the polynomial ax^n")
    a = int(input("Coefficient a: "))
    n = int(input("Power n: "))
    
    result = diffrentiate(a, n)
    
    if result == 0:
        print("The derivative is 0")
    else:
        print(f"The derivative of {a}x^{n} is {result[0]}x^{result[1]}")
        
if __name__ == "__main__":
    main()