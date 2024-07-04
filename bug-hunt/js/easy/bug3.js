// Challenge 3: Reverse a String
// Scenario: A student is trying to write a function to reverse a string, but it doesn't work as intended.

// The function should return the reversed string, but it's not working correctly.
function reverseString(str) {
  let reversed = "";
  for (let i = 0; i < str.length; i++) {
    reversed += str[i];
  }
  return reversed;
}

// Example usage:
// console.log(reverseString("hello")); // Expected output: "olleh"
