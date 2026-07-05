'''''''''''''''''''''''''''''''''''''''''git commands'''
# git add *
# git commit -m "Explaint the commit here"
# git push


'''''''''''''''''''''''''''''''''''''''''''''''BuBBle sorting'''
# my_list = [8, 10, 6, 2, 4]
# print(my_list)
# count = 0
# for index1 in range(len(my_list)-1):
#     for index in range(len(my_list)-1-index1):
#  #phele jayada chal rha tha coz jo last ke elements hai already sorted unhe bhi check kar raha ttha but ( index - 1) se kam ho gaya 
#         count+=1
#         if(my_list[index] > my_list[index + 1]):
#             my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

# print(my_list)
# print("My program has run for:", count, "times")


''''' now if alrdey sorted ho aur kam chale'''
# my_list = [8, 10, 6, 2, 4]
# swapped = 0
# print(my_list)
# count = 0
# for index1 in range(len(my_list)-1):
#     for index in range(len(my_list)-1-index1):
#  #phele jayada chal rha tha coz jo last ke elements hai already sorted unhe bhi check kar raha ttha but ( index - 1) se kam ho gaya 
#         count+=1
#         if(my_list[index] > my_list[index + 1]):
#             my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
#             swapped = 1
#     if swapped == 0:
#         break

# print(my_list)
# print("My program has run for:", count, "times")

''' now from while loop bubble sorting  '''
# my_list = [8, 10, 6, 2, 4]
# swapped = True  #its a little fake ,we need it to enter the while loop
# count = 0 
# while swapped:
#     swapped = False # no swap so far
#     for i in range(len(my_list)- 1):
#         count += 1
#         if my_list[i] > my_list[i + 1]:
#             swapped = True #a swap occured!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)
# print("loops are rummimg for : ", count,"Times" )
'''''bubble sort from without logic '''
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)


'''''''reverse the list with logic'''
# '''0 = -1'''
# '''1 = -2'''
# '''formula  = { -1 * [index + 1]}'''
# ''' for index = 0 we got value (-1) and for 2  we got (-2)'''
# lst = [5, 3, 1, 2, 4]


# print(lst)
# count = 0
# for index in range(len(lst)//2):
#     count += 1
#     lst[index], lst[-1 * (index +1)] = lst[-1 * (index + 1)], lst[index]
# print(lst)
# print("loops are rummimg for : ", count,"Times" )

'''from 2nd formula'''
# lst = [5, 3, 1, 2, 4]
# print(lst)
# count = 0
# for index in range(len(lst)//2):
#     count += 1
#     lst[index], lst[len(lst) - (index +1)] = lst[len(lst) - (index + 1)], lst[index]
# print(lst)
# print("loops are rummimg for : ", count,"Times" )
''''''''''reverse the list without logic'''
# my_list = [8, 10, 6, 2, 4]
# my_list.reverse()
# print(my_list)
