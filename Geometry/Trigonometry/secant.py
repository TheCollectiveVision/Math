import sys as s
s.path.append("../..")
from Numerical_Methods.Pi_Algorithms.Machin_algo import MachinAlgorithm
from Geometry.Trigonometry.cosine import Cosine 

def Sec(radians): 
    sec = 1/Cosine(radians)

    return sec 


if __name__ == "__main__":
    precision = 10
    degree = int(input("Please input angle in degrees: "))
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    sec = Sec(radians)
    print(f'The value of cosec is {sec:.2f}')
