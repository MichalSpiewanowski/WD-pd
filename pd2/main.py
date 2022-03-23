#Zadanie 1
sporty = ['Snooker', 'Culring', 'Bobsleje', 'Biathlon']
sporty.reverse()
sporty.append('Piłka nożna')
sporty.append('Skoki narciarskie')
sporty.append('Kolarstwo')
print(sporty)

#Zadanie 2
skroty = {'dr': 'doktor', 'itp': 'i tym podobne', 'itd': 'i tak dalej', 'np.': 'na przykład', 'nr': 'numer', 'PESEL': 'Powszechny Elektroniczny System Ewidencji Ludności', 'tj': 'to jest', 'tzn':'to znaczy', 'tzw': 'tak zwany'}
print(skroty)

#Zadanie 3
ilosc = 0
gry = {'W3': 'Wiedźmin 3', 'DbD': 'Dead by Daylight', 'OW': 'Overwatch', 'MC': 'Minecraft'}
for x in gry:
    ilosc += 1
print(ilosc)
#Zadanie 4
suma = 0
y = 0
napis = input('Wprowadź napis: ')
for x in napis:
    if napis[y]=='a':
        suma +=1
    y+=1
print(suma)

#Zadanie 5
import sys as system
system.stdout.write("Podaj pierwszą liczbę: ")
liczba1 = system.stdin.readline()
liczba1 = int(liczba1)
system.stdout.write("Podaj drugą liczbę: ")
liczba2 = system.stdin.readline()
liczba2 = int(liczba2)
system.stdout.write("Podaj trzecią liczbę: ")
liczba3 = system.stdin.readline()
liczba3 = int(liczba3)
print(liczba1**liczba2+liczba3)

#Zadanie 6
a = input('Podaj pierwszą liczbę: ')
b = input('Podaj drugą liczbę: ')
c = input('Podaj trzecią liczbę: ')
a = int(a)
b = int(b)
c = int(c)
if (a > b):
    if(a > c):
        print('Największą liczbą jest a')
    else:
        print('Największą liczbą jest c')
else:
    if(b > c):
        print('Największą liczbą jest b')
    else:
        print('Największą liczbą jest c')

#Zadanie 7
kwadrat = [3, 4, 345, 32, 12, 4.5, 2.3, 5.6, 45.2, 3.57, 21.786, 245, 65, 4.5]
y = 0
for x in kwadrat:
    kwadrat[y] = kwadrat[y]**2
    y+=1
print(kwadrat)

#Zadanie 8
y = 0
parzyste = []
while y < 10:
    liczba = input('Podaj liczbę: ')
    liczba = int(liczba)
    if liczba % 2 == 0:
        parzyste.append(liczba)
    y+=1
print(parzyste)

#Zadanie 9
liczba = input('Podaj liczbę: ')
liczba = int(liczba)
import math
try:
    print(math.sqrt(liczba))
except ValueError:
    print('Liczba nie może być ujemna')