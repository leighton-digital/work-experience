// Challenge 2: Find the Largest Number in a List
// Scenario: A student is writing a function to find the largest number in a list but encounters an issue.

// The function should return the largest number in an array, but it's not working correctly.
function findLargest(arr) {
  let largest = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < largest) {
      largest = arr[i];
    }
  }
  return largest;
}

// Example usage:
// console.log(findLargest([1, 2, 3, 4, 5])); // Expected output: 5
