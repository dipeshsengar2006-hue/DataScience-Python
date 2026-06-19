'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add*
# git commit -m "Explaint the commit here"
# git push



'''print("hello")

name = "Dipesh"
profession = "software developer"
experience = 10
print("Hello, I am", name,".I am a ", profession,"professionally.And I have around", experience," years of experience with it!")
'''
'''
x = 5 
print(x,type(x))
x = "Hello World"
print(x,type(x))
x = 20
print(x,type(x))
x = 20.5
print(x,type(x))
x = ["apple", "banana", "cherry"]
print(x,type(x))
x = ("apple", "banana", "cherry")
print(x,type(x))
x = range(6)
print(x,type(x))
x = {"name" : "John", "age" : 36}
print(x,type(x))
x = {"apple", "banana", "cherry"}
print(x,type(x))
x = frozenset({"apple", "banana", "cherry"})
print(x,type(x))
x = True
print(x,type(x))
x = b"Hello"
print(x,type(x))
x = bytearray(5)
print(x,type(x))
x = memoryview(bytes(5))
print(x,type(x))
x = None
print(x,type(x))
'''
'''
print("10 + 2 = ", 10 + 2)
print("10 - 2 = ", 10 - 2)
print("10 * 2 = ", 10 * 2)
print("10 / 2 = ", 10 / 2)
print("10 % 2 = ", 10 % 2)
print("10 // 2 = ", 10 // 2)
print("10 ** 2 = ", 10 ** 2)
'''
'''
x=5
print(x)
x += 3
print(x)
x -= 2
print(x)
x *= 3
print(x)
x /= 2
print(x)
x //= 3
print(x)
x **= 2
print(x)
x = 5
x %= 3
print(x)
x |= 2
print(x)
x ^= 3
print(x)
'''''
'''''
a = 10
b = 20
print("a == b: ", a == b)
print("a == 10: ", a == 10)
print("a != b: ", a != b)
print("a != 10: ", a != 10)
print("a > b: ", a > b)
print("a < b: ", a < b)
print("a <= b: ", a <= b)
print("a >= b: ", a >= b)
print("a >= 10: ", a >= 10)
'''''
'''''
x = 3
print(x < 5 and x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))
'''''
'''''
x = 3
y = 4
print(x is y)
print(x is not y)
'''''
'''''
x = ["Maruti", "BMW"]  # becz x & y are carring diff. address 
y = ["Maruti", "BMW"]
z = x
print(x is y) #identity operator 
print(x is z)
print(y is z)
'''''
'''
x = 10  # 0000 1010
y = 20  # 0001 0100
print(x & y) #0
print(x | y) #30
print(x ^ y)
print(~x)
print(~y)
print(x << 2)    #000 1010 => 0010 1000
print(y << 2)
print(x >> 2)
print(y >> 2)   
'''
# name = input("Enter your name: ")
# print("Hello ", name)
# age = input("Enter your age: ")
# print("Hello ", name, "You are ", age, "Years Old")
# phone = input("Enter your phone no.: ")
# print("Contact Number ", phone)
# email = input("Enter your email: ")
# print("email ", email)

# x = int(input("Enter first value for sum: ")) #typecasting (int lagana starting mai = typecasting specially before + )
# y = int(input("Enter second value for sum: ")) # it is important to both be int or strng 
# z = x + y
# print("sum: ", z)

# x = input("Enter value of x : ")
# y = input("Enter value of y : ")
# z = int(x) + int(y)
# print("sum: ", z)

#'''
# Write a program to calculate hypotenuse between to sides
# p = float(input("Enter value of perpendicular : "))
# b = float(input("Enter value of base : "))
# H = ((p**2 + b**2)**(1/2))
# print("H is : ", H)

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