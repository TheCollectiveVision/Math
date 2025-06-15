def main():
    print("Welcome to the Quadratic Formula Solver!")
    print("This program will help you find the roots of a quadratic equation of the form ax^2 + bx + c = 0.")
    print("We will calculate the discriminant and then find the roots based on its value using the formula (-b +/- sqrt(b^2 - 4ac)/2a where the discriminant is b^2 - 4ac).")
    a = float(input("Enter the coefficient x^2: "))
    b = float(input("Enter the coefficient x: "))
    c = float(input("Enter the constant term: "))
    if a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        return
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("The equation has no real roots.")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"The equation has one real root: {root}")
    elif discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        print(f"The equation has two real roots: {root1} and {root2}") 
    
    solution1 = (-b + discriminant**0.5) / (2 * a) if discriminant >= 0 else None
    solution2 = (-b - discriminant**0.5) / (2 * a) if discriminant >= 0 else None
    print(f"Solutions: {solution1}, {solution2}")

if __name__ == "__main__":
    main()    