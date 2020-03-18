# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:35:22 2020

@author: Cinthya
"""

# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
    
print("________________________________________________________________")

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
    
print("________________________________________________________________")

# Print First 10 natural numbers using while loop
print("Print First 10 natural numbers using while loop")

i = 0
j = 0
numbers = []

while i < 11:
    print(i)
    i += 1
    
    #OR
print("____________________________OR____________________________________")

while j < 11:
    numbers.append(j)
    j += 1

print(numbers)

    # OR
print("_______________________________OR_________________________________")

for y in range (0,11):
    print(y)
    
print("________________________________________________________________")
