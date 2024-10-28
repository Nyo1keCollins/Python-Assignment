# Function to convert a list of tuples into a dictionary
def tuples_to_dictionary(tuple_list):
    result = {}
    for key, value in tuple_list:
        result[key] = value
    return result

# Example usage
sample_tuples = [("apple", 5), ("banana", 10), ("cherry", 15)]
print(tuples_to_dictionary(sample_tuples))  # Output: {'apple': 5, 'banana': 10, 'cherry': 15}
