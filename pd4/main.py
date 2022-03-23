#Zadanie 1
import random
import sys

x = 0
plik = open('plik.txt', 'w+')
while x < 15:
    y = random.randint(1, 30)*2
    y = str(y)
    plik.write(y)
    plik.write(', ')
    x+=1

plik.close()

#Zadanie 2
plik = open('plik.txt', 'r')
print(plik.read())
plik.close()

#Zadanie 3
with open('plik2.txt', 'w+') as plik:
    plik.write(sys.stdin.readline())
with open('plik2.txt', 'r') as plik:
    print(plik.read())

#Zadanie 4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        return str(self.ilosc)+self.jednostka_miary
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed


test1 = NaZakupy('mleko', 5, 'l', 1.5)
print(test1.wyswietl_produkt())
print(test1.ile_produktu())
print(test1.ile_kosztuje())


#Zadanie 5
class Ciagi:
    def __init__(self, a1, n , r):
        self.a1 = a1
        self.n = n
        self.r = r
    def wyswietl_dane(self):
        print('a1 = ', self.a1)
        print('n = ', self.n)
        print('r = ', self.r)
    def pobierz_elementy(self):
        self.n=input('Podaj n: ')
        an = input('Podaj an: ')
        an = int(an)
    def pobierz_parametry(self):
        self.a1 = input('Podaj a1: ')
        self.n = input('Podaj n: ')
        self.r = input('Podaj r: ')
        self.a1 = int(self.a1)
        self.n = int(self.n)
        self.r = int(self.r)
    def policz_sume(self):
        return ((self.a1+(self.a1+(self.n-1)*self.r))/2)*self.n
    def policz_elemety(self):
        return self.a1+(self.n-1)*self.r

test2 = Ciagi(1, 8, 3)
print(test2.pobierz_parametry())
print(test2.wyswietl_dane())
print(test2.pobierz_elementy())
print(test2.policz_sume())
print(test2.policz_elemety())

#Zadanie 6
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ile_krokow):
        self.y = self.y + ile_krokow * self.krok
    def idz_w_dol(self, ile_krokow):
        self.y = self.y - ile_krokow * self.krok
    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - ile_krokow * self.krok
    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + ile_krokow * self.krok
    def pokaz_gdzie_jestes(self):
        print(self.x, ', ', self.y)

ruch = Robaczek(0, 0, 1)
ruch.idz_w_gore(3)
ruch.idz_w_lewo(7)
ruch.pokaz_gdzie_jestes()
ruch.idz_w_dol(10)
ruch.idz_w_prawo(2)
ruch.pokaz_gdzie_jestes()