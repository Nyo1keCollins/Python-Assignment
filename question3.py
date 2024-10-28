# Function to return the sum of all numbers in a list
def sum_of_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Example usage
nums = [1, 2, 3, 4, 5]
print(sum_of_list(nums))
