# PROBLEM 1

def searchInsert(nums, target):
    # Initialize the left and right pointers for binary search
    left = 0
    right = len(nums) - 1 # right starts at the last index

    # Continue searching while the search space is valid
    while left <= right:
        # Find the middle index of the current search space
        mid = (left + right) // 2

        # If the target is found at mid, return the index
        if nums[mid] == target:
            return mid

        # If target is greater, ignore left half by moving left pointer
        elif nums[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half by moving right pointer
        else:
            right = mid - 1

    # If target is not found, left is the index where it should be inserted
    return left

# Test cases:
print(searchInsert([1, 3, 5, 6], 5)) # Output: 2
print(searchInsert([1, 3, 5, 6], 2)) # Output: 1
print(searchInsert([1, 3, 5, 6], 7)) # Output: 4

# PROBLEM 2

def removeElement(nums, val):
    # Initialize a pointer 'k' to keep track of the position to place the next valid element
    k = 0

    # Loop through each element in the array
    for i in range(len(nums)):
        # If the current element is NOT equal to the value to remove
        if nums[i] != val:
            # Place the current element at index k
            nums[k] = nums[i]
            # Move k to the next position
            k += 1
            # This ensures that the first k elements are all valid (not equal to val)

    # After the loop, k will be the count of elements not equal to val
    return k

# Example test cases:
nums1 = [3, 2, 2, 3]
k1 = removeElement(nums1, 3)
print(k1, nums1[:k1])  # Output: 2, [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
k2 = removeElement(nums2, 2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 3, 0, 4] or any other order with those numbers