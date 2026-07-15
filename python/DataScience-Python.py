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



# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# gpa = float(input('Enter your gpa: '))
# print(name)
# print(type(name))
# print(age)
# print(type(age))
# print(gpa)
# print(type(gpa))

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

# str = "-" * 10
# print(str) 

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
# text = ' Hello python world! '
# print(text.upper())   # HELLO PYTHON WORLD!
# print(text.lower())   # hello python world!
# print(text.title())   # Hello Python World!
# print(text.capitalize()) # hello python world

# #Strip whitespace 
# print(text.strip()) # Hello Python World

# #Search 
# print('pyhton in text')   #True
# print(text.find('python')) #8 (index where found)
# print(text.count('l')) # 3
# str = "hello how are you "
# print(str.capitalized()) #Hello how are you 

# text = ' Hello python World!'

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











'''' # Boolean values, conditional execution, loops, list, processing, logical,  and bitwise operator '''

# print(2 == 2)
# print( 2 == 2.)
# var = 0 # assigning 0 to var
# print(var == 0)
# var = 1 # assigning 1 to var
# print(var == 0)

'''Conditional execution '''
# var = 11
# if var == 11:
#     print("var is 11 🌯")
# print("Hello")


'''''if, elif, lse conditions'''
# num1 = int(input("enter value of num 1 :"))
# num2 = int(input("enter value of num 2 :"))
# if num1>num2:            # if num1>num2: larger_num = num1
#     larger_num = num1    # else: larger_num = num2
# else:
#     larger_num = num2
# print("The larger number is ", larger_num)


# num1 = int(input("enter value of num 1 :"))
# num2 = int(input("enter value of num 2 :"))
# num3 = int(input("enter value of num 3 :"))
# if num1>num2 and num1>num3:
#     larger_num = num1  
# elif num2>num3 and num2>num1:
#     larger_num = num2 
# elif num3>num1 and num3>num2:
#     larger_num = num3 
# print("lergest number is : ", larger_num)

'''shorter way of if-else'''
# if num1>num2 and num1>num3 : larger_num = num1
# elif num2>num3 and num2>num1 : larger_num = num2
# elif num3>num2 and num3>num1 : larger_num = num3

""""  max min way mai """
# largest_num = max(num1, num2, num3)
# lowest_num = min(num1, num2, num3)
# print("lergest number is : ", largest_num)
# print("lowest number is : ", lowest_num)

''''Loops'''

# while True:
#     print("I'm stuck inside loop.")

# largest_num = -999999999
# num = int(input("Enter a number or type -1 to stop: "))

# while num != -1:
#     if num>largest_num:
#         largest_num = num
#     num = int(input("Enter a number or type -1 to stop: "))
# print("The largest number is: ", largest_num)

''' counting even and odd numbers  and stop at 0 and at last print totall even and odd number '''
# num = int(input("enter value of num 1 :"))
# count_even = 0
# count_odd = 0
# while num != 0:
#     if (num %2 == 0):
#         count_even += 1 #count_even = count_even + 1
    
#     elif (num %2 != 0):
#         count_odd += 1

#     num = int(input("Enter a number or type 0 to stop: "))

    
# print("Even Numbers are :", count_even)
# print("Even Numbers are :", count_odd)

# print(bool(5))  # true
# print(bool(1))    # true
# print(bool(-1))  # true
# print(bool(0))  #false always 0 and none are false except null coz null is not to be compare
# print(bool("a"))  # true
# print(bool("b"))   # true
# print(bool(" "))    # true
# print(bool(""))    #false
# print(bool("None"))  #false
# print(bool("NULL"))   # error

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outer the loop.", counter)

# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outer the loop.", counter)

''''''''''''''''''''''''''''''''''''''''''''''''''''''' for loop'''
# for counter in range(10):
#     print("Counter :", counter)

# for counter in range(2, 8):
#     print("Counter :", counter)

"""" hw.1"""
# plant = input()

# if plant == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif plant == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not", plant + "!")

''''hw.2'''
# income = float(input())

# if income <= 85228:
#     tax = income*0.18 -556.02
# else:
#     tax = 14839.02 + 0.32 * (income - 85528)

# if tax < 0:
#     tax = 0 

# print(round(tax))

"""hw.3"""
# year = int(input())

# if year < 1582:
#     print("Not within the Gregorian calendar period")
# else:
#     if year % 4 != 0:
#         print("Common year")
#     elif year % 100 != 0:
#         print("Leap year")
#     elif year % 400 != 0:
#         print("Common year")
#     else:
#         print("Leap year")

'''for loop ''''''''when range is known '''
'''''''''''''''''''''''''''''''''''''''''''''''''''' Break in for loop '''''''''''''''''''''''''''''''''
# print("The break instructions: ");
# for counter in range(1, 6):
#     if counter == 3:
#         break
#     print("Inside the loop. ", counter)
# print("Output the loop. ")

'''''''''''''''''''''''''''''''''''''''''''''''''''' coninue in for loop '''''''''''''''''''''''''''''''''

# print("The break instructions: ");
# for counter in range(1, 6):
#     if counter == 3:
#         continue
#     print("Inside the loop. ", counter)
# print("Output the loop. ")



# largest_num = -999999999
# counter = 0
# while True:
#     num = int(input("Enter a number or type -1 to stop: "))
#     if num == -1:
#         break
#     counter += 1
#     if num > largest_num:
#         largest_num = num
# if counter != -0:
#     print("The largest number is: ", largest_num)
# else:
#     print("You havent enterd ay other 😶")



# largest_num = -999999999
# counter = 0
# num = int(input("Enter a number or type -1 to stop: ")) 

# while num != -1:
# beacuse while ne condition dedi ke -1 hua toh chalega hi nhi toh pura while loop chalega hi nhi even wo uske andar jayega hi nhi 
  #''' if num == -1: '''   #will never execute 
   # '''   continue   '''  #will never execute
   #''' counter += 1  '''   #will never execute
  # ''' if num > largest_num: '''  #will never execute
   # '''    largest_num = num ''' #will never execute
   #''' num = int(input("Enter a number or type -1 to stop: ")) '''     #will never execute 

# if counter:
#     print("The largest number is: ", largest_num)
# else:
#     print("You havent enterd ay other 😶")

""""practice question """
# counter = 1
# while counter < 5:
#   print(counter)
#   counter += 1
# else:
#   print("else: ", counter)
""""practice question """
# counter = 5
# while counter < 5:
#   print(counter)
#   counter += 1
# else:
#   print("else: ", counter)
  
""""practice question """
# for counter in range(5):
#     print(counter)
# else:
#     print("else:", counter)

""""practice question """
# counter = 111
# for counter in range(2, 1):
#   print(counter)
# else:
#   print("else: ", counter)

""""practice question  pyramid"""
# blocks = int(input("Enter the value of blocks you have : "))
# counter = 0
# while(blocks - counter > 0 ):
#     counter += 1
#     blocks = blocks - counter
# print("Height of pyramid is: ", counter)

""""practice question  """
# user_word = input("Enter a word: ")
# user_word = user_word.upper()

# word_without_vowels = ""

# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue

#     word_without_vowels += letter

# print(word_without_vowels)

'''''''''''''''''''''''''''logical expression '''

'''example'''
# print( var > 0)
# print(not( var <= 0))  # true 
'''example'''
# i = 1
# j = not not i # 1

'''git commands '''
# git add*
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
# #print(numbers[5]) #''error'''

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

'''''''''''''''''''''''insert '''
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

"""""""'''''''''''''''''''sorting"""
# list1 = [8, 10, 6, 2, 4]

''' logical operations'''

# i = 1
# j = not not i
# print(i)
# print(j)

'''
Truthy: 1, 2, 3, -1, -20, "a", "Hello", [1, 2], {1:1}, " "
Falsy:  0, "", [], {}, None, Null
'''