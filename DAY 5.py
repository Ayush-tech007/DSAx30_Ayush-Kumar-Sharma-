# PROBLEM 1

def myAtoi(s: str) -> int:
    # Step 1: Remove leading whitespaces
    s = s.lstrip()

    # Edge case: if string becomes empty after removing spaces
    if not s:
        return 0

    i = 0  # index to track our position in the string
    sign = 1  # default sign is positive
    result = 0  # to store the final number

    # Step 2: Check if the current character is '+' or '-'
    if s[i] == '-':
        sign = -1  # negative number
        i += 1
    elif s[i] == '+':
        i += 1  # keep it positive

    # Step 3: Read digits until a non-digit character is found
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit  # build the number digit by digit
        i += 1

    # Apply the sign to the result
    result *= sign

    # Step 4: Clamp the result to 32-bit signed integer range
    INT_MIN = -2**31      # -2147483648
    INT_MAX = 2**31 - 1   # 2147483647

    if result < INT_MIN:
        return INT_MIN
    elif result > INT_MAX:
        return INT_MAX
    else:
        return result

# Example Test Cases
print(myAtoi("42"))           # Output: 42
print(myAtoi("   -042"))      # Output: -42
print(myAtoi("1337c0d3"))     # Output: 1337
print(myAtoi("0-1"))          # Output: 0
print(myAtoi("words and 987"))# Output: 0



# PROBLEM 2


from itertools import permutations

# Function to calculate the maximum possible overlap between two strings
def overlap(s1, s2):
    max_olap = 0
    # Try all possible suffixes of s1 and check if they match prefixes of s2
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i:] == s2[:i]:
            max_olap = i # update maximum overlap
    return max_olap

# Function to merge two strings with the maximum overlap
def merge(s1, s2):
    olap = overlap(s1, s2)
    return s1 + s2[olap:] # merge by avoiding repeated overlap

# Function to find the minimal merged string from 3 input strings
def minimal_superstring(a, b, c):
    strings = [a, b, c]
    min_string = None

    # Try all permutations (6 total) of the 3 strings
    for perm in permutations(strings):
        # Merge first two strings
        temp = merge(perm[0], perm[1])
        # Then merge with the third
        result = merge(temp, perm[2])
        # Update result if it's smaller or lexicographically earlier
        if (min_string is None or 
            len(result) < len(min_string) or 
            (len(result) == len(min_string) and result < min_string)):
            min_string = result # store the best result
    return min_string

# Example usage
a = "abc"
b = "bca"
c = "aaa"
print("Output:", minimal_superstring(a, b, c)) # Output: "aaabca"

# Another example
a = "ab"
b = "ba"
c = "aba"
print("Output:", minimal_superstring(a, b, c)) # Output: "aba"
