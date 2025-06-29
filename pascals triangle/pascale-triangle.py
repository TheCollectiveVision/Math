#pascale_triangle  in python
def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    max_length = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        print(" ".join(map(str, row)).center(max_length))
        
# Example usage
n = int(input("Enter the number of rows for Pascal's Triangle: "))  # Change this value to generate more or fewer rows
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)