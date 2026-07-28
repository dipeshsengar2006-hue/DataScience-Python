# tuple_1 = (1, 2, 4, True)
# tuple_2 = 1., .5, .25, .125
# print("tuple_1: ", tuple_1)
# print("type of tuple_1: ", type(tuple_1))
# print("tuple_2: ", tuple_2)
# print("type of tuple_2: ", type(tuple_2))

# empty_tuple = ()
# print("empty_tuple: ", empty_tuple)
# print("type of empty_tuple: ", type(empty_tuple))
# one_empty_tuple_1 = (1, )
# print("one_empty_tuple_1: ", one_empty_tuple_1)
# print("type of one_empty_tuple_1: ", type(one_empty_tuple_1))
# one_empty_tuple_2 = 1,
# print("one_empty_tuple_2: ", one_empty_tuple_2)
# print("type of one_empty_tuple_2: ", type(one_empty_tuple_2))

''''''
# my_tuple = (1, 10, 100, 1000)

# my_tuple.append(1000) #error
# del my_tuple[0] #error
# my_tuple[1] = -10 #error

''''''
# my_tuple = (1, )
# my_tuple_2 = (2, ) 
# my_new_tuple = my_tuple + my_tuple_2 # add kar dega tuple ko
# print(my_new_tuple)

# my_tuple_2 = ("A", 2, False)
# my_new_tuple = my_tuple_2 * 2  # 2 baar print kar dega
# print(my_new_tuple)

''''''
# my_tuple = (1, 10, 100)
# t1 = my_tuple + (1000, 1000)
# t2 = my_tuple * 3
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

''''''
# ####Example 1 
# tuple_1 = (1, 2, 3) 
# for elem in tuple_1:    
#     print(elem) 
# ####Example 2 
# tuple_2 = (1, 2, 3, 4) 
# print(5 in tuple_2) 
# print(5 not in tuple_2) 
# #Example 3 
# tuple_3 = (1, 2, 3, 4) 
# print(len(tuple_3)) 
# print(5 not in tuple_3) 
# ###Example 4 
# tuple_4 = tuple_1 + tuple_2 
# tuple_5 = tuple_3 * 2 
# print(tuple_4) 
# print(tuple_5)
# print(tuple_4[0]) 
# print(tuple_5[1])

''''''
# my_tuple = tuple((1, 2, "string"))
# print(my_tuple)

# my_list = [2, 4, 6]
# print(my_list) # outputs: [2, 4, 6] 
# print(type(my_list)) # outputs: <class 'list'> 
# tup = tuple(my_list) 
# print(tup) # outputs: (2, 4, 6) 
# print(type(tup)) # outputs: <class 'tuple'>

'''swapping in tupple'''
var = 123
t1 = (1) 
t2 = (2) 
t3 = (3, var) 
t1, t2, t3 = t2, t3, t1 
print(t1, t2, t3)

''''''