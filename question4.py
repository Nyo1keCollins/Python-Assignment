# Function to reverse each string in a list of strings
def reverse_strings(strings):
    reversed_list = []
    for string in strings:
        reversed_list.append(string[::-1])
    return reversed_list

# Example usage
strings = ["apple", "banana", "cherry"]
print(reverse_strings(strings))  # Output: ["elppa", "ananab", "yrrehc"]
