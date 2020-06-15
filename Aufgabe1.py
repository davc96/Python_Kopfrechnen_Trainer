print("Willkommen beim Kopfrechnen Trainer!")
print()
print("Wir wuenschen Dir viel Spass")

name = input("Was ist deine Name?")

import random as rd

print("Hallo",name)

interval = int(input("Aus welchem Intervall [1,x] sollen die Zahlen kommen?"))
if interval < 0 or interval < 10:
    interval = int(input("Bitte gib eine ganze Zahl > 0 und > 10 ein: "))
numbers_interval = []
for i in range(1,interval):
    numbers_interval.append(i)

number_of_aufgaben= int(input("Wie viele Aufgaben willst Du haben?"))
if number_of_aufgaben < 0:
    number_of_aufgaben = int(input("bitte gib eine ganze Zahl > 0 ein: "))

richtige_antworten = 0

def add(x,y):
    print("was ist",x, "+", y)
    a = int(input())
    if a == (x+y):
        print("das ist RICHTIG")
        return True
    else:
        print("das ist FALSCH")
        return False

def subtract(x,y):
    print("was ist", x, "-", y)
    a = int(input())
    if a == (x - y):
        print("das ist RICHTIG")
        return True
    else:
        print("das ist FALSCH")
        return False

def multiply(x,y):
    print("was ist", x, "*", y)
    a = int(input())
    if a == (x * y):
        print("das ist RICHTIG")
        return True
    else:
        print("das ist FALSCH")
        return False

liste = [1,2,3]
for i in range(number_of_aufgaben):
    a = rd.choice(liste)
    x = rd.choice(numbers_interval)
    y = rd.choice(numbers_interval)
    if a == 1:
        if multiply(x,y) == True:
            richtige_antworten += 1
    elif a == 2:
        if subtract(x,y) == True:
            richtige_antworten += 1
    else:
        if add(x,y) == True:
            richtige_antworten += 1

print("Richtige antworten:",richtige_antworten, "Prozent Richtig:", (richtige_antworten/number_of_aufgaben)*100,"%")








