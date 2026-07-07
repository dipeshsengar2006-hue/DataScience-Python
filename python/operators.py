'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push


# ● Variable  - myOfficialName
# ● Function  - myOfficialName()
# ● Class     - MyOfficialName
# ● Object    - myOfficialNameObj  
# ● Constants- MY_OFFICIAL_NAME

'''Python Data types for a variable'''
# Text Type:      - str
# Numeric Types:  - int, float, complex 
# Sequence Types: - list, tuple, range 
# Mapping Type:   - dict
# Set Types:      - set, frozenset
# Boolean Type:   - bool
# NoneType:       - NoneType

'''''''Python supports these operator types:'''
# ○ Arithmetic Operators 
# ○ Assignment operators 
# ○ Comparison operators 
# ○ Logical operators 
# ○ Identity operators 
# ○ Membership operators 
# ○ Bitwise operators

''''printing Hello '''
#print("hello")

'''● Precedence of the Arithmetic operators '''
# ○ P – Parentheses 
# ○ E – Exponentiation 
# ○ M – Multiplication (Multiplication and division have the same precedence) 
# ○ D – Division 
# ○ A – Addition (Addition and subtraction have the same precedence) 
# ○ S – Subtraction 
# ○ 1 + 3 - 5 / 7 * 3 (2/3)

'''operators'''
# name = "Dipesh"
# profession = "software developer"
# experience = 10
# print("Hello, I am", name,".I am a ", profession,"professionally.And I have around", experience," years of experience with it!")
# '''
# '''
# x = 5 
# print(x,type(x))
# x = "Hello World"
# print(x,type(x))
# x = 20
# print(x,type(x))
# x = 20.5
# print(x,type(x))
# x = ["apple", "banana", "cherry"]
# print(x,type(x))
# x = ("apple", "banana", "cherry")
# print(x,type(x))
# x = range(6)
# print(x,type(x))
# x = {"name" : "John", "age" : 36}
# print(x,type(x))
# x = {"apple", "banana", "cherry"}
# print(x,type(x))
# x = frozenset({"apple", "banana", "cherry"})
# print(x,type(x))
# x = True
# print(x,type(x))
# x = b"Hello"
# print(x,type(x))
# x = bytearray(5)
# print(x,type(x))
# x = memoryview(bytes(5))
# print(x,type(x))
# x = None

'''○ Arithmetic Operators'''
# print(x,type(x))
# '''
# '''
# print("10 + 2 = ", 10 + 2)
# print("10 - 2 = ", 10 - 2)
# print("10 * 2 = ", 10 * 2)
# print("10 / 2 = ", 10 / 2)
# print("10 % 2 = ", 10 % 2)
# print("10 // 2 = ", 10 // 2)
# print("10 ** 2 = ", 10 ** 2)

'''○ Assignment operators'''
# x=5
# print(x)
# x += 3
# print(x)
# x -= 2
# print(x)
# x *= 3
# print(x)
# x /= 2
# print(x)
# x //= 3
# print(x)
# x **= 2
# print(x)
# x = 5
# x %= 3
# print(x)
# x |= 2
# print(x)
# x ^= 3
# print(x)

'''○ Comparison operators'''
# a = 10
# b = 20
# print("a == b: ", a == b)
# print("a == 10: ", a == 10)
# print("a != b: ", a != b)
# print("a != 10: ", a != 10)
# print("a > b: ", a > b)
# print("a < b: ", a < b)
# print("a <= b: ", a <= b)
# print("a >= b: ", a >= b)
# print("a >= 10: ", a >= 10)

'''○ Logical operators '''''
# x = 3
# print(x < 5 and x < 10)
# print(x < 5 or x < 4)
# print(not(x < 5 and x < 10))

'''○ Identity operators '''''

# x = 3
# y = 4
# print(x is y)
# print(x is not y)
'''○ Membership operators '''
# x = ["Maruti", "BMW"]  # becz x & y are carring diff. address 
# y = ["Maruti", "BMW"]
# z = x
# print(x is y) #identity operator 
# print(x is z)
# print(y is z)
'''○ Bitwise operators '''
# x = 10  # 0000 1010
# y = 20  # 0001 0100
# print(x & y) #0
# print(x | y) #30
# print(x ^ y)
# print(~x)
# print(~y)
# print(x << 2)    #000 1010 => 0010 1000
# print(y << 2)
# print(x >> 2)
# print(y >> 2)   



'''practice question'''
# name = input("Enter your name: ")
# print("Hello ", name)
# age = input("Enter your age: ")
# print("Hello ", name, "You are ", age, "Years Old")
# phone = input("Enter your phone no.: ")
# print("Contact Number ", phone)
# email = input("Enter your email: ")
# print("email ", email)

'''practice question'''
# x = int(input("Enter first value for sum: ")) #typecasting (int lagana starting mai = typecasting specially before + )
# y = int(input("Enter second value for sum: ")) # it is important to both be int or strng 
# z = x + y
# print("sum: ", z)
'''practice question'''
# x = input("Enter value of x : ")
# y = input("Enter value of y : ")
# z = int(x) + int(y)
# print("sum: ", z)

'''practice question'''
''' Write a program to calculate hypotenuse between to sides'''
# p = float(input("Enter value of perpendicular : "))
# b = float(input("Enter value of base : "))
# H = ((p**2 + b**2)**(1/2))
# print("H is : ", H)
'''practice question'''
# print("+ - - - - - - - - - - +")
# print("|                     |")
# print("|                     |")
# print("|                     |")
# print("|                     |")
# print("|                     |")
# print("|                     |")
# print("+ - - - - - - - - - - +")

# print("+" + "-" * 10 + "+")
# print(("|" + " " * 10 + "|\n" ) * 5,end="")
# print("+" + "-" * 10 + "+")

''' Strings'''
# city = 'BHOPAL' 
# #       012345   <--- index positions 
# #      -6-5-4-3-2-1  <---- negative indices(from end to start )

# print(city[0])   #B  (first charachter)
# print(city[-6])  #B
# print(city[2])   #O
# print(city[-1])  #L
# print(city[-3])  #P



"""""tools or functions in pythons"""

# #Strip whitespace 
# print(text.strip()) # Hello Python World

# #Search 
# print('pyhton in text')   #True
# print(text.find('python')) #8 (index where found)
# print(text.count('l')) # 3
# str = "hello how are you "
# print(str.capitalized()) #Hello how are you 

# text = ' Hello python world! '
# print(text.upper())   # HELLO PYTHON WORLD!
# print(text.lower())   # hello python world!
# print(text.title())   # Hello Python World!
# print(text.capitalize()) # hello python world

# #Replace 
# print(text.replace('Phython', 'AI'))   # Hello AI World!

# #Split and join 
# csv = 'Rahul,22,Bhopal,Engineer'
# parts = csv.split(',')  # ['Rahul, '22', 'Nhopal', 'Engineer'
# print("parts: ",parts)
# print(parts[0])
# rejoined = ' | '.join(parts) # 'Rahul | 22 | Bhopal | Engineer'
# print("rejoined: ", rejoined)

# #check content
# print('hello123'.isalnum())  #True - all letters/difits
# print('hello123*'.isalnum())  ##True - all letters/difit
# print('12345'.isdigit())  # True - all digits
# print('Python'.isalpha())  # True - all letters
# print(' '.isspace())  # True - all spaces

# #start/end check
# email = 'student@gmail.com'
# #a@b.c
# print(email.endswith('.com')) #True
# print(email.startswith('stu')) #True

# name, marks, rank = 'Anita', 92.567, 3
# print(name, marks, rank)

# #Basic
# print(f'Hello, {name}!')

# #Formate numbers
# print(f'Marks: {marks:.2f}')  #92.57(2 decimal places)
# print(f'Marks: {marks:.0f}')  #93   (rounded)
# print(f'Count: {1000000:,}')  #1,00,000 (comma seperator)

# #Padding and aligment
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}') #left/right align
# #Anita            |          92.57|Rank:3
# #ye <15 = 15 character jis side muh khula hai uss side se lega same concept  >8 
# name = "Aditya Gupta"
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')  #left/right align

# #Expression inside {}
# price, gst, = 500, 0.18
# print(f'price:Rs.{price}   | GST:Rs.{price*gst:.2f}   | Total:Rs.{price*(1+gst):.2f}')
