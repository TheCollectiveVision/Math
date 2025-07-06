# Simple Differentiation of a Polynomial with Two or More Terms

terms = int(input("Enter the number of terms in the polynomial: "))

coefficients = []
powers = []

for i in range(terms):
    coeff = int(input(f"Enter coefficient for term {i+1}: "))
    power = int(input(f"Enter power for term {i+1}: "))
    coefficients.append(coeff)
    powers.append(power)


print("The polynomial is:")
for i in range(terms):
    if i == 0:
        print(f"{coefficients[i]}x^{powers[i]}", end="")
    else:
        print(f" + {coefficients[i]}x^{powers[i]}", end="")
print()

print("The derivative is:")
for i in range(terms):
    if powers[i] == 0:
        continue
    coeff, power = coefficients[i] * powers[i], powers[i] - 1
    if i == 0:
        print(f"{coeff}x^{power}", end="")
    else:
        print(f" + {coeff}x^{power}", end="")
print()