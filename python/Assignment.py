'''''''''''''''''''''''''''''''''''''''''git commands '''
# git add *
# git commit -m "Explaint the commit here"
# git push



'''Assignment Question: 1'''

''' Write a program that utilizes the concept of conditional execution, takes a string as input, and:
prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen 
if the inputted string is "Spathiphyllum" (upper-case)prints "No, I want a big Spathiphyllum!" 
if the inputted string is "spathiphyllum" (lower-case)prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input. '''
# plant = input()
# if plant == "spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif plant == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")


'''Assignment Question: 2'''

'''Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. 
The people paid taxes, of course – their happiness had limits. The most important tax, 
called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents 
(this was what they called tax relief)if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents,
plus 32% of the surplus over 85,528 thalers.Your task is to write a tax calculator.
It should accept one floating-point value: the income.Next, it should print the calculated tax, rounded to full thalers. 
There's a function named round() which will do the rounding for youNote: this happy country never returned any money to its citizens. 
If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.'''
# income = float(input("Enter ypur income:"))
# if income <= 85528:
#     tax = (0.18 * income) - 556.02
#     if tax < 0:
#         print(tax = 0)
# elif income > 85528:
#     tax = 14839.02 + 0.32 * (income - 85528)
# print(round(tax))



'''Assignment Question: 3'''

'''As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
if the year number isn't divisible by four, it's a common year;otherwise, if the year number isn't divisible by 100, it's a leap year;otherwise, 
if the year number isn't divisible by 400, it's a common year;otherwise, it's a leap year.Look at the code in the editor – it only reads a year number, '
'and needs to be completed with the instructions implementing the test we've just described.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.
#question '''

# year = int(input("Enter you year: "))
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
    
'''Assignment Question: 4'''

"""Do you know what Mississippi is? 
It's the name of one of the states and rivers in the United States.'
' The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). '
'It's so long that a single drop of water needs 90 days to travel its entire length!
The word Mississippi is also used for a slightly different purpose: to count mississippily.
If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.
The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and 
therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time!
It's often used by children playing hide-and-seek to make sure the seeker does an honest count.
Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. 
Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"   """

# for i in range(1, 6):
#     print(i, "Mississippi")

# print("Ready or not, here I come!")

 
'''Assignment Question: 5'''

'''You must design the (ugly) vowel eater! Write a program that uses:
1. a for loop;
2. the concept of conditional execution (if-elif-else)
3. the continue statement.
Your program must:
1. ask the user to enter a word
2. use user_word = user_word.upper() to convert the word entered by the user to upper case; 
we'll talk about string methods and the upper() method very soon - don't worry;
3. use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
4. ⁠assign the uneaten letters to the word_without_vowels variable and print the variable to the screen. '''

# x = input()
# word_without_vowels = ""
# x = x.upper()
# for i in range(len(x)):
#     if x[i] in "AEIOU":
#         continue
#     word_without_vowels += x[i]
# print(word_without_vowels)



'''Assignment Question: 6'''

''' Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. 
The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:
Your task is to write a program which reads the number of blocks 
the builders have, and outputs the height of the pyramid that can 
be built using these blocks.
Note: the height is measured by the number of fully completed layers – 
if the builders don't have a sufficient number of blocks and cannot 
complete the next layer, they finish their work immediately.'''

# blocks = int(input("Enter the number of blocks: "))
# height = 0 
# layer = 1
# while blocks >= layer:
#     blocks = blocks - layer
''''' #imagine 10 blocks u have
     # Tumne 1 block use kar diya.
     # Ab kitne bache?
     # 10 - 1 (layers) = 9 
     # means 9 blocks remaing 
     #thats why we done [ block - layers ]'''
#     height += 1
#     layer += 1
# print("Height of pyramids is: ", height)
# print("Remaining blocks:", blocks)


'''Assignment Question: 6'''


'''In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) 
which can be described in the following way:
1. take any non-negative and non-zero integer number and name it c0;
2. ⁠if it's even, evaluate a new c0 as c0 ÷ 2;
3. ⁠otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4. ⁠if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.
Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number '
'(it may even require artificial intelligence), but you can use Python to check some individual numbers. '
'Maybe you'll even find the one which would disprove the hypothesis.
Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. 
We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success. '''

# c0 = int(input())  
# steps = 0 
# while c0 != 1:  
#     if c0 %2 == 0:  
#         c0 = c0/2  
#     else:  
#        c0= 3* c0 + 1  
#     print(c0)  
#     steps += 1  
# print("Steps =", steps)


'''Assignment Question: 7'''

'''The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. 
Some people consider them to be the most influential act of the rock era. Indeed, 
they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, 
and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
step 1: create an empty list named beatles;step 2: use the append() method to add the following members of the band to the 
list: John Lennon, Paul McCartney, and George Harrison;step 3: use the for loop and the append() method to prompt the user to add 
the following members of the band to the list: Stu Sutcliffe, and Pete Best;step 4: use the del instruction to remove Stu Sutcliffe 
and Pete Best from the list;step 5: use the insert() method to add Ringo Starr to the beginning of the list.'''















