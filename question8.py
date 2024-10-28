# Function to find keys where the value is greater than `n`
def keys_greater_than_n(dictionary, n):
    result = []
    for key, value in dictionary.items():
        if value > n:
            result.append(key)
    return result

# Example usage
sample_dict = {'a': 5, 'b': 12, 'c': 3}
print(keys_greater_than_n(sample_dict, 4))  # Output: ['a', 'b']
