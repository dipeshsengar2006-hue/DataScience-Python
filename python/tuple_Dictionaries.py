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
# var = 123
# t1 = (1, ) 
# t2 = (2, )
# t3 = (3, var)
# t1, t2, t3 = t2, t3, t1 
# print(t1, t2, t3)

''''''
# dictionary = {
#     "cat": "chat", 
#     "dog": "chien", 
#     "horse": "cheval"   
#     } 
# phone_numbers = {
#     'boss': 5551234567, 
#     'Suzy': 22657854310
#     } 
# empty_dictionary = {}
# print("dictionary: ", dictionary)
# print("type(dictionary): ", type(dictionary))  
# print("phone_numbers: ",phone_numbers) 
# print("type(phone_numbers): ",type(phone_numbers)) 
# print("empty_dictionary: ", empty_dictionary)
# print("type(empty_dictionary): ", type(empty_dictionary)) 

# '''1 - 1 element access '''

# print(dictionary["cat"])
# print(dictionary["horse"])

# '''we cant use direct key word without data type  '''
# ##example
# cat = "catkey"
# dog = "Dog"

# my_dictionary = {
#     cat: "cat",
#     dog: "Dog"
#  }
# print(my_dictionary)
# print(my_dictionary[cat])# it will gonna work 
'''it is user friendly toocoz in dictionary we can do anything inside { } & it is implicit '''

# dictionary = {
#                 "cat": "chat", 
#                 "dog": "chien", 
#                 "horse": "cheval"   
#              } 
# keys = ["cat", "lion", "horse"]

# for key in keys:
#     if key in dictionary:
#         print(key, "->", dictionary[key])
#     else:
#         print(key, "is not  in dictionary")

''''''
# dictionary = {
#                 "cat": "chat", 
#                 "dog": "chien", 
#                 "horse": "cheval",
#                  1:"One"   
#              } 
# for key in dictionary.keys():
#     print(key)
#     print(dictionary[key])

    # if key in dictionary:
    #     print(key, "->", dictionary[key])
    # else:
    #     print(key, "is not in dictionary")

'''items()'''
# dictionary = {
#                 "cat": "chat", 
#                 "dog": "chien", 
#                 "horse": "cheval",
#                  1:"One"   
#              } 
# print(dictionary.items())
# print(type(dictionary.items()))

# for english, french in dictionary.items():
#     print(english, "->", french)
'''values()'''

# for french in dictionary.values():
#     print(french)

'''copy() or add with refrence like change 1 will change 2 '''
# pol_eng_dictionary = {

#     "zamek": "castle",

#     "woda": "water",

#     "gleba": "soil"

# }
# pol_eng_dictionary_copy = pol_eng_dictionary
# pol_eng_dictionary_copy2 = pol_eng_dictionary.copy()

# print(pol_eng_dictionary)
# print(pol_eng_dictionary_copy)
# print(pol_eng_dictionary_copy2)
 
# pol_eng_dictionary["One"] = 1
# print(pol_eng_dictionary)
# print(pol_eng_dictionary_copy)
# print(pol_eng_dictionary_copy2)

# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item) 
# print("pol_eng_dictionary: ", pol_eng_dictionary)
# del pol_eng_dictionary["zamek"]
# print("pol_eng_dictionary: ", pol_eng_dictionary)

'''CRUD = create | Retrive | Upadte | Delete {list, tuple, dictionary}'''


'''
30 julyyyyyyyyyy
'''
dictionary = {}
while True:
    name = input("Enter Student's Name:")
    if name != "":
        mark = float(input(f"Enter {name}'s Score"))
        if name not in dictionary:
            dictionary.update({name:(mark,)})
        else:
            dictionary[name] = dictionary[name] + (mark, )
    else:
        break
for name, marks in dictionary.items():
    sum = 0 
    for mark in marks:
        sum += mark
    print(f"{name}'s Average score is: {sum/len(marks)}")