'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Print functions """

# print("hello") # hello
 
# print(5) # 5

# print("Dipesh", "Tilak", "Vinay") # Dipesh Tilak Vinay

# print(True)  #True

# print("India", 5, True)  # Indis 5 True

# print("Dipesh", "Tilak", "Vinay", sep= "/") # Dipesh/Tilak/Vinay
# print("Dipesh", "Tilak", "Vinay", sep= "-") # Dipesh-Tilak-Vinay

# print("Hello")  
# print("World")
#     # Hello 
#     # World
# print("Hello", end=" ")
# print("Wolrd")
    # Hello world


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Data Types (DT) """
"""
1. BASIC TYPES - integer, float, boolean, complex and string
2. CONTAINER TYPES - list, tuples, sets and dictionary
3. USER DEFINED TYPES - Class (we will see this in oops)
"""
## 1.BASIC TYPES
'''Integer'''
#print(4)
#print(1e309)

'''float'''
#print(1.5e204)

'''boolean'''
#print(True)
#print(False)

'''Complex'''
#print(4 + 5j)

'''String'''
#print('India')
#print("India")
#print("""India""")

## 2.CONTAINER TYPES
'''list'''
#print([1, 2, 3, 4, 5]) #[1, 2, 3, 4, 5]

'''tuple'''
#print((1, 2, 3, 4, 5)) #(1, 2, 3, 4, 5)

'''sets'''
#rint({1, 2, 3, 4, 5}) #{1, 2, 3, 4, 5}

'''Dictionary'''
#print({"Name": "Dipesh", "Age": 20, "Gender": "Male"}) #{'Name': 'Dipesh', 'Age': 20, 'Gender': 'Male'}


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Variable """
# in C language we have to declare variable first 
# int  a = 5

#But in python we do direct
#name = 'Dipesh'
#print(name)   # Dipesh

""" Dynamic Typing """
# We dont have to specify what type of Variable is,, it alredy understand by it self (example - python, PHP)
# Jaise C, Java mai variable declare karna padhta hai
""" Static Typing """
# We have to specify what type of Variable is,,,,
# Jaise Python mai variable declare nhi karna padhta

""" Dynamic Binding """
# name = True 
# print(name)  # True 

# name = "wow"
# print(name) # wow

#so yaha 1 hi variable baar baar diff. data type mai change ho jata hai 

""" Static Binding"""
#isme 1 hi variable k aap baar baar alagalag data type nhi de sakte if 1 baar wo int ho gaya then o gaya and if usse thik karna hai toh starting mai jaa kar phele wala change karo 


'''special syntax  (to assin 3 variable at once)'''
#a=3;b=4;c=6
#print(a)
#print(b)
#print(c)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Keywords """
#### aise words jo language apne particular use ke liye le leti hai and fr wo words hum normally use nhi kart sakte to avoid confusions and all 
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
#  'raise', 'return', 'try', 'while', 'with', 'yield']

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Identifiers """
## identifiers are name which is used to idetify variable, functions, Class, module and others 

'''Rules :-'''
#1. start with alphabet or _(underscroll)
#2. 0, _, digits ye beech mai easily use kar sakte hai even double undersroll too 
#3. keywords ko as a identifiers use nhi kar sakte 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Input Functions """
# input()

# input("Apna naam bata")
# # Apna naam bata(Dipesh)

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# result = a + b
# print(result)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Literals """
##Literals are raw data given in variable 
##        Now types of Literals 
#         1. Numeric Literals
#         2. String Literals
#         3. Boolean Literals
#         4. special Literals

''''''''''''''' 1. Numeric Literals '''
# a = 0b1010 #Binary Literal
# b = 100 #Decimal Literal
# c = 0o310 #Octal Literal 
# d = 0x12c # Hexadecimal Literal

'''Float numbers'''
# float_1 = 10.5
# float_2 = 1.5e2
# float_3 = 1.5e-3

'''complex numbers'''
# x = 3.14j or 4 + 3.14j
# print(a, b, c, d)
# print(float_1, float_2, float_3)
# print(x, x.imag, x.real)
#10 100 200 300
#10.5 150.0 0.0015
#3.14j 3.14 0.0

''''''''''''''' 2. string Literals '''
# string = ' python '
# strings = " python "
# multi_strings = """ python """
# #unicode = u"\U001f600\U001f606"#ye emoji ke liye use hota hai 
# raw_str = r" raw \n string "
# print(string)
# print(strings)
# print(multi_strings)
# #print(unicode)
# print(raw_str)

''''''''''''''''''' 3. Boolean '''
# a = True + 4 
# b = False + 5
# print("a:", a)
# print("b:",b)

'''''''''''''''''''4. special litreal '''
# a = None
# print(a)

"""""""""""""""""""""""""""""""""""""""""""""""""""" Operators """
#operators
# 1. Airthmetic Op. 
# 2.Comparison op. 
# 3.Logical op.
# 4.Bitwise op.
# 5.Assignment op.
# 6.Identif op.
# 7.Membership

''''Airthmetic operation '''
# x = 5
# y = 2
# print(x + y) #  7
# print(x - y) #  3
# print(x * y) #  10
# print(x / y) #  2.5
# print(x % y) #  1
# print(x ** y)#  25
# print(x // y) # 2

''''Comparison op.'''
# print(x > y) #  T
# print(x < y) #  F
# print(x >= y) # T
# print(x <= y) # F
# print(x == y) # F
# print(x != y) # T

''''' Logical op.'''
# x = True
# y = False
# print(x or y) #  T
# print(x and y) # F
# print(not x) #   F
# print(not y) #   T    

''''' Bitwise op. '''
# x = 2
# y = 3

# print(x & y) # 2
# 010
# 110
# ---
# 010

# print(x | y) # 3
# print(x >> 2) # 0
# print(x << 3) #24
# print(~x) # -3  

''''' Assignment op.'''
# a=3

# a += 3
# print(a)

# a -= 3
# print(a)

# a *= 3
# print(a)

# a /= 3
# print(a)

# a &= 3
# print(a)

''''' identity op.'''
# a = 3
# b = 3
# print( a is b) # True

# a = "Hello"
# b = "Hello"
# print(a is b) # True

# a =[1, 2, 3, 4, 5]
# b =[1, 2, 3, 4, 5]
# print(a is  b) #False

# a = "Hello - world"
# b = "Hello - world"
# print(a is b) # True  

# x = "Delhi"
# print("D" in x) # True

# b =[1, 2, 3, 4, 5]
# print(2 in b) # True

""""""""""""""""""""""""""""""""""""""""""""""""""""" if- elif - else """
########correct email - dieshsengar@gmail.com
########correct password - 1234

# email  = input("Enter you email: ")
# if "@" in email:
#     password = input("Enter your password: ")
#     if  email == "dieshsengar@gmail.com" and password == '1234':
#         print("Welcome")
#     elif email == "dieshsengar@gmail.com" and password != '1234':
#         print("Password is not valid!")
#         password = input("Enter your password again : ")
#         if password == '1234':
#             print("finally its correct, Welcome")
#         else :
#             print("Still incorrect")
#     else:
#         print("tujh se nhi hoga lala ")
# else:
#     print("Eee tu jaa ree")

""""""""""""""""""""""""""""""""""""""""""""""""""""" indentation """