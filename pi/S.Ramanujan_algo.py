#Calculating the value of pi using Ramanujan's formula to a specific degree of accuracy.
# This script uses Ramanujan's series to approximate the value of pi.
import math
def ramanujan_pi(terms=10):
    """
    Calculate pi using Ramanujan's formula.
    
    Args:
        terms (int): Number of terms to use in the series.
        
    Returns:
        float: Approximation of pi.
    """
    total = 0
    for k in range(terms):
        numerator = math.factorial(4 * k) * (1103 + 26390 * k)
        denominator = (math.factorial(k) ** 4) * (396 ** (4 * k))
        total += numerator / denominator
    
    pi_approx = (2 * math.sqrt(2) / 9801) * total
    return 1 / pi_approx
if __name__ == "__main__":
    # Example usage
    terms = int(input("Enter the number of terms to use in the series: "))  # You can change this value to increase/decrease accuracy
    pi_value = ramanujan_pi(terms)
    # Ask user for desired decimal places
    decimal_places = int(input("Enter the number of decimal places for display: "))
    
    # Format the output with specified decimal places
    format_str = f"{{:.{decimal_places}f}}"
    print(f"Approximation of pi using {terms} terms: {format_str.format(pi_value)}")
    print(f"Actual value of pi: {format_str.format(math.pi)}")
    print(f"Difference: {format_str.format(abs(pi_value - math.pi))}")

# This script calculates the value of pi using Ramanujan's formula and compares it with the actual value of pi.
# The more terms you use, the more accurate the approximation will be.
# The script prints the approximation of pi, the actual value of pi, and the difference between them.
# Note: The Ramanujan formula converges very quickly, so even a small number of terms gives a very accurate result.