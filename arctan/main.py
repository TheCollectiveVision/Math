#class to calculate the arctangent of (1/x)
from decimal import Decimal, getcontext
class ArctanCalculator:
    def __init__(self, precision):
        getcontext().prec = precision + 2  # Set precision for Decimal calculations
        self.precision = precision

    def calculate_arctan(self, x):
        if x == 0:
            return Decimal(0)
        elif x < 0:
            return -self.calculate_arctan(-x)

        arctan_value = Decimal(0)
        term = Decimal(1) / Decimal(x)  # First term of the series
        n = 0

        while term > Decimal(10) ** (-self.precision):
            arctan_value += term / (2 * n + 1)
            n += 1
            term *= -Decimal(1) / (x * x)

        return arctan_value
    
if __name__ == "__main__":
    precision = int(input("Enter the number of decimal places for arctan(1/x): "))
    x = Decimal(input("Enter the value of x: "))
    calculator = ArctanCalculator(precision)
    arctan_value = calculator.calculate_arctan(x)
    print(f"Calculated value of arctan(1/{x}) to {precision} decimal places: {arctan_value}")