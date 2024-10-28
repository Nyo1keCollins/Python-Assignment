# Function to check if any two distinct numbers in a list add up to a target sum
def has_pair_with_sum(numbers, target_sum):
    seen_numbers = set()
    for number in numbers:
        if target_sum - number in seen_numbers:
            return True
        seen_numbers.add(number)
    return False

# Example usage
numbers_list = [1, 2, 3, 9]
print(has_pair_with_sum(numbers_list, 8))  # Output: False
print(has_pair_with_sum(numbers_list, 5))  # Output: True
