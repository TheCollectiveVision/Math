def main():
    principal_amount = print(float("Enter the principal amount($): "))
    intrest_rate = print(float("Enter the intrest rate(%): "))
    time = print(int("Enter the time applied: "))
    compound_frequency = print(int("Enter the number of times interest is compounded per year: "))
    compound_interest = principal_amount * (1 + (intrest_rate / 100) / compound_frequency) ** (compound_frequency * time)
    print(f"The compound interest is: ${compound_interest:.2f}")
if __name__ == "__main__":
    main()