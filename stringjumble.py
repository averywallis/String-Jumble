"""
stringjumble.py
Author: Avery Wallis
Credit: Ethan, Daniel

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
string= str(input("Please enter a string of text (the bigger the better): "))
l=(int(len(string)))
print('You entered "'+ string + '". Now jumble it:')
the = list(string)
spil = string.split(' ')
print()

for x in range(1,l+1):
    print(string[-x],end="")
print()

f=list(reversed(spil))
for word in f:
    print(word,end=" ")
print("")    
print()

for words in spil:
    g=0
    while g>0:
        print(word,end="")
        g=g+1
"""
for x in range(l,1,-1):
    if string[-x]==" ":
        for y in range(l,x-1,1):
            print(string[-y+(l-x)],end="")
"""
