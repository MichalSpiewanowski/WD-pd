#Zadanie 1
A = [1-x for x in range(1,11,1)]
print(A)
B = [4**x for x in range(7)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

#Zadanie 2
lista1 = [12, 32, 124, 321, 9, 71, 56, 93, 18, 11]
print(lista1)
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista2)

#Zadanie 3
produkty = {'mleko': 'l', 'jajka': 'sztuki', 'mięso drobiowe': 'kg', 'mięso wołowe': 'kg', 'pomidory': 'kg', 'chleb': 'sztuki', 'woda': 'l', 'sok owocowy': 'l', 'kalarepa': 'sztuki'}
sztuki = {key: value for key, value in produkty.items() if value == 'sztuki'}
print(sztuki)

#Zadanie 4
def prostokatny(a, b, c):
    if (a < c) & (b < c):
        if a**2+b**2 == c**2:
            return 'Trójkąt jest prostokątny'
        else:
            return 'Trójkąt nie jest prostokątny'
    elif (a < b) & (c < b):
        if a**2+c**2 == b**2:
            return 'Trójkąt jest prostokątny'
        else:
            return 'Trójkąt nie jest prostokątny'
    else:
        if b**2+c**2 == a**2:
            return 'Trójkąt jest prostokątny'
        else:
            return 'Trójkąt nie jest prostokątny'
print(prostokatny(3, 4, 5))
print(prostokatny(3, 5, 4))
print(prostokatny(4, 3, 5))
print(prostokatny(4, 5, 3))
print(prostokatny(5, 4, 3))
print(prostokatny(5, 3, 4))
print(prostokatny(3, 3, 5))

#Zadanie 5
def trapez(a=6, b=3, h=4):
    return ((a+b)*h)/2
print(trapez())

#Zadanie 6
def iloczyn(a=1, b=4, ile=10):
    wynik = a
    for x in range(ile-1):
        a+=b
        wynik*=a
    return wynik
print(iloczyn())

#Zadanie 7
def iloczyn2(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        wynik = 1
        for x in liczby:
            wynik*=x
        return wynik
print(iloczyn2(1, 5, 9, 13, 17, 21, 25, 29, 33, 37))

#Zadanie 8
# def suma(** rzeczy):
#     ilosc = 0
#     for x in rzeczy:
#         ilosc += 1
#     wynik = 0
#
#     return 'Koszt '&ilosc&' rzeczy wynosi '&sum(rzeczy.values())
# print(suma(Pomidor=1.2, Mleko=3.5, Chleb=2.7))

#Zadanie 9
import ciagi.caryt
ciagi.caryt.wzory(1)
print(ciagi.caryt.wyraz_n(2, 10, 3))
print(ciagi.caryt.suma(2, 29, 10))
import ciagi.cgeo
ciagi.cgeo.wzory(1)
print(ciagi.cgeo.wyraz_n(1, 7, 3))
print(ciagi.cgeo.suma(1, 7, 3))

