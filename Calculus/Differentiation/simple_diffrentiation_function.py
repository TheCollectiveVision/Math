# Class for Simple Differentiation of a Polynomial with Two or More Terms

class Polynomial:
    def __init__(self):
        self.terms = int(input("Enter the number of terms in the polynomial: "))
        self.coefficients = []
        self.powers = []

    def input_terms(self):
        for i in range(self.terms):
            coeff = float(input(f"Enter coefficient for term {i+1}: "))
            power = float(input(f"Enter power for term {i+1}: "))
            self.coefficients.append(coeff)
            self.powers.append(power)

    def differentiate(self):
        print("The derivative is:")
        for i in range(self.terms):
            if self.powers[i] == 0:
                continue
            coeff, power = self.coefficients[i] * self.powers[i], self.powers[i] - 1
            if i == 0:
                print(f"{coeff}x^{power}", end="")
            else:
                print(f" + {coeff}x^{power}", end="")

    def main(self):
        self.input_terms()
        self.differentiate()
        print()
        
if __name__ == "__main__":
    poly = Polynomial()
    poly.main()