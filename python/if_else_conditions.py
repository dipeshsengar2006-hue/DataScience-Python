'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push


'''''if, elif, lse conditions'''
# num1 = int(input("enter value of num 1 :"))
# num2 = int(input("enter value of num 2 :"))
# if num1>num2:            # if num1>num2: larger_num = num1
#     larger_num = num1    # else: larger_num = num2
# else:
#     larger_num = num2
# print("The larger number is ", larger_num)


#num1 = int(input("enter value of num 1 :"))
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

#read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# #choose the largest number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
# #print the result
# print("The largest number is: ", larger_number)


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
# we already giver largest position too n1
largest = n1
if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3
print("Largest number is: ", largest)