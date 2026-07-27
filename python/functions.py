'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push


''' functions syntax '''
# def function_name():
#     function body

''' functions  example'''
# def message():
#     print("Enter a value: ")  # ''' ye after function hai'''
#     a = int(input())
#     print(a)

# message()
# message()
# message()

# print("Enter a value: ")  ''' ye before function hai'''
# a = int(input())
# print(a)
# print("Enter a value: ")
# b = int(input())
# print(b)
# print("Enter a value: ")
# c = int(input())
# print(c)

''' functions  example'''
# def message():
#     print("Enter a next value: ")

# print("We start here. ")
# message()
# print("the end is here.")

'''cant define function before making it '''
# message()
# def message():
#     print("Enter a next value: ")

# print("We start here. ")
# message()
# print("the end is here.")

''' functions  example'''
# def message():
#     print("Enter a value: ")
#     return 
#     a = int(input)
# a = message()
#     # Enter a value
# print(message())
#     # Enter a value 
#     # None (coz wo message ki value bhi print kar raha hai)
# message()
    # Enter a value: 
'''function Argument '''
# def hi(num):    # parameter
#     print("hi")
# hi(5)           # argument

'''function Argument question'''
# def hello(n):                   #defining a function
#     print("Hello,", n)          # body of the function 

# name = input("Enter your name: ")
# hello(name)                     # calling the function

'''function parametrized question'''
# def message(number):
#     print("Enter a number: ", number)

# message(1)

'''function parametrized question'''
# def message(num):
#     print("number:", number)
#     print("num:", num)

# number = 1234
# message(1)
# print(number)

'''function parametrized question'''
# def message(what, number):
#     print("Enter", what, "number", number)

# message("telephone", 11)
# message("price", 5)
# message("number", "number")

'''function parametrized question'''
# def print_grade(name, marks):
#     grade = ""
#     if marks < 50:
#         grade = "D"
#     elif marks < 60:
#         grade = "C"
#     elif marks < 75:
#         grade = "B"
#     elif marks < 90:
#         grade = "A"
#     elif marks > 90:
#         grade = "A+"
#     print(f'Hello {name}, your Grade from {marks} is {grade}!')

# print_grade("X", 0)
# print_grade("Y", 80)
# print_grade("Z", 70)
# print_grade("P", 60)
# print_grade("Q", 95)
# print_grade("R", 55)

'''
24 july reh gyi class
'''

'''scope in function (like nickname) '''
'''' jo bhar define hai Global and jo andar wo local'''
# def scope_test():
#     x = 123
# scope_test()
# #print(x)

''''''
# def my_function():
#     var = 2
#     print("Do I KNOW THAT VARIABLE?", var)
# var = 1
# my_function()
# print(var)

''''''
# var = 2
# def mult_by_var(x):
#     return x * var
# print(mult_by_var(7))

# def mult(x):
#     var = 5  #shadow var inn local scope
#     return x * var 
# print(mult(7))

''''''
# def adding(x):
#     var = 7
#     return x + var
# print(adding(4))   #outputs: 11
# print(var) ''' error, coz var is defined in adding functions local scope'''

'''global funtion local ko bhi global n=bana deta hai coxz of global keyword'''
# def my_function():
#     global var
#     var = 2
#     print("Do I KNOW that variable? ", var)

# var = 1
# my_function()
# print(var)

''''''
# var = 2
# print(var) #2

# def return_var():
#     global var
#     var = 5
#     return var

# print(return_var()) #5
# print(var) #5
''''''
#yes we can change argument in 
# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)

# var = 1
# my_function(var)
# print(var)

''''''
# def my_function(my_list_1):
#     print("Print #1:", my_list_1) # local coz andar define hua hai 
#     print("Print #2:", my_list_2) # Global coz ye aage chalkar bhar define hua hai 
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)#local
#     print("Print #4:", my_list_2)#global

# my_list_2 = [2, 3] # Global list
# my_function(my_list_2)
# print("Print #5:", my_list_2)
''''''
def my_function(my_list_1, v):
    print("Print #1:", my_list_1) # local coz andar define hua hai 
    print("Print #2:", my_list_2) # Global coz ye aage chalkar bhar define hua hai 
    print("v:", v)
    print("var:", var)
    del my_list_1[0]
    my_list_1.append(4)
    del v
    print("Print #3:", my_list_1)#local
    print("Print #4:", my_list_2)#global

my_list_2 = [2, 3] # Global list
var = 2
my_function(my_list_2, var)
print("Print #5:", my_list_2)