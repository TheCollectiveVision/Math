#Calculating pi using Nilakantha's algorithm
import math
def calculate_pi(terms):
    pi = 3.0
    sign = 1.0
    for n in range(1, terms + 1):
        term = sign * (4.0 / (2 * n * (2 * n + 1) * (2 * n + 2)))
        pi += term
        sign *= -1.0  # Alternate the sign for the next term
    return pi
if __name__ == "__main__":
    terms = int(input("Enter the number of terms to calculate pi: "))
    pi_value = calculate_pi(terms)
    print(f"Calculated value of pi using {terms} terms: {pi_value}")
    print(f"Math library value of pi: {math.pi}")
    print(f"Difference: {abs(pi_value - math.pi)}")