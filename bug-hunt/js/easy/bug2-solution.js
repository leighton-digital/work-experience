function findLargest(arr) {
  let largest = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    }
  }
  return largest;
}

// Example usage:
// console.log(findLargest([1, 2, 3, 4, 5])); // Expected output: 5
