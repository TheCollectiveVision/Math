#Chain Rule Differentiation
# This code implements the chain rule for differentiation, which is used when differentiating composite functions.
# Function is the form y = f(x) * g(x), where f and g are polynomials.

from simple_diffrentiation_function_2terms_or_more import Polynomial

class ChainRule:
    def __init__(self):
        self.outer_poly = Polynomial()
        self.inner_poly = Polynomial()

    def differentiate(self):
        print("Differentiating composite function...")
        # Differentiate the outer function
        self.outer_poly.differentiate()
        # Differentiate the inner function
        self.inner_poly.differentiate()

    def main(self):
        print("Outer function:")
        self.outer_poly.main()
        print("Inner function:")
        self.inner_poly.main()
        self.differentiate()

if __name__ == "__main__":
    chain = ChainRule()
    chain.main()