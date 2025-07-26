import sys as s
s.path.append("../..")
from Numerical_Methods.Pi_Algorithms.Machin_algo import MachinAlgorithm
from Geometry.Trigonometry.sine import Sine 
from Geometry.Trigonometry.cosine import Cosine 

def Tan(radians): 
    tan = Sine(radians)/Cosine(radians)

    return tan 


if __name__ == "__main__":
    precision = 10
    degree = int(input("Please input angle in degrees: "))
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    tan = Tan(radians)
    print(f'The value of tan is {tan:.2f}')
