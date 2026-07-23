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
def print_grade(name, marks):
    grade = ""
    if marks < 50:
        grade = "D"
    elif marks < 60:
        grade = "C"
    elif marks < 75:
        grade = "B"
    elif marks < 90:
        grade = "A"
    elif marks > 90:
        grade = "A+"
    print(f'Hello {name}, your Grade from {marks} is {grade}!')

print_grade("X", 0)
print_grade("Y", 80)
print_grade("Z", 70)
print_grade("P", 60)
print_grade("Q", 95)
print_grade("R", 55)

