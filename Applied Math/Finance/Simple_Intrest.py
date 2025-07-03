# Simple intrest calculator

def main():
    principal_amount = print(float(input("Enter your principal amount ($): ")))
    intrest_rate = print(float(input("Enter the intrest rate (%): ")))
    time = print(float(input("Enter the time applied: ")))
    
    intrest = (principal_amount * intrest_rate * time) / 100
    total_amount = principal_amount + intrest
    
    print(f"Total amount after {time} at {intrest_rate}% simple intrest is ${total_amount} ")
    
if __name__ == "__main__":
    main()