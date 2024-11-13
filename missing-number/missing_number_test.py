def missing_number(A):
    # Create a set to store positive numbers in A
    numbers = set()
    
    # Filter only positive numbers
    for num in A:
        if num > 0:
            numbers.add(num)
    
    # Find the smallest positive integer missing
    smallest_positive = 1
    while smallest_positive in numbers:
        smallest_positive += 1
    
    return smallest_positive

# Examples
print(missing_number([1, 3, 6, 4, 1, 2]))  # Output: 5
print(missing_number([1, 2, 3]))          # Output: 4
print(missing_number([-1, -3]))           # Output: 1
