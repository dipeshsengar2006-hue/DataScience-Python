'''''''''''''''''''''''''''''''''''''''''git commands'''
# git add *
# git commit -m "Explaint the commit here"
# git push


'''''''''''''''''''''''''''''''''''''''''''''''BuBBle sorting'''
my_list = [8, 10, 6, 2, 4]
print(my_list)
count = 0
for index1 in range(len(my_list)-1):
    for index in range(len(my_list)-1-index1):
 #phele jayada chal rha tha coz jo last ke elements hai already sorted unhe bhi check kar raha ttha but ( index - 1) se kam ho gaya 
        count+=1
        if(my_list[index] > my_list[index + 1]):
            my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

print(my_list)
print("My program has run for:", count, "times")