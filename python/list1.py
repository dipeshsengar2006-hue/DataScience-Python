'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push

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

''' how to print adresss of  variable and variable's number '''
# numbers = [10, 5, 7, 2, 1]
# a = 10

# print("variable a: ", a)
# print("Adress of variable a in integer: ", id(a))
# print("Adress of variable a in integer: ", hex(id(a)))

# print(hex(id(numbers)))
# print(hex(id(numbers[0])))
# print(hex(id(numbers[1])))
# print(hex(id(numbers[2])))

"""""question 1"""
# numbers = [ 1, 2, 3, 4, 5]
# print(len(numbers))
# del numbers[-1]
# print(numbers)
# x = int(input("enter your replaced number: "))
# numbers[int(len(numbers)/2)] = x
# print(numbers)


'''''''append '''
# list = [5, 4, 3, 2, 1]
# print(list)
# print(f'Length of list: {len(list)}')
# list.append(6)
# print(list)
# print(f'Length  of list:{len(list)}')
'''   f' kjSnjshk '    '''# we an use any thing in line with f'' like list, tuple...etc

'''''''''''''''''''''''insert { index, element}'''
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

'''problem '''
# list1 = [1, 2, 3]
# for count in range(len(list1)):
#   print(list1[count])

'''problem '''
# my_list=[]
# for i in range(1,11, 1):
#   my_list.append(i)
# print(my_list)
# '''''''''from while loop'''
# count = 1
# while count<=10:
#   my_list.append(count)
#   count += 1
# print(my_list)

'''problem '''
# my_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(10):
#   my_list[i] += 1
  
# print(my_list)

'''''problem '''
# my_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# sum = 0
# for index in range(len(my_list)):  # or for element in mylist:
#     sum +=  my_list[index]

# print("Sum :", sum)


'''''problem [ copying variable into another variable {swaping number}]'''
# a = 10
# b = 20
# print("a:", a)
# print("b:", b)
# #variable 1 , variable 2 = variable 2 ,variable 1
# a, b = b, a
# print("a:", a)
# print("b:", b)

'''''problem [ copying element into another element {swaping element }]'''
# my_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(my_list)
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print(my_list)

'''''problem '''
# lst = ["D", "F", "a", "Z"]
# lst.sort()

# print(lst)
# print("A" > "a")

'''''problem '''
# a = 3
# b = 1
# c = 2
# lst = [ a, c, b]
# lst.sort()
# print(lst)

'''''problem '''
# a = "A"
# b = "B"
# c = "C"
# d = " "
# lst = [ a, c, b, d]
# lst.reverse()
# print(lst)

'''''problem '''
# a = 1
# b = a
# a = 2
# print(a)
# print(b)
'''''''''''''''but now same problem with list'''
# list_1 = [1]
# list_2 = list_1 
# #list_2 = list_1 ne copy nahi banayi. Dono variables same list ko point kar rahe hain.
# list_1[0] = 2
# print(list_2)

'''now we will copy the element ''' 
# from slicing 
# list_1 = [1]
# list_2 = list_1[:] 
# list_1[0] = 2
# print(list_2)

'''same concept with more example'''
# from slicing 
# list_1 = [1, 2, 3, 4]
# list_2 = list_1[0:2] # n-1 chalta hai ye bhi 
# list_1[0] = 2
# print(list_2)
'''same concept with more example'''
# lst = [10, 8, 6, 4, 2]
# lst_2 = lst[1:3] # n-1
# print(lst_2)

# lst_2 = lst[1:-1]
# print(lst_2)

# lst_2 = lst[-1:1]
# print(lst_2)

""""""""""""""""""""""""" to print asci vale """ # use ord
# print(ord("A"))



'''''problem  slicing'''
# lst = [10, 8, 6, 4, 2]
# del lst[:] # n-1
# print(lst)

'''''problem '''
# lst = [10, 8, 6, 4, 2]
# del lst
# print(lst)
'''''problem '''
# lst = [10, 8, 6, 4, 2]
# print(5 in lst)
# print(5 not in lst)
# print(12 in lst)

'''''problem  finding greatest number '''
# lst = [ 17, 3, 11, 5, 1, 9, 7, 15, 13]
# lst.sort()
# print(lst)
# print("maximum number is : ", lst[-1])

'''''''''''''with logic'''
# my_list = [ 17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# for index in range(len(my_list)): #0. 1. 2. 3. 4. 5. 6. 7. 8
#     # print(index) # for index
#     # print(my_list[index]) # for element 
#     # print(index, "->", my_list[index])
#     if largest < my_list[index]:
#         largest = my_list[index]

# print(largest)
'''''''''''''with logic 2'''
    
# my_list = [ 17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# largest = my_list[0]
 
# for element in my_list:
#     if largest < element:
#         largest = element
   
# print(largest)
''''''''''problem of searching numbers in list'''
# my_list = [ 17, 3, 11, 5, 1, 9, 7, 15, 13]
# found = -1
# for index in range(len(my_list)):
#     if my_list[index] == 5:
#         print("5 is found at ", index)
#         found = index
#         break
#     if found < 0:
#         print("Element not found in the list")
#     else:
#         print("Element is found at :", found)



'''append means last mai add hona '''
'''insert means 2 chizo ke beech or at the begnning kuch add karna '''


# list = [5, 4, 3, 2, 1]
# print(len(list))
# print(list)

# list.append(6)
# print(len(list))
# print(list)

# list.insert(0, 222)
# print(len(list))
# print(list)


'''practice question'''
'''There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
Your task is to:
write a line of code that prints the length of the existing list (Step 1).
write a line of code that removes the last element from the list (Step 2)
write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 3)'''
# hat = [ 1, 2, 3, 4, 5]
# print(len(hat))
# del hat[-1]
# print(hat)
# middle = len(hat) // 2
# hat[middle] = int(input("Enter your number: "))
# print(hat)


'''traversing = puri list ko dekhna and usse print kara dena'''
# list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index in range(len(list)):
#     print(index) # ye index print karayega
#     print(list[index])

# list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index in list:
#     print(index)
'''now traversing by while loop'''
# list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# index = 0 
# while index < len(list):
#     print(list[index])
#     index += 1

'''practice question'''
# list = []
# for index in range(21, 32):
#     list.append(index)   # if we didnt give 21 at start and 0 se print ho jaye toh apn =   list.append(index + 1)
# print(list)

'''practice question'''
# list1 = [10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
# for index in range(len(list1)):
#     list1[index] += 1
# print(list1)

'''practice question'''
# list1 = [10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
# sum = 0
# for index in list1:
#     sum += index
# print("sum is : ", sum)

'''practice question'''
# list1 = [10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
# index = 0
# for abc in list1:
#     print("list1[", index, "]=>", abc)
#     index += 1
'''practice question  swapping'''
# a = 10
# b = 20
# print("a : ", a)
# print("b : ", b)
# print("-------------")
# temp = b
# b = a
# a = temp
# print("a : ", a)
# print("b : ", b)
""" or """
# a, b = b, a
# print("a : ", a)
# print("b : ", b)

'''practice question  swapping in list'''
# list1 = [10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
# print(list1)
# """ swap - 2nd and 5th values"""
# list1[1], list1[4] = list1[4], list1[1]
# print(list1)