'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push
''''''
""" 
*****
*****
*****
*****
*****
"""
# for row in range(6):
#     for stars in range(6):
#         print("*", end=" ")
#     print()

"""
*
**
***
****
*****
"""
# for row in range(1, 6):
#     for stars in range(row):
#         print("*", end=" ")
#     print()

"""
*****
****
***
**
*
"""
# for row in range(5, 0, -1):
#     for stars in range(row):
#         print("*", end=" ")
#     print()

"""
    *
   **
  ***
 ****
*****
"""

# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end=" ")
#     for j in range(i):
#             print("*", end=" ")
#     print()

"""
*****
 ****
  ***
   **
    *
"""
# for i in range(5, 0, -1):
#     for j in range(5 - i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")

#     print()

"""
    *
   ***
  *****
 *******
*********
"""
# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end=" ")
#     for j in range(2*i - 1):
#         print("*", end=" ")
#     print()


'''
*********
 *******
  *****
   ***
    *
'''
# for i in range(5, 0, -1):
#     for j in range(5 - i):
#         print(" ", end=" ")
#     for j in range(2*i - 1):
#         print("*", end=" ")
#     print()


"""
1
12
123
1234
12345
"""
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

"""
1
22
333
4444
55555
""" 
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
#     print() 

"""
1
121
12321
1234321
"""
# for i in range(1, 5):
#    for j in range(i):
#      print("*", end=" ")
#    for j in range(3)

#    print()

"""
*****
*   *
*   *
*   *
*****
"""
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):

#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


"""
*
**
* *
*  *
*****
"""
# n = 5
# for i in range(1, n+1):
#     for j in range(1, n + 1):

#         if j == 1 or j == i or i == n:
#          print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print() 
