import sys
sys.path.append("../..")
from Numerical_Methods.Factorial.factorial import factorial

class EulersNumber:
    def __init__(self):
        self.e = self.compute_eulers_number()

    def compute_eulers_number(self):
        e = 0
        for n in range(100):
            e += 1 / factorial(n)
        return e
if __name__ == "__main__":
    euler_number_calculator = EulersNumber()
    print(f"The value of Euler's number (e) is approximately: {euler_number_calculator.e}")
