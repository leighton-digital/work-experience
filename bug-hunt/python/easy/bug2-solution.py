def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example usage:
# print(find_largest([1, 2, 3, 4, 5])) # Expected output: 5
