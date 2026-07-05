'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push
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

'''for loop ''''''''(when range is known) '''
'''''''''''''''''''''''''''''''''''''''''''''''''''' Break in for loop '''''''''''''''''''''''''''''''''
# print("The break instructions: ");
# for counter in range(1, 6):
#     if counter == 3:
#         break
#     print("Inside the loop. ", counter)
# print("Output the loop. ")

'''''''''''''''''''''''''''''''''''''''''extra for loop questions'''
#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#   print(x)

#for x in "banana":
#   print(x) 

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#   print(x)
#   if x == "banana":
#     break

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#   if x == "banana":
#     break
#   print(x)


#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

#for x in range(6):
#   print(x)

#for x in range(2, 6):
#   print(x)

#for x in range(2, 30, 3):
#   print(x)


#for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")











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