# Challenge 3: Reverse a String
# Scenario: A student is trying to write a function to reverse a string, but it doesn't work as intended.
# The function should return the reversed string, but it's not working correctly.

def reverse_string(s):
    reversed_s = ""
    for i in range(len(s)):
        reversed_s += s[i]
    return reversed_s

# Example usage:
# print(reverse_string("hello")) # Expected output: "olleh"
