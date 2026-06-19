'''''''''''''''''''''''''''''''''List'''

# numbers = [ 10, 5, 7, 2, 1]
# print(numbers)
# print(type(numbers))

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# #print(numbers[5]) #''error coz list 0 to 4 ki hi hai bass'''

# numbers[0] = 100
# print(numbers)

# numbers = [ 10, 5, 7, 2, 1]
# print("Original list contents: ", numbers)  # printing original list contentents.
# numbers[0] = 111
# print("Original list contents: :", numbers) #current list contents. 
# numbers[1] = numbers[4] # copying value of the fifth element to second.
# print("New list contents: ", numbers)  #printing current list contents.

# print(len(numbers))  # shows number of element in list

# print(numbers)
# print(len(numbers))

# del numbers[1] ''' to delete anyhing = del'''
# print(numbers)  
# print(len(numbers))




# numbers = [111, 7, 2, 1]
# print(numbers[-1])
# print(numbers[len(numbers * -1)])
# numbers = [111, 7, 2, 1, " "]
# print(numbers[-1])

"""""question 1"""
numbers = [ 1, 2, 3, 4, 5]
print(len(numbers))
del numbers[-1]
print(numbers)
x = int(input("enter your replaced number: "))
numbers[int(len(numbers)/2)] = x
print(numbers)