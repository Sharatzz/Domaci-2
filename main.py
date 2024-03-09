#1.

broj = int(input('Unesite broj: '))

if broj%2 == 0:
    print('Portal se otvara!')
else:
    print('Portal ostaje zatvoren')

#2.

p = int(input('Petrov broj: '))
m = int(input('Markov broj: '))

if p > m:
    print('Pobjednik je Petar')
else:
    print('Pobjednik je Marko')

#3.

procenat = int(input('Procenat: '))
seminarski = int(input('0 predstavlja da bar jedan seminarski rad nike uradjen, a 1 da su svi seminarski radovi uradjeni'))

if procenat > 75 and seminarski == 1:
    print('Moze da pristupi ispitu')
else:
    print('Ne moze da pristupi ispitu')

#4.

vrijeme = int(input('Unesite vrijeme:'))

if vrijeme > 6 and vrijeme < 13:
    print('Mogu da rade')
elif vrijeme > 17 and vrijeme < 22:
    print('Mogu da rade')
else:
    print('Ne mogu da rade')

#5.

a = float(input("Unesite dužinu  a: "))
b = float(input("Unesite dužinu b: "))
c = float(input("Unesite dužinu c: "))

if a + b > c and a + c > b and b + c > a:
    print('Moze se napraviti trougao')
else:
    print('Ne moze se napraviti trougao')

#6.

x = int(input('Unesite X kordinatu:'))
y = int(input('Unesite y kordinatu:'))

x1 = 2 * x +5

if y == x1:
    print('Nalazi se na pravoj')
else:
    print('Ne nalazi se na pravoj')

#7.

mat1 = int(input('Poeni iz matm prvog takmicara'))
mat2 = int(input('Poeni iz matm drugog takmicara'))
prog1 = int(input('Poeni iz prog prvog takmicara'))
prog2 = int(input('Poeni iz matm drugog takmicara'))

poeni_prvog_tak = mat1 + prog1
poeni_drugog_tak = mat2 + prog2

if poeni_prvog_tak == poeni_drugog_tak:
    if prog1> prog2:
        print('Pobjednik prvi takmicar')
    else:
        print("Pobjednik drugi takmicar")
elif poeni_prvog_tak > poeni_drugog_tak:
    print("Pobjednik prvi takmicar")
else:
    print("Pobjednik drugi takmicar")

#8.

uspjeh = float(input('Unesite uspjeh'))

if uspjeh > 4.5:
    print('Odlican')
elif uspjeh > 3.5 and uspjeh < 4.5:
    print('Varlo dobar')
elif uspjeh > 2.5 and uspjeh < 3.5:
    print('Dobar')
elif uspjeh >= 2.0 and uspjeh < 2.5:
    print('Dovoljan')
else:
    print('Nedovoljan')

#9.

x1_pravougaonika = int(input('Unesite x1: '))
y1_pravougaonika = int(input('Unesite y1: '))
x2_pravougaonika = int(input('Unesite x2: '))
y2_pravougaonika = int(input('Unesite y2: '))

x1_zavjesa = int(input('Unesite x1: '))
y1_zavjesa = int(input('Unesite y1: '))
x2_zavjesa = int(input('Unesite x2: '))
y2_zavjesa = int(input('Unesite y2: '))

duzina1 = x2_pravougaonika - x1_pravougaonika
visina1 = y1_pravougaonika - y2_pravougaonika

duzina2 = x2_zavjesa - x1_zavjesa
visina2 = y1_zavjesa - y2_zavjesa

P1 = duzina1 * visina1
P2 = duzina2 * visina2

if P1 >= P2:
    print('Hoce prekriti')
else:
    print('Nece prekriti')
#10.

x = int(input('Kordinata x1'))
y = int(input('Kordinata y1'))

p = int(input('Kordinata centra 1:'))
q = int(input('Kordinata centra 2:'))
r = int(input('Unesite r:'))

if (((x - p)**2) + ((y - q)**2)) < r**2 :
    print('Pogodila je pikado')
else:
    print('Nije pogodila pikado')

#11.

#12.
db= input('Unesite dvocifreni broj:')

a = int(db[0])
b = int(db[1])
c = int(db[2])

if a > b:
    print(a - b)
elif a<b:
    print(a + b)
elif a == b ==c:
    print(a * b* c)

#13.

r1 = int(input('Unesite r1:'))
r2 = int(input('Unesite r2:'))

p1 = (3.14) * (r1**2)
p2 = (3.14) * (r2**2)

if p1> p2:
    print(p1)
else:
    print(p2)

#14.
pr_1 = int(input('Cijena prvog prozivoda'))
pr_2 = int(input('Cijena drugog prozivoda'))
pr_3 = int(input('Cijena treceg prozivoda'))

zbr1 = pr_1 + pr_2
zbr2 = pr_1 + pr_3
zbr3 = pr_2 + pr_3

if zbr1 < zbr2:
    if zbr1 < zbr3:
        print('zbir proizvoda jedan i dva')
elif zbr2 < zbr1:
    if zbr2 < zbr3:
        print('zbir proizvoda jedan i tri')
elif zbr3 < zbr1:
    if zbr3 < zbr2:
        print('zbir proizvoda dva i tri')

#15.

godina = int(input('Unesite godinu:'))

if (godina%4 == 0 and godina%100 != 0) or (godina%400 == 0):
    print('Godina je prestupna')
else:
    print('Godina nije prestupna')

#16

x1 = int(input('Unesite x1:'))
y1 = int(input('Unesite y1:'))
x2 = int(input('Unesite x2:'))
y2 = int(input('Unesite y2:'))

x = int(input('Unesite x:'))
y = int(input('Unesite y:'))

if x>x1 and x<x2 and y<y1 and y>y2:
    print('Tacka se nalazi unutra pravougaonika.')
else:
    print('Tacka se ne nalazi unutra pravougaonika.')

#17

a = int(input('Unesite duzinu stranice a:'))
b = int(input('Unesite duzinu stranice b:'))

obim = 2*a+2*b
if obim%2==0 and (obim/2)%4==0:
    c = (obim/2)/4
    print('Stranica tog kvadrata je {}'.format(c))
else:
    print('Ne mogu se napraviti takva dva kvadrata')


#18

temp = int(input('Unesi temperaturu:'))
if temp>0 and temp<100:
    print('tecno')
elif temp <= 0:
    print('cvrsto')
elif temp >=100:
    print('gasovito')


#19

skolarina = float(input('Unesite cijenu skolarine: '))
prosjek = float(input('Unesite prosjek ucenika: '))
nagrada = int(input('Da li ucenik ima nagradu (Unesi 1 ako ima, 0 ako nema): '))

if prosjek>=2.5 and prosjek<3.5:
    popust = 10
elif prosjek>=3.5 and prosjek<4.5:
    popust = 20
elif prosjek>=4.5:
    popust = 40
else:
    popust = 0

if nagrada == 1 and popust < 30:
    popust = 30

skolarina -= skolarina*(popust/100)

print('Cijena skolarine je: {}'.format(skolarina))


# 20

n = input('Unesi cetvorocifreni broj: ')
while len(n) != 4:
    n = input('Unesi cetvorocifreni broj: ')

zbirproizvod = 0

if int(n) % 2 == 0:
    for i in n:
        if int(i) % 2 == 0:
            zbirproizvod += int(i)
else:
    zbirproizvod += 1
    for i in n:
        if int(i) % 2 == 1:
            zbirproizvod *= int(i)
print(zbirproizvod)

#21

import math

x = float(input('Unesi X:'))

if x < -7:
    y = -2*x+7/2
elif x < 1:
    y = (x**2-3*x+5)/(x**2+2)
elif x < 8:
    y = math.sqrt(x**2+2*x+2) + math.sqrt(math.fabs(3/2 * x - 4/7))
else:
    math.fabs(3/(x**2)-11*x)

print('Rezultat je {}.'.format(y))

#22

x = float(input('Unesi koordinatu x: '))
y = float(input('Unesi koordinatu y: '))

if x>0 and y>0:
    print('Pripada 1. kvadrantu')
elif x<0 and y>0:
    print('Pripada 2. kvadrantu')
elif x < 0 and y < 0:
    print('Pripada 3. kvadrantu')
elif x > 0 and y < 0:
    print('Pripada 4. kvadrantu')
else:
    print('Tacka se nalazi na nekoj od koordinantnih osa.')

#23

x = float(input('Unesi koordinatu x: '))
y = float(input('Unesi koordinatu y: '))

# y = x-4
# x**2 +y**2 = 16    x**2+y**2 = 36

pom = x - 4
if y > pom: #iznad
    if x<0 and y>0 and x**2 + y**2 < 36 and x**2 + y**2 > 16:
        print('Pripada')
    elif x>0 and y>0 and x**2 + y**2 < 16:
        print('Pripada')
    else:
        print('Ne pripada')
elif y > pom: #ispod
    if x>0 and y>0 and x**2 + y**2 < 36:
        print('Pripada')
    elif x>0 and y<0 and x**2 + y**2 < 16:
        print('Pripada')
    else:
        print('Ne pripada')
else: #na pravoj
    print('Ne pripada')

#24

tekst = 'a'*25+'b'*10
tekst = tekst[0:30]+'.'*3
print(tekst)


#25

tekst = input('Unesi tekst:')
tekst = tekst[1:len(tekst)-1]
print(tekst)

#26

broj = input('Unesi broj: ')
if broj.startswith('0b'):
    print('Binarni')
elif broj.startswith('0o'):
    print('Oktalni')
elif broj.startswith('0x'):
    print('Heksadecimalni')
else:
    print('Dekadni')

#27

tekst = input('Unesi string: ')
ind = 0
for i in tekst:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print('Ima samoglasnik')
        ind = 1
        break

if ind == 0:
    print('Nema samoglasnik')

#28

s = input('Unesi string: ')
target = input('Unesi target string:')

if s.endswith(target):
    print('Da')
else:
    print('Ne')

#29

broj = input("Unesi broj:")
ind = 0

for i in broj:
    if not (i == '0' or i == '1'):
        print('Nije binaran.')
        ind = 1
        break;
if ind == 0:
    print('Jeste binaran')

#30.

N = int(input('Unesite N: '))
s = 0
p = 1
br_parnih = 0
br_neparnih = 0
for _ in range(0,N):

    if _%2 == 0:
        s = s + _
        br_parnih +=1
    else:
        p = p*_
        br_neparnih +=1

print(s)
print(p)
print(br_parnih)
print(br_neparnih)

#31.

start = int(input('Start:'))
end = int(input('End:'))
s = 0

for _ in range(start,end):

    if _%2 == 0 and _%4 !=0:

        a = _**2
        s=s+a

print(s)

#32.
a = int(input('a:'))
b = int(input('b:'))
djelilac = int(input('djelilac:'))
s= 0
br = 0

for _ in range(a,b):

    if _%djelilac ==0:
        s = s +_
        br +=1

print(s)
print(br)

#33.

a = input('tekst')
p = 1
for _ in a:

    if _.isdigit():
        b = int(_)
        p = p *b

print(p)

#34.

str = 'Hi Mr.Rober53. How are you today? Today is 08.10.2019'
a = ''
for _ in str:

    if _.isdigit():
        a = a + _

print(a)

#35.

str1 = input('Unesite string koji zelite da enkriptujete:')

str = str1.lower()
krpt = ''

for _ in str:

    if _ in 'aeiou':
        krpt = krpt + '1'
    else:
        krpt = krpt + '0'

print(krpt)

#38.

str1 = input('Unesite string koji zelite da enkriptujete:')


krpt = ''

for _ in str1:

    if _.isdigit():
        if int(_)%2 ==0:
            krpt = krpt + '0'
        else:
            krpt += '1'
print(krpt)

#39.

broj = input('Unesite broj:')
isNarcissisticNumber = False

N = len(broj)

s = 0

for _ in broj:

    a = int(_)

    s = s + a**N

if int(broj) == s:
    isNarcissisticNumber = True

if isNarcissisticNumber:
    print('Narcis broj')
else:
    print('Nije narcis broj')

#40.

s = 0
niz = [-2, 7, -5, 3, 1, -4]
for broj in niz:
    if broj < 0 and broj % 2 == 0:
        s += abs(broj)

print(s)

#41.

lista = [-2, 7, -5, 3, 1, -4]
max = 3
rez = 0

for broj in lista:
    if broj < max and broj % 2 == 0:
        rez += abs(broj)

print(rez)

#43.

ocjene = [4,5,2,4,3,3,5,3,3]

ocjena_5 = 0
ocjena_4 = 0
ocjena_3 = 0

for _ in ocjene:

    if _ ==3:
        ocjena_3 +=1
    elif _ ==4:
        ocjena_4 +=1
    else:
        ocjena_5 += 1

print(ocjena_5)
print(ocjena_4)
print(ocjena_3)

#44.

posjete = [5000, 5500, 6000, 7000, 6500, 8000, 7500, 7200, 6800, 6000]
najvise = 0

for posete_dan in posjete:
    if _ > najvise:
        najvise = _


print(_)

#45.

plate = [500, 600, 700]
br = 0

for _ in plate:

    if _ > 700:
        br +=1

print(br)


#46.

plate = [540, 690, 900]
najveca_plata = max(plate)
plate.remove(najveca_plata)
druga_najveca_plata = max(plate)

print(druga_najveca_plata)


#47.
broj_1 = float(input("Unesite prvi broj: "))
broj_2 = float(input("Unesite drugi broj: "))
broj_3 = float(input("Unesite treći broj: "))

# Pronalazak minimuma i maksimuma
minimum = min(broj_1, broj_2, broj_3)
maksimum = max(broj_1, broj_2, broj_3)

print(minimum)
print(maksimum)


#48.

X = float(input("Unesite broj X: "))
n = int(input("Unesite broj n: "))

rez = 1
for _ in range(0,n):
    rez *= X

print(rez)

#50.

str = input('String: ').lower()

str1 = ''
for _ in str:

    if _ in 'aeiou':
        str1 += _

print(str1)

#52.

a = 'test'
pre = 'pr'
suf = 'su'
num = 2

novi_string = pre + a + suf
novi_string *= num

print(novi_string)

#53.
petrov_zbir = int(input("Unesite Petrov zbir: "))
broj_golova = petrov_zbir // 2

print(broj_golova)

#55.
H = int(input('H:'))
O = int(input('O:'))

a = min(H//2,O)

print(a)

#57.

broj = input('Unesite broj:')
isNarcissisticNumber = False

N = len(broj)

s = 0

for _ in broj:

    a = int(_)

    s = s + a**N

if int(broj) == s:
    isNarcissisticNumber = True

if isNarcissisticNumber:
    print('Narcis broj')
else:
    print('Nije narcis broj')


#58.
str = 'Hi Mr.Rober53. How are you today? Today is 08.10.2019'
a = ''
for _ in str:

    if _.isalpha():
        a = a + _

print(a)

#59.
tr1 = input('Unesite string koji zelite da enkriptujete:')


krpt = ''

for _ in str1:

    if _.isdigit():
        if int(_)%2 ==0:
            krpt = krpt + '0'
        else:
            krpt += '1'
print(krpt)

#60
start = int(input('Start:'))
end = int(input('End:'))
s = 0

for _ in range(start,end):

    if _%3 == 0 and _%6 !=0:

        a = _**2
        s=s+a

print(s)

#61.

str = input('Unesite string: ')
a = ''
for _ in str:

    if _.isupper():

        a = a + _

print(a)

#62.

a = input('String input: ')


brojac_a = 0


list_a = a.split()


for _ in list_a:

    if _[:2] == '0x':
        brojac_a += 1
    else:
        pass


print(brojac_a)

#63.

str = input('String:').split()

max = ''

for _ in str:

    if len(_) > len(max):
        max = _

print(max)

#64.

broj = int(input("Unesite broj: "))


najmanja_cifra = 9
najveca_cifra = 0


while broj > 0:
    cifra = broj % 10
    najmanja_cifra = min(najmanja_cifra, cifra)
    najveca_cifra = max(najveca_cifra, cifra)
    broj //= 10

print(najmanja_cifra+najveca_cifra)
#66.
unos_lista = input("Unesite elemente liste: ")
lista = [int(x) for x in unos_lista.split()]
brojac_dvocifrenih = 0
brojac_trocifrenih = 0

for broj in lista:
    if 10 <= abs(broj) <= 99:
        brojac_dvocifrenih += 1
    elif 100 <= abs(broj) <= 999:
        brojac_trocifrenih += 1

if brojac_dvocifrenih > brojac_trocifrenih:
    print("U listi ima više dvocifrenih brojeva.")

#67.
unos_lista = input("Unesite elemente liste: ")
lista = [int(x) for x in unos_lista.split()]


trazeni_broj = int(input("Unesite broj: "))


print(lista.count(trazeni_broj))

#69.

zarade = [5000, 6000, 7000, 8000, 9000]
prosjek = sum(zarade) / len(zarade)

for i in range(len(zarade)):
        if zarade[i] > prosjek:
            zarade[i] *= 0.9
        else:
            zarade[i] *= 1.1

#70.

lista = [1, 2, 3, 4, 5]

zbir = 0

for _ in lista:
    if _ % 3 == 0:
        zbir += _**2

            
print(zbir)













