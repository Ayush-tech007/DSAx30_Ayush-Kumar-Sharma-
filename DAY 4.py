# PROBLEM 1

def is_subsequence_sum(nums, k):
    # We use a helper function with backtracking to try all combinations of subsequences
    def backtrack(index, current_sum):
        # If the current sum equals the target, return True
        if current_sum == k:
            return True
        # If we reach the end of the array or current sum exceeds target, stop this path
        if index == len(nums) or current_sum > k:
            return False

        # Choice 1: Include the current number in the sum
        if backtrack(index + 1, current_sum + nums[index]):
            return True
        # Choice 2: Exclude the current number from the sum
        if backtrack(index + 1, current_sum):
            return True
        
        # If neither choice led to a valid sum, return False
        return False

    # Start from index 0 and sum 0
    return backtrack(0, 0)


# Test case 1
nums1 = [1, 2, 3, 4, 5]
k1 = 8
print("Yes" if is_subsequence_sum(nums1, k1) else "No") # Output: Yes

# Test case 2
nums2 = [4, 3, 9, 2]
k2 = 10
print("Yes" if is_subsequence_sum(nums2, k2) else "No") # Output: No.


# PROBLEM 2

def subsets(nums):
    result = [] # This will store all subsets

    # Helper function using backtracking to generate subsets
    def backtrack(start, current_subset):
        # Append the current subset to the result (we make a copy to avoid reference issues)
        result.append(current_subset[:])

        # Loop through the remaining elements starting from 'start' index
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current_subset.append(nums[i])

            # Recurse to continue building the subset with the next elements
            backtrack(i + 1, current_subset)

            # Backtrack: remove the last element added to try other combinations
            current_subset.pop()

    # Start the recursion with an empty subset starting from index 0
    backtrack(0, [])

    return result


# Test case 1
nums1 = [1, 2, 3]
print(subsets(nums1)) # Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

# Test case 2
nums2 = [0]
print(subsets(nums2)) # Output: [[], [0]]