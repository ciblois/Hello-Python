# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:50:54 2020

@author: Cinthya
"""

print("Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.")

numbers = [
951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105,
942, 941,
386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
345,
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687,
217,
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742,
717,
958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328,
753, 470,
743, 527
]
# your code goes here
#print (len(numbers))
#100 números no total
#pos_stop = numbers.index(237)
#print(pos_stop) #237 = numbers[53]
#print(numbers[53])
#print(numbers[52])
#o último número da lista solicitada tem que ser o 918
i = 0
y = numbers[i]
#imprimi todos os números em sequência
#for x in numbers:
# print(x)
#for x in range(0, 100, 1):
# continue
# while i < 53:
# print(y)
# i += 1
for i in range(0, 100, 1):
    y = numbers[i]
    if i < 53 and y%2 == 0:
        print(y)
        
print("____________________________OR____________________________________")

for number in numbers:
    if number == 237:
        break

    if number % 2 == 1: #number % 2 != 0
        continue

    print(number)