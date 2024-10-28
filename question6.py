# Function to find the largest number in a tuple
def find_largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers_tuple = (10, 20, 30, 40, 50)
print(find_largest_number(numbers_tuple))  # Output: 50
