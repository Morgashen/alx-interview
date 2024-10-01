def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Create a row with all elements initialized to 1
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Calculate the value based on the previous row
        triangle.append(row)
    
    return triangle

# Example usage:
n = 5
print(pascal_triangle(n))
