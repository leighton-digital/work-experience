def reverse_string(s):
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s

# Example usage:
# print(reverse_string("hello")) # Expected output: "olleh"
