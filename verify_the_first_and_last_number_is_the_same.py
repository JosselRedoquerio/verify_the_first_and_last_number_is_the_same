# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

def first_last_same(numberList):
    print("Provided list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    

# Given lists and print the result
numbers_x = [10, 20, 30, 40, 10]
print("The result is", first_last_same(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print("The result is", first_last_same(numbers_y))