# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_markers: '{{{,}}}'
#     cell_metadata_filter: comment_questions,-all
#     cell_metadata_json: true
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Lab 2020-09-22

# [dokumentacija](https://docs.python.org/3.7/tutorial/index.html)

# ## Pakuotės
#
# Python programų pradžioje visada būna programoje naudojamų pakuočių importavimas. Pakuočių pagalba galime pasinaudoti kitų žmonių darbu.
# Pavyzdžiui importavę `math` pakuotę galėsim naudoti jos viduje apibrėžtą pi vertę `math.pi`


import math
from time import sleep
import random


# ## Python vietoj skaičiavimo mašinėlės

2+2

math.sqrt(4)

3**2

6/2

# ---
# >> **UŽDUOTIS 1**
# >>
# >> Interpretatoriuje (The REPL - Read, Eval, Print and Loop) parašykite `math.` ir tada paspauskite `TAB` klavišą. Paspaudimas duos daug viduje math pakuotės apibrėžtų elementų. Patyrinėkite juos, pamėginkite parašyti paprastas formules naudodamiesi math funkcijomis (sin, cos, log).
# >>
# ---


math.





# ## IPython

# Dokumentacijos pasiekimas

math.sin?

# Pilna dokumentacija help funkcija

help(math)

# Kai kurios OS komandinės eilutės komandas galima rašyti tiesiai į Jupyter lab ląsteles
#
# Dabartinė aktyvi direktorija gaunama

pwd

# ls -a

# Norint atlikti ar priskirti kintamajam komandų išeigą reikia pridėti `!`

direktorija = !find . -type d
direktorija

# Taip pat galima pasiekti buvusių komandų rezultatus arba pačias komandas in ir out komandomis

In[-2]


Out[9]


# ---
# >> **UŽDUOTIS 2**
# >>
# >> - Patyrinėkite IPython funkcijas. `%lsmagic`, `%magic` and `alias`
# >>    - Raskite dabartinę direktoriją
# >>    - nueikite į ~/Documents/biod2020/lect direktoriją.
# >>
# >>
# ---

# Komentarai. Rašant jupyter lab ipynb failus komentarus patogu rašyti markdown sintakse.
#  Tada jie ryškiau matosi ir galima pateikti daug papildomos informacijos.

# {{{
#python will ignore this
#pwd
# }}}

#
# ## Operatoriai
#
# suma +
#
# skirtumas -
#
# sandauga *
#
# kėlimas laipsniu **
#
# dalyba /
#
# dalyba be liekanos //
#
# liekana %

2 + 2

2 - 2

2 * 2

2 ** 3

2 / 3

2 // 3

2 % 3

35 % 10


# ## Loginiai operatoriai
#
# Šių operatorių pagalba formuojame saknius
#
# mažiau <
#
# daugiau >
#
# lygu ==
#
# nelygu !=
#
# mažiau arba lygu <=
#

a = True
b = False

# Ir

print(a and b)

# Arba

print(a or b)

# ne

print(not a)

# ## Duomenų tipai

# Parašysim programą konvertuojančią temperatūrą iš Celsijaus į Farenheito skalę. y = (x × 9/5) + 32

# Norint konvertuoti 100 galime tiesiog rašyti formulę

(100 * 9/5) + 32


# Vėlesniam panaudojimui galime priskirti rezultatą kintamajam

Fahrenheit = (100 * 9/5) + 32
Fahrenheit

# Sukurtas `float` tipo kintamasis --  jis tikslesnis už `int` kuris vaizduoja tik sveikus skaičius.
#
# Kintamojo tipą galima rasti naudodami funkciją `type`.

type(Fahrenheit)

# Galima pakeisti kintamojo tipą:

int(Fahrenheit)

# Vertė kintamojo pasikeis galutinai tik priskyrus int funkcijos išeigą kintamajam

Fahrenheit = int(Fahrenheit)
Fahrenheit

# Pagrindiniai tipai kintamųjų

# Integer

10

#  Float

3.14

# Galima naudoti mokslinę notaciją

4e2

# Boolean - True False arba 1 0

type(True)

# Complex

type(3 + 4j)

# String

message = 'Hello world'
message

#  Ir 4 tipai talpinantys daugiau nei vieną kintamąjį

# Sąrašas (List)

[1, 2, 3]

# Kortežas (Tuple)
# Nekintantis objektas, sudaromas iš bet kokio tipo duomenų. Sukuriamas `tuple()` komandos pagalba arba `()`. Elementai atskiriami kableliu; vieno elemento tuple sukuriamas `(x,)`.

(1, 2)

# Aibė (Set)

{1, 2}

# Žodynas (Dictionary)

{'key': 'value'}

# Vėliau juos apžvelgsime plačiau

# IPython terminale galime pamatyti visus kintamuosius aplinkoje.

who

# Visus kintamuosius ištrinti ir atlaisvinti vietą galime komandą `reset`

# ---
# >> **UŽDUOTIS 3**
# >>
# >> - Patyrinėkite dokumentaciją ir raskite būdą ištrinti tik vieną specifinį kintamąjį . Ištrinkite Farenheito kintamąjį bet palikite kitus atmintyje.
# >>
# ---

# ## Funkcijos
# Norėdami naudoti tą pačią funkciją daug kartų sukuriam funkciją kuria pasieksime reikalingą kodą.
#


def celsius_to_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit)


# Jei norėtumėm suskaičiuoti daug verčių ir jas išsaugoti viename kintamajame galime panaudoti sąrašus. Juos kuriame laužtiniais skliaustais [] ir jie gali turėti daug skirtingų tipų.

ListA = [celsius_to_farenheit(100), celsius_to_farenheit(
    110), celsius_to_farenheit(200)]
ListA

# Sąrašo elementų skaičius

len(ListA)


# Sąrašai vieni iš naudingiausių konteinerių. Patyrinėkite skirtingus metodus skirtus dirbti su sąrašais.
# Paspauskite TAB po taško

ListA.

# ### Metodai:

# Append - prideda elementus prie sąrašo

ListA.append(2)
ListA

# Surūšiuoja sort

ListA.sort()
ListA

# Extend -- prideda elementus iš kitų konteinerių

ListA.extend([1, 2, 3])
ListA


ListA.append([10, 11, 12])
ListA


# Pridėti skaičių 2 specifinėje vietoje galime su insert

ListA.insert(1, 2)
ListA

# Verčių apvertimas

ListA.reverse()
ListA

# Pop išima elementą iš sąrašo specifinėj vietoje

pp = ListA.pop(2)
ListA

pp


# Copy - duoda kopiją sąrašo

ListB = ListA.copy()

ListA.append(2)
ListA

ListB

#  Jei mes kurtumėme kopiją tiesiog priskirdami

ListC = ListA
ListC

ListA.append(88)
ListA

ListC

#  matome kad sukuriama netikra kopija, o tik nuorodą į ta patį elementą todėl pakeitus ListC pakinta ir ListA

# Index -- gražina elemento indeksą

ListA.index(3)

# Remove -- pašalina elementą (tik patį pirmą eilėj)

ListA.remove(88)
ListA

# clear - ištrina visus elementus

ListA.clear()
ListA


# Elementus pasiekiam indeksuodami

ListB[0]

ListB[3]

ListB[-1]

# Arba kirpdami

ListB[0:2]

# Su sąrašais galime atlikti aritmetines operacijas

ListB * 2

ListB + ListB

#  galima kurti sąrašus sąrašuose (nested lists)

ListC = [ListB, ListB]
ListC

# Pasiekti pirmą sąrašą:

ListC[0]

# pasiekti pirmą elementą pirmame sąraše

ListC[0][0]


TestList = [1, [79, 77, 78], 0, [2, [45, 65], 55], 4]

# ---
# >> **UŽDUOTIS 4**
# >>
# >> - Gauti skaičius 78, 55, 0, 45 iš sąrašo `TestList`
# >>
# ---













# Pakeičiam funkciją kad ji gražintu dar ir temperatūrą kelvino skalėj


def celsius_to_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius - 273.15
    return round(fahrenheit), round(kelvin)


output = celsius_to_farenheit(42)
output

#  Funkcijos gražina kortežą  (tuple) `output`
#  Kortežo pakeisti negalima

output[1] = 3


# Kortežus galima išskleisti

fah, kel = output
kel

fah

fah, kel = celsius_to_farenheit(42)


#  Kortežai veikia greičiau už sąrašus ir jų negalima turinio pakeisti.

# Žodynai formuojami iš rakto ir vertės poros `{key: value}`. Raktai turi būti unikalūs ir nekeičiami (tuple, integer, string, float, boolean).
# Vertes žodyne pasiekiam rakto pagalba. Vertės apribojimų neturi.

temperature = {}
cel = 34
fah, kel = celsius_to_farenheit(cel)
temperature[cel] = fah, kel

cel = 4
fah, kel = celsius_to_farenheit(cel)
temperature[cel] = fah, kel

cel = -9
fah, kel = celsius_to_farenheit(cel)
temperature[cel] = fah, kel

temperature

temperature[4]

# Gauti visus elementus iš žodyno

temperature.items()

# Raktus gauname

temperature.keys()

#  Rakto pagalba gauname vertes

temperature.get(4)

# Žodynus galime kurti daugeliu būdu


dictA = {'key1': 'value1', 'key2': 'value2'}
dictA.keys()

dictA['key1']


dictA = dict(key1='value1', key2='value2')
dictA


dictA = dict([('key1', 'value1'), ('key2', 'value2')])
dictA


# Aibės yra kolekcijos unikalių verčių
#
# Aibių pagalba atliekame daug loginių operacijų
# pvz jei turime sąrašą s

s = [1, 1, 1, 2, 3, 5, 5]

# paversdami jį aibe gauname tik unikalias vertes

ss = set(s)
ss


# Aibių metodai

rr = set([2, 4, 6, 5])

rr.difference(ss)  # skirtumas elementų

rr.intersection(ss)  # bendri elementai

rr.issubset(ss)  # tikrina ar viena aibė yra kitos aibės dalis

rr.union(ss)  # apjungia aibes

rr.add('k')  # prideda elementus
rr

rr.clear()  # pašalina elementus
rr

# plačiau

help(set)


# ---
# >> **UŽDUOTIS 5**
# >>
# >> - patyrinėkite metodus kolekcijų (set, tuple, dict)
# >>
# ---


# ## Teksto formatavimas

# Galiausiai norėdami pavaizduoti gautus rezultatus (ekrane arba suformatuoti ir įrašyti į failą naudojame teksto kintamuosius (string)

stringA = "This is string A"
stringA

stringB = 'This is string B'
stringB

# Teksto kintamasis  yra nepakeičiamas ir kad ir kokius veiksmus su juo atliekame naujas objektas yra sukuriamas atmintyje. Kaip ir kolekcijos teksto kintamieji turi daug metodų.

# Norint pakeisti didžiąsias raides į mažąsias.

stringA.lower()

# Į didžiąsias

stringA.upper()

# + ir *  sujungia kintamuosius

stringA + stringB

stringA * 2

# Geriau naudoti join metodą kurio pagalba lengviau kontroliuoti išeigą

' '.join([stringA, stringB])

# split padaliną į dalis

stringA.split()

# ---
# >> **UŽDUOTIS 6**
# >>
# >> - Peržvelgti teksto kintamojo [metodus](https://docs.python.org/3.7/library/stdtypes.html#string-methods)
# >>
# ---

# ## Teksto formatavimas

# `print` funkcija formatuoja ir atvaizduoja tekstą

print(stringA)

print(stringA, stringB)

# Seni teksto formatavimo metodai

"Celsius, %s. Fahrenheit %s." % (cel, fah)  # % operator

"Celsius, {0}. Fahrenheit{1}.".format(cel, fah)  # str.format method

# print funkcijos pagalba apjungiame

print('Temperature in Celsius', cel, 'Fahrenheit ',
      fah, sep=' ', end='\n', flush=False)

# Nuo python 3.6 versijos  naudojami fString ir rString teksto kintamieji

#  fStrings pakeičia laužtiniuose skliaustuose esančius elementus į jų reikšmes python kode

f'Temperature in Celsius {cel}'

# rString ignoruoja visus specialius ženklus

r'Temperature in Celsius {cel}'

#  Variantai vaizdavimo
#
# |special char|displayed|
# |-----------|----------|
# |\t|tab|
# |\n|new line|
# |\r|Enter, return|
# |\b|back|
# |\\|backslash \|
# |\'|quotation mark|
# |\"|double quotation mark|

print(f'Temperature\nCelsius {cel}\t Fahrenheit {fah}')


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)


for i in range(101):
    progress(i)
    sleep(0.1)

# ---
# >> **UŽDUOTIS 7**
# >>
# >> - pakeiskite funkciją progress kad gauti apačioje pavaizduotą išeigą
# >>
# ---


# {{{ {"active": ""}
# [  # ] 5%
# [  # ] 6%
# [  # ] 7%
# [  # ] 8%
# [  # ] 9%
# [  # ] 10%
# [  # ] 11%
# [  # ] 12%
# }}}

# ## Eigos kontrolė

# ## IF
#
# Vienas iš svarbiausių elementų. Jei (if) kažkas yra tiesa tai daryk X kita vertus jei kažkas kitkas tiesa (elf) daryk Y galiausiai (else) daryk Z
# else ir elif nėra būtini

if 5 > 6:
    print(1)

# Pakeiskite x į kažką kitą kad matyt kaip veikia if

x = 0
if x < 0:
    print("neigiamas skaičius")
elif x == 0:
    print("nulis")
else:
    print("teigiamas skaičius")

# Papildom funkciją kitais metodais naudodami if


def convert_to_SI(value, type="temp"):
    if type == "temp":
        celsius = (value - 32) * 5 / 9
        kelvin = celsius + 273.15
        return round(celsius), round(kelvin)
    elif type == "dist":
        meters = value * 0.0245
        return meters
    else:
        print("Type is not defined")


convert_to_SI(40)

convert_to_SI(40, "dist")

convert_to_SI(40, "temp")

# ---
# >> **UŽDUOTIS 8**
# >>
# >> Papildykite funkciją `convert_to_SI2` kad ji atskirtų ir gražintų arba Celsius arba Kelvinus
# >>
# ---


def convert_to_SI2(value, type="celsius"):
    pass







convert_to_SI2(10, "celsius")

convert_to_SI2(10, "dist")

convert_to_SI2(10, "kelvin")


# # FOR
#
# For pagalba einam per elementus konteineriuose

for x in [1, 2, 3]:
    print(x)

# Kuriam sąrašus

values_in_fahrenheit = [0, 44, 56, 788]
values_in_celsius = []
values_in_kelvin = []
for value in values_in_fahrenheit:
    cel, kel = convert_to_SI(value)
    values_in_celsius.append(cel)
    values_in_kelvin.append(kel)


values_in_kelvin

values_in_celsius


# ## RANGE
#
# Automatiškai generuojam sąrašą skaičių
#
# range([start], stop[, step])

for i in range(4):
    print(i)


a_range = range(-10, -100, -30)
a_range

#  konvertuojam į sąrašą

a_list = list(range(4))
a_list

# i yra priskiriamas kiekvienoje iteracijoje ir viduje jo pakeitimas yra tik laikinas

for i in range(4):
    print(i)
    i = 10
    print(i)


# ### For ir žodynai

data = {"-18": "255", "7": "280"}
for k, v in data.items():
    print(f"Celsius: {k}, Kelvin {v}")

# ### enumerate
#
# Norint gauti indeksą elemento naudojam enumerate
#
# enumerate(iterable, start=0)

a = ["a", "b", "c"]
for i, v in enumerate(a):
    print(i, v)

for i in range(len(a)):
    print(i, a[i])


str = "Python"
for idx, ch in enumerate(str):
    print(f"index is {idx} and character is {ch}")


#  ### zip sujungia daugiau sąrašų

for q, a in zip(values_in_fahrenheit, values_in_celsius):
    print(f"Temperature in celsius {a} equals {q} in fahrenheit")

#  Jei konteineriai ne vienodo dydžio

for q, a in zip(values_in_fahrenheit, values_in_celsius[1:2]):
    print(f"Temperature in celsius {a} equals {q} in fahrenheit")


#  ## while
#
# While kuria ciklus begalinio dydžio arba kol pasiekiama tam tikra sąlyga

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b


x = 0
while x < 0.9:
    x = random.random()
    print(x)


#  ## break ir continue


for n in range(2, 10):
    print(f"n {n}", flush=True)
    for x in range(2, n):
        print(f"x {x}", flush=True)
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:  # for loop condition else is evaluated if no break was encountered
        print(n, "is a prime number")


#  ## pass
#
# nedaro nieko bet leidžia sukurti tuščias sąlygas

for i in range(4):
    pass



















# ### Atsakymai
# 2. pwd, cd
# 3. %reset_selective dabartine_dir
# 4. TestList[1][2]
#  TestList[3][2]
#  TestList[2]
#  TestList[3][1][0]
# 5. \r pakeisti į \n
# 8.

def convert_to_SI2(value, type="celsius"):
    if type == "celsius":
        celsius = (value - 32) * 5 / 9
        return round(celsius)
    if type == "kelvin":
        celsius = (value - 32) * 5 / 9
        kelvin = celsius + 273.15
        return round(kelvin)
    elif type == "dist":
        meters = value * 0.0245
        return meters
    else:
        print("Type is not defined")


