def main():
    print("This is the main function of the cubic formula module.")
    print("This program will help you find the roots of a cubic equation of the form ax^3 + bx^2 + cx + d = 0.")
    a = float(input("Enter the coefficient x^3 (a): "))
    b = float(input("Enter the coefficient x^2 (b): "))
    c = float(input("Enter the coefficient x (c): "))
    d = float(input("Enter the constant term (d): "))
    if a == 0:
        print("Coefficient 'a' cannot be zero for a cubic equation.")
        return
    
    value1 = (-((b)**3)/(27 * a **3)) + ((b*c)/(6*a**2)) - (d/(2*a))
    value2 = value1**2 + ((c/(3*a))**3)
    value3 = value2 ** (1/2)
    
    alpha = (value1 + value3) ** (1/3) 
    beta = (value1 - value3) ** (1/3)
    gamma = - b/(3 * a)
    
    solutions = alpha + beta + gamma
    
    print(f"The solution to the cubic equation {a}x^3 + {b}x^2 + {c}x + {d} = 0 is: {solutions}")
    
if __name__ == "__main__":
    main()