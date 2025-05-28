# Function to find indices of two numbers that add up to the target
def two_sum(nums, target):
    # Dictionary to store previously seen numbers and their indices
    num_to_index = {}

    # Loop over the list with index and value using enumerate
    for i, num in enumerate(nums):
        # Calculate the number needed to reach the target
        complement = target - num

        # Check if the complement has already been seen
        if complement in num_to_index:
            # If found, return the indices of the complement and the current number
            return [num_to_index[complement], i]

        # Store the current number and its index for future reference
        num_to_index[num] = i

# Test the function with examples
print(two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]
print(two_sum([3, 2, 4], 6))        # Output: [1, 2]
print(two_sum([3, 3], 6))           # Output: [0, 1]


#PROBLEM 2

# Function to rotate the array by one position in clockwise direction
def rotate_by_one(arr):
    # First, check if the array is empty or has only one element
    if len(arr) <= 1:
        return arr  # No rotation needed

    # Store the last element of the array (which will be moved to the front)
    last_element = arr[-1]  # arr[-1] accesses the last element

    # Shift all other elements to the right by one position using slicing
    # arr[:-1] gives all elements except the last
    rotated_array = [last_element] + arr[:-1]

    # Return the rotated array
    return rotated_array

# Test the function with example inputs
print(rotate_by_one([1, 2, 3, 4, 5]))               # Output: [5, 1, 2, 3, 4]
print(rotate_by_one([9, 8, 7, 6, 4, 2, 1, 3]))       # Output: [3, 9, 8, 7, 6, 4, 2, 1]