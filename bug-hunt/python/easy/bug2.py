# Challenge 2: Find the Largest Number in a List
# Scenario: A student is writing a function to find the largest number in a list but encounters an issue.

# The function should return the largest number in a list, but it's not working correctly.
def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num < largest:
            largest = num
    return largest

# Example usage:
# print(find_largest([1, 2, 3, 4, 5])) # Expected output: 5
