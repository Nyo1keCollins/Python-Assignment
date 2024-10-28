# Function to print keys with even values from a dictionary
def print_even_value_keys(dictionary):
    for key, value in dictionary.items():
        if value % 2 == 0:
            print(key)

# Example usage
sample_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(sample_dict)  # Output: a c
