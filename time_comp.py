#Constants

#Assignment
x = 7   
y = 3

#Math Operations
add = x + y
sub = x - y

#comparison 
a == b
a > b

#===================== Logrithmic Time Complexity 
#Binary Search
#Time Complexity: O(log n)
#Space Complexity: O(1)

def binary_search(arr, target):
    # Initialize the starting and ending indices of the array
    start = 0
    end = len(arr) - 1
    
    # Repeat the search until the start index is less than or equal to the end index
    while start <= end:
        # Calculate the middle index of the array
        mid = (start + end) // 2
        
        # Check if the middle element is equal to the target
        if arr[mid] == target:
            return mid
        # If the middle element is greater than the target, search the left half of the array
        elif arr[mid] > target:
            end = mid - 1
        # If the middle element is less than the target, search the right half of the array
        else:
            start = mid + 1
    
    # Return -1 if the target is not found in the array
    return -1

#===================== Linear Time Complexity

#Linear Search
#Time Complexity: O(n)
#Space Complexity: O(1)

# example 1
def double_even_numbers(numbers):
    # Initialize an empty list to store the doubled even numbers
    even_numbers = []
    
    # Iterate over each number in the input list
    for num in numbers: #for loops indicated linear time complexity
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, double it and add it to the even_numbers list
            even_numbers.append(num * 2)
    
    # Return the list of doubled even numbers
    return even_numbers
# example 2
def double_even_numbers(numbers):
    # Initialize an empty list to store the doubled even numbers
    even_numbers = []
    
    # Iterate over each number in the input list
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, double it and add it to the even_numbers list
            even_numbers.append(num * 2)
    
    # Return the list of doubled even numbers
    return even_numbers
def highest(scores):
    current_highest = 0
    for score in scores:
        if score > current_highest:
            current_highest = score

#======================= Linear Logrithmic Time Complexity

#.sort() method
#.sorted() function

#creates the highest time complexity

def highest(scores):
    # Sort the list of scores in descending order
    scores.sort() #.sort() 
    
    # Return the highest score
    return scores[-1]

#======================= Quadratic Time Complexity

#nest linear operations
# Define a function named 'squad' that takes one parameter 'alias'
def squad(alias):
    # Loop through each element in 'alias'
    for num in alias:
        # Print the current element in the outer loop
        print("outter:", num)
        # Loop through each element in 'alias' again for the inner loop
        for num2 in alias:
            # Print the current element in the inner loop
            print("inner:", num2)

# Create a list of integers
alist = [1, 2, 3, 4, 5]
# Call the 'squad' function with 'alist' as the argument
squad(alist)

# Define a function named 'highest_count' that takes one parameter 'alist'
def highest_count(alist):
    # Initialize variables to keep track of the highest count and the corresponding number
    highest_counter = 0
    highest_num = 0

    # Loop through each element in 'alist'
    for num in alist:
        # Initialize a counter for the current number
        count = 0
        # Loop through each element in 'alist' again
        for num2 in alist:
            # Check if the count of the current number is greater than the highest count recorded
            if alist.count(num) > highest_counter:
                # Update the highest number and the highest count
                highest_num = num
                highest_counter = alist.count(num)

        # Return the number with the highest count and the count itself
        return highest_num, highest_counter

#================== Dictionary Time Complexity






