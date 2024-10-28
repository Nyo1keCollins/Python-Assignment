# Function to remove duplicates from a list without using `set`
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
sample_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(sample_list))  # Output: [1, 2, 3, 4, 5]
