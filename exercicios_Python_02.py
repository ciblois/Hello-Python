# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:59:09 2020

@author: Cinthya
"""
# 2) Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:

from math import factorial

n = int(input("Digite um número para obter o seu fatorial: "))
f = factorial(n)

print("O fatorial de {} é {}." .format(n,f))

#não utilizando a entrada do número e criando uma lista com 10 números aleatórios:

numbers = []
numbers_fact = []

import random

while len(numbers) < 10:
         x = random.randint(1,101)
         numbers.append(str(x))
         y = factorial(x)
         numbers_fact.append(str(y))
         print("O fatorial de {} é {}." .format(x,y))
         
# Se quiser também imprimir as listas em separado...
#print("Essa é a lista com 10 números aleatórios:" + str(numbers))
#print("Essa é a lista com o fatorial de cada um dos 10 números aleatórios:" + str(numbers_fact))
   