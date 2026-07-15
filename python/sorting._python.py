'''''''''''''''''''''''''''''''''''''''''git commands'''
# git add *
# git commit -m "Explaint the commit here"
# git push


'''''''''''''''''''''''''''''''''''''''''''''''BuBBle sorting'''
# my_list = [8, 10, 6, 2, 4]
# print(my_list)
# count = 0
# for index1 in range(len(my_list)-1):                  #4
#     for index in range(len(my_list)-1-index1):        #4 (1, 2, 3, 4) ==> 16
#  #phele jayada chal rha tha coz jo last ke elements hai already sorted unhe bhi check kar raha ttha but ( index - 1) se kam ho gaya 
#         count+=1
#         if(my_list[index] > my_list[index + 1]):
#             my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

# print(my_list)
# print("My program has run for:", count, "times")  #10 times 


''''' now if alrdey sorted ho aur kam chale'''
# my_list = [1, 2, 3, 4, 5, 6]
# swapped = False
# print(my_list)
# count = 0
# for index1 in range(len(my_list)-1):
#     for index in range(len(my_list)-1-index1): #phele jayada chal rha tha coz jo last ke elements hai already sorted unhe bhi check kar raha ttha but ( index - 1) se kam ho gaya 
#         if(my_list[index] > my_list[index + 1]):
#             my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
#             swapped = True
#         count+=1
#     if not swapped:
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

# lst = ["D", "F", "A", "Z"]
# lst.sort()  """or""" #print(sorted(lst))
# print(lst)
"""in & not in membership operator"""
# lst = [0, 3, 12, 8, 2]
# print(5 in lst)       #False
# print(5 not in lst)   #True
# print(12 in lst)      #True

"""largest element"""
# lst = [17, 3, 11, 5, 1, 9, 7, 15, 13]

'''find specific element'''
#lst = [17, 3, 11, 5, 1, 9, 7, 15, 13]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""List Comprehention"""
# row = []
# for x in range(8):
#     row.append("WHITE_PAWN")
# print(row)
"""but in list Comprehention"""""
# row = ["WHITE_PAW" for x in range(8)]
# print(row)

"""square list Comprehention """
# square = [x ** 2 for x in range(10)]
# print(square) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#'"""""'' 0**2, 1**2, 2**2, 3**2.........9**2'''

"""2 ki power  list Comprehention"""
# twos = [ 2 ** x for x in range(8)]  
# print(twos) #[1, 2, 4, 8, 16, 32, 64, 128]
##''' 2**0, 2**1, 2**2, 2**3.........2**9'''

"""odd list Comprehention"""
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# odds = [x for x in square if x % 2 != 0]
# print(odds) # [1, 9, 25, 49, 81]

"""list of list Comprehention"""
board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
print(board)