
'''''if, elif, lse conditions'''
num1 = int(input("enter value of num 1 :"))
num2 = int(input("enter value of num 2 :"))
if num1>num2:            # if num1>num2: larger_num = num1
    larger_num = num1    # else: larger_num = num2
else:
    larger_num = num2
print("The larger number is ", larger_num)


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
