import sys as s
s.path.append("../..")
from Numerical_Methods.Factorial.factorial import factorial



def Sine(radians): 
    sine = 0
    sign = 0
        
    for idx in range(1,100,2):
        if sign % 2 == 0:
            sine += radians**idx/factorial(idx)
        else:
            sine -= radians**idx/factorial(idx)
        sign += 1 
    
    return sine 