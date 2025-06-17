#calculating the value of p(n) for n is a positive integer
def partition(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print(f"The number of partitions of {n} is: {partition(n)}")
# This code calculates the number of partitions of a positive integer n.
# A partition of a positive integer n is a way of writing n as a sum of positive integers, where the order of addends does not matter.
# The function partition(n) uses dynamic programming to compute the number of partitions.
# The main block allows the user to input a positive integer and prints the number of partitions for that integer.