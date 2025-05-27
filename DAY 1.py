# PROBLEM 1

# Function to print the pattern for a given integer N
def print_pattern(N):
    # Calculate the size of the square pattern, which is (2*N - 1)
    size = 2 * N - 1

    # Loop through each row of the pattern
    for i in range(size):
        # Loop through each column of the pattern
        for j in range(size):
            # For each cell (i, j), we find the minimum distance from the edges
            # This determines the layer (concentric square) the cell belongs to
            # The value to be printed is N minus this minimum distance
            min_dist = min(i, j, size - 1 - i, size - 1 - j)
            value = N - min_dist

            # Print the value with a space, end=" " ensures output stays on the same line
            print(value, end=" ")
        
        # After each row, print a newline to move to the next row
        print()

# Example usage:
print("Pattern for N = 3:")
print_pattern(3)

print("\nPattern for N = 6:")
print_pattern(6)


# PROBLEM 2

# Function to print the required pattern
def print_pattern(N):
    # Loop through rows from 1 to N
    for i in range(1, N + 1):
        # Initialize an empty string to store each row
        row = ''
        
        # First part: Add increasing characters from 'A' to the i-th letter
        for j in range(0, i):
            # Convert number to corresponding uppercase alphabet using chr() and ord()
            row += chr(ord('A') + j)
        
        # Second part: Add decreasing characters from (i-2)-th to 0-th letter
        for j in range(i - 2, -1, -1):
            row += chr(ord('A') + j)
        
        # Print the constructed row
        print(row)

# Example usage
N = 3
print("Pattern for N = 3:")
print_pattern(N)

print("\nPattern for N = 6:")
N = 6
print_pattern(N)


# PROBLEM 3

# Importing permutations function from itertools module
from itertools import permutations

# Prompt the user to enter a number between 2 and 5
n = int(input("Enter any number from 2 to 5 (both inclusive): "))

# Check if the input is within the allowed range
if 2 <= n <= 5:
    # Create a list of digits from 1 to n
    digits = list(range(1, n + 1))

    # Generate all possible permutations of the digits
    all_combinations = list(permutations(digits))

    # Loop through each combination
    for combo in all_combinations:
        # Join the digits with a space and print
        print(' '.join(map(str, combo)))

    # Print the total number of combinations
    print("Total number of combinations:", len(all_combinations))
else:
    # Print an error message for invalid input
    print("Invalid input! Please enter a number between 2 and 5.")


# PROBLEM 4

# Function to determine if a number is a happy number
def is_happy(n):
    # Set to store numbers we’ve seen to detect cycles
    seen = set()

    # Continue until n becomes 1 or a cycle is detected
    while n != 1:
        # If we've already seen this number, a loop is happening — not a happy number
        if n in seen:
            return False
        
        # Add the current number to the seen set
        seen.add(n)

        # Calculate the sum of the squares of the digits
        sum_of_squares = 0
        for digit in str(n):  # Convert the number to string to access each digit
            sum_of_squares += int(digit) ** 2  # Square each digit and add to the sum

        # Update n to the new value (sum of squares)
        n = sum_of_squares

    # If we exited the loop because n is 1, it’s a happy number
    return True

# Example usage
num = int(input("Enter a number to check if it is a happy number: "))

# Check and print result
if is_happy(num):
    print(f"{num} is a Happy Number!")
else:
    print(f"{num} is NOT a Happy Number.")


# PROBLEM 5

# Function to check whether a number is a Kaprekar number
def is_kaprekar(n):
    # Step 1: Square the number
    sq = n ** 2
    str_sq = str(sq)  # Convert square to string to split
    
    # Step 2: Determine the position to split the square string
    len_sq = len(str_sq)
    for i in range(1, len_sq + 1):
        # Split into two parts: left and right
        left = str_sq[:len_sq - i]  # Left part
        right = str_sq[len_sq - i:]  # Right part

        # Convert parts to integers (treat empty string as 0)
        left_num = int(left) if left else 0
        right_num = int(right)

        # Step 3: Add both parts and check if equal to original number
        if left_num + right_num == n:
            return True  # It is a Kaprekar number
    
    return False  # Not a Kaprekar number

# Input from user
p = int(input("Enter the lower bound (p): "))
q = int(input("Enter the upper bound (q): "))

# Check input constraints
if 0 < p < q < 5000:
    kaprekar_numbers = []

    # Iterate through the range
    for i in range(p, q + 1):
        if is_kaprekar(i):
            kaprekar_numbers.append(i)
    
    # Output the results
    print("\nKaprekar numbers between", p, "and", q, "are:")
    for num in kaprekar_numbers:
        print(num)

    print("Total number of Kaprekar numbers:", len(kaprekar_numbers))
else:
    print("Invalid input! Make sure 0 < p < q < 5000.")