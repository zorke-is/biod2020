# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:light,md:myst
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

# # Duomenų valdymas ir vaizdinimas
#
# 2020-10-13
#
# - numpy
# - matplotlib
# - K1

# ---
# - [NumPy](https://numpy.org/)
#
# Tai fundamentali duomenų analizės pakuotė susidedanti iš:
#
# - N-dimensių masyvų objektų.
# - Masyvų  operacijų (broadcasting).
# - Įrankių integruoti C/C++ ir Fortran programavimo kalbų kodą.
# - Įvairų metodų duomenų analizei (algebra, FFT, atsitiktinių skaičių
#   generavimas ir t.t.)
# ---
# - [pandas](https://pandas.pydata.org/)
#
# `pandas` skirta greitam duomenų manipuliavimui ir apžvalgai.
# Sukurta SAS, STATA, SQL, R data.frame pavyzdžiu naudojant python ir numpy.
# ---
# - [scipy](https://www.scipy.org/)
#
# Python ekosistema atviro kodo programų skirtų duomenų analizei.
# Pagrindinės pakuotės: NumPy, Matplotlib, IPython, SymPy, pandas, SciPy
# biblioteka

# ## Numpy
#
# Bibliotekų importavimas

import pathlib
import re
import numpy as np
import matplotlib.pyplot as plt

# NumPy (Numerical Python) įgalina python programavimo kalbą efektyviai laikyti
# ir manipuliuoti dideliais duomenų masyvais.
# Tai pati svarbiausia biblioteka duomenų analizėje!
#
# Siekdama efektyvumo NumPy leidžia masyvuose laikyti tik vieno tipo
# kintamuosius.

simple_array = [1, 4, 2, 5, 3]
simple_array

# Standartinius sąrašus galime lengvai paversti į NumPy masyvą:

simple_array = np.array(simple_array)
simple_array

# Jei sąraše yra skirtingi duomenų tipai tai jie  paverčiami į sudėtingiausią
# tipą esanti sąraše.
#
# Pvz:
#
# Visi elementai paverčiami į `float`

np.array([3.14, 4, 2, 3])

# Visi elementai paverčiami į tekstą

np.array([3.14, 4, 2, 3, 't'])

# Tipą galime nurodyti kūrimo metu

np.array([1, 2, 3, 4], dtype='float32')

# Teksto elementų paversti skaičiais negalime

np.array([1, 't', 3, 4], dtype='float32')

# Daugiadimensiai masyvai susikuria iš daugiadimensių sąrašų (nested)

listA = [[4, 5], [3, 2]]
np.array(listA)

# ### Dažnai pasitaikantys metodai
#
# Tuščias masyvas 3x3 dimensijų (vertės lieka tokios kokios prieš tai buvo
# išskirtose atminties blokuose)

np.empty((3, 3), dtype=float)

# 10 elementų nuliai:

np.zeros(10, dtype=int)

# 3x5 float vienetų masyvas

np.ones((3, 5), dtype=float)

# 2d masyvas su vienetais pagrindinėje įstrižainėje

np.identity(n=5)

# Nurodytoje įstrižainėje

np.eye(N=3,  # rows
       M=5,  # columns
       k=1   # Index of the diagonal (main diagonal 0 is default)
       )

# 3x5 float masyvas su specifine reikšme

np.full((3, 5), 3.14)

# Masyvas užpildytas nurodytomis vertėmis

np.full((3, 5), [3.14, 2, 3, 4, 5])

# #### `np.arange`
#
# Python dažnai naudojamas metodas `range` turi porą alternatyvų NumPy
# pakuotėje
#
# `range` -> `arange(start,end,step)`

np.arange(0, 20, 2)

# #### `np.linspace`

# +
np_array, step = np.linspace(0, # pradinis taškas
1, # pabaiga
5, # taškų skaičius
endpoint=False, # Paskutinio elemento įtraukimas
retstep=True, # žingsnis
dtype=float) # duomenų tipas

step, np_array
# -

np_array, step = np.linspace(
    0, 1, 5, endpoint=False, retstep=True, dtype=float)
np_array

N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
plt.plot(x1, y, 'o', label='endpoint=True')
plt.plot(x2, y + 0.5, 'o', label='endpoint=False')
plt.ylim([-0.5, 1])
plt.title('Endpoint effect')
plt.legend();

# Geometrinė progresija nuo 1 iki 10, vienodais tarpais

x = np.geomspace(1, 10, num=10, endpoint=True, dtype=float)
plt.plot(x);

# Logaritminė skaičių seka (gali būti skirtinga bazė)

x = np.logspace(1, 10, 10, endpoint=True, base=10.0, dtype=float)
plt.plot(x);

# ### Atsitiktiniai skaičiai
#
# NumPy turi metodus generuoti atsitiktinius skaičius.
#
# Pati svarbiausia dalis dirbant su atsitiktiniais skaičiais yra
# nustatymas atsitiktinio generavimo pradmens (seed).
# Kiekvieną kartą nustačius naujai pradmenį tie patys atsitiktiniai skaičiai yra sugeneruojami.
# Tokiu būdu mes galime atkartoti "atsitiktinius" eksperimentus.
#
# Dažniausiai naudojama pradmens nustatymo ir atsitiktinių skaičių
# generavimo sintaksė:

np.random.seed(1)
np.random.random()

np.random.random()

np.random.seed(1)
np.random.random()

np.random.random()

# Šio metodo sintaksė panaši į random pakuotės naudojamą sintaksę

import random
random.seed(1)
random.random()

# NumPy `seed` funkcija įtakoja tik NumPy ir ją naudojančias pakuotes!
# Globalų pradmenį galima nustatyti random pakuotės pagalba.
#
# Nustatyti atsitiktinių skaičių kūrimo pradmenis ir generuoti
# atsitiktinius skaičius galima ir per objektus:
#
# Pirmiausiai apsibrėžiam naują generatoriaus objektą kuriame nurodome pradmenį
# generuojančius parametrus ir tada naudojame sukurtą objektą `rng` šaukdami jo metodus.

rng = np.random.default_rng(seed=1)
rng.random()

rng = np.random.default_rng(seed=1)
rng.random()

# +
# np.random?
# -

# #### Metodai generuojantys atsitiktinių skaičių sekas
#
# Atsitiktinis float skaičius intervale [0.0, 1.0) iš tolygaus skirstinio:

rng.random(size=4)

rng.random()

# +
# rng.shuffle?
# -

# Sumaišyti sąrašą galime

listA = np.arange(10)
listA

rng.shuffle(listA)
listA

# Atsitiktinai pasirinkti elementą iš sąrašo (np.choice?)

rng.choice(listA)

# Atsitiktinis sveikas skaičius

np.random.randint(8)

# Atsitiktinis skaičius iš normalaus skirstinio

rng.normal()

# Atsitiktinis skaičius iš Puasono skirstinio

rng.poisson()

# ### Informacija apie masyvus
#
# Sukūrus masyvus ar importavus duomenis pirmiausiai norime gauti
# informaciją apie juos

x1 = np.arange(12)
x1

print("x1 dimensions: ", x1.ndim)

print("x1 shape:", x1.shape)

print("x1 size:", x1.size)

print("x1 type:", x1.dtype)

print("x1 size in bits of every element:", x1.itemsize)

print("total size of array:", x1.nbytes)

# ### Performatavimas masyvo dimensijų

x2 = np.arange(0, 12)
np.reshape(a=x2,                
           newshape=[2, 6])     # naujos dimensijos

# Tą patį galima padaryt vienoje eilutėje sujungus abi komandas tašku

x2 = np.arange(0, 12).reshape(2, 6)
x2

print("x2 dimensions: ", x2.ndim)

print("x2 shape:", x2.shape)

print("x2 size:", x2.size)

print("x2 type:", x2.dtype)

print("x2 size of every element:", x2.itemsize)

print("array size:", x2.nbytes)

# Atvirkščiai duomenis paverčia vienadimensiais `np.ravel`

np.ravel(a=x2,
         order='C'  # eiliškumas išskleidimo C,F
         )

np.ravel(a=x2,
         order='F'
         )

# Pavertimas vienadimensiu vadinamas išlyginimu (flattening)

x2.flatten(order='C')

# Masyvo transponavimas

x2.T

# Apvertimas iš viršaus į apačia

np.flipud(x2)

# Apvertimas iš kairės į dešinę

np.fliplr(x2)

# Pasukimas prieš laikrodžio rodyklę 90 laipsnių

np.rot90(x2,
         k=1  # pasukimų skaičius
         )


# Pastūmimas elementų nurodyta kryptimi

x2

np.roll(a=x2,
        shift=2,  # per 2 elementus pastumti
        axis=0  # eilutė
        )

# ### Elementų pasiekimas (indexing)
#
# Elementai pasiekiami panašiai kaip ir paprastuose sąrašuose

x1

# Gauti pirmą elementą

x1[0]

# 5-tą elementą

x1[4]

# Paskutinį elementą

x1[-1]

# Daugiamačių masyvų indeksavimas šiek tiek kitoks
#
# Standartiniai masyvai indeksuojami dviem laužtiniais skliaustais

x_2 = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
x_2

x_2[1][0]

# NumPy daugiamačiai masyvai indeksuojami vienais laužtiniais skliaustais

x2

x2[1, 0]

# Norint pakeisti vertes nurodom vietą kurią norime pakeisti ir priskiriame naują
# vertę.
# Reikia nepamiršti kad priskiriamos naujos vertės keičia savo tipą į to masyvo tipą.
# Pavyzdyje 33.33(float) tampa 33(int).

x2[1, 1] = 33.33
x2

# ### Fancy indexing
#
# Galima pasiekti daug elementų ir suformatuoti išeigą viena komanda indeksuojant
# kito masyvo pagalba.

ind = np.array([[1, 0], [-2, -1]])
x1

# Jei naudojam ind masyvą kaip indeksą

x1[ind]

# ind yra dvidimensis tad ir atsakymas yra dviejų dimensijų

ind.shape

x1[ind].shape

# Pirmoje dimensijoje mes gauname 1 ir 0 iš x1, antroje dimensijoje -2 ir -1

x2

row = np.array([0, 1])
col = np.array([0, 1])

x2[row, col]

# ### NumPy masyvų karpymas
#
# x1[start:stop:step]

x1[:5]  # pirmi penki elementai

x1[2:]  # nuo antro elemento

x1[::2]  # kas antras elementas

# Kas antras elementas pradedant nuo antro elemento (pirmas ties 0)

x1[1::2]

x1[::-1]  # atvirštine tvarka

x1[5:-2]  # apversti mašyvą ir nuo 5to elemento imti kas antrą elemntą.

# ### Daugiadimensių masyvų karpymas

x2

x2[:2, :3]  # pirmos dvi eilutės ir pirmi trys stulpeliai

x2[:3, ::2]  # trys pirmos eilutės ir kas antras stulpelis nuo pradžių

x2[::-1, ::-1]  # apvertimas

x2[:, 0]  # pirmas stulpelis

x2[0]  # tas pats kaip x2[0,:]

# ## Kopijos
#
# Svarbu! Python kalboje priskyrimai nesukuria tikrų nepriklausomų kopijų

x2

x_change = x2[0, :]
x_change[1] = 55
x_change

x2  # x2 ir x_change pasikeitė

# Iš naujo sukuriam masyvą

x2 = np.arange(0, 12).reshape(2, 6)
x2

# Nepriklausoma kopija sukuriama copy metodu

x2_independent = x2[0, :].copy()
x2_independent[1] = 55
x2

x2_independent

# ### Apjungimas masyvų

np.concatenate([x1, x1])

np.concatenate([x2, x2])  # axis =0

np.concatenate([x2, x2], axis=1)

x1 = np.arange(6)
x2 = np.arange(0, 12).reshape(2, 6)
x2.shape

x1.shape

# x1 forma yra (6,), o x2 (2, 6).
#
# (6,) ir (6,1) turi tik vieną dimensiją.

x1[1]

x1[1, 0]

x1.reshape(6, 1)[5, 0]

# (6,) ir (6,1) arba (1,6) atrodo panašiai bet daugumai metodų jie yra skirtingi.
# (6,) turi tik vieną ašį, o (6,1) reprezentuojamas dviem ašimis.
#
# Pridėti daugiau ašių galime keliais metodais.

x1.reshape(6, 1, 1, 1)

# Norint atlikti veiksmus su šiais masyvais kartu reikia suvienodinti jų
# dimensijas.
# Tai numpy atlieka automatiškai jei tai padaryti įmanoma (broadcasting).
#
# Sujungiam ties pirma ašimi naudodami vstack

np.vstack([x1, x2])

# Tą patį galime padaryt ir su concatenate tik reikia papildomo ašies argumento

np.concatenate([x1.reshape(1, 6), x2], axis=0)

# Ties antra ašimi sujungiame su hstack

np.hstack([x2, x2])

# arba universalia concatenate

np.concatenate([x2, x2], axis=1)

# Trečiame ašimi

np.dstack([x2, x2])

np.concatenate([x2.reshape(2, 6, 1), x2.reshape(2, 6, 1)], axis=2)

# `Split` dalina masyvą ties pasirinktais taškais (pvz 3 ir 5).

x11, x12, x13 = np.split(x1, [3, 5])
print(x11, x12, x13)

# Panašiai kaip ir sujungimo atveju split yra universali funkcija.
# Jos atitikmuo pirmai ašiai vsplit

top, bottom = np.vsplit(x2, [1])
print(top, bottom)

top, bottom = np.split(x2, [1], axis=0)
print(top, bottom)

# Antra ašis

left, right = np.hsplit(x2, [3])
print(left, right)

np.split(x2, [3], axis=1)

# Trečia ašis

np.dsplit(x2.reshape(2, 6, 1), [2])

np.split(x2.reshape(2, 6, 1), [2], axis=2)

# ### Vektorizavimas (ufunc)
#
# NumPy veikia daug greičiau nei standartiniai python metodai.
# Taip yra dėl vektorinio skaičiavimo kompiliuotomis programomis.

# %timeit np.add(5, x1)

# %timeit [x + 5 for x in x1]

# %timeit (5 + x1) # Tas pats kaip np.add

# Dažnos operacijos

np.add(x1, 5)

np.subtract(x1, 5)

np.negative(x1)

np.multiply(x1, 5)

np.divide(x1, 5)

np.floor_divide(x1, 5)

np.power(x1, 5)

np.mod(x1, 5)

np.mean(x1)

np.std(x1)

# Papildomi parametrai operacijoms

y = np.zeros([8])
y

np.multiply(x1, 10, out=y[2:])  # Priskiria ties nurodytomis pozicijomis
y

x = np.arange(1, 6)
x

np.add.reduce(x)  # Kartoja opreraciją kol lieka tik vienas elementas

np.multiply.reduce(x)

np.multiply.accumulate(x)  # taip pat kaip reduce tik visus žingsnius išsaugo

np.multiply.outer(x, x)  # poruotiems elementams

# ## Dimensijų automatinis suvienodinimas (Broadcasting)
#
# NumPy siekdamas maksimalaus greičio vektorizuodamas
# naudoja pora taisyklių atlikdamas veiksmus su skirtingo dydžio masyvais.
#
# Jei turime a ir b masyvus

a = np.ones((2, 3))
a.shape

a

b = np.arange(3)
b.shape

b

# Sumuojant šiuos du masyvus atliekami šie veiksmai tokia tvarka:
#
# Žingsniai: a dimensijos (2,3) ir b (3,).
#
# - `b` tampa (1,3) prie kairės pusės 1 dydžio (np.ones) dimensija pridedama.
# - Pridėta dimensija  prie `b` praplečiama kad atitiktų `a` (b -> (2,3))
# - Tikrinamos ar dabar dimensijos lygios
#
# Pvz 1:

a = np.arange(3).reshape((3, 1))
b = np.arange(3)
a,b

# `b` (3,)-> (1,3) -> ir praplečiama iki (3,3)
#
# `a` taip pat praplečiama (3,1)->(3,3)

a + b

# Pvz 2:

a = np.ones((3, 2))
b = np.arange(3)
a,b

# b (3,) tamp (1,3) -> (3,3)
#
# a neturi vienetinėse dimensijos. (3,2) nėra lygu (3,3)

a + b

# ### Loginiai palyginimai
#
# Python standartiniai palyginimai neveikia su sudėtingesnėmis struktūromis

a = np.ones((2, 3))
b = np.ones((2, 3))

(a==b) and (b>a)

np.logical_and(a==b, b>a)

np.logical_or(a==b, b>a)

# ## Grafikų paišymas (matplotlib)
#
# Python būdama viena iš populiariausių programavimo kalbų turi be galo daug
# specifinių pakuočių vizualizuoti duomenis.
#
# Mes apžvelgsime pačią populiariausią `matplotlib` pakuotę.
#
# - Viena iš senesnių pakuočių.
# - Įmanoma viskas, bet dažnai daug reik rašyti kodo.
# - Sintaksė panaši į naudojamas matlab, julia programavimo kalbose.
# Tad lengva pereiti, adaptuoti kodą.
# - Daug python pakuočių naudoja.
# - Alternatyvos: Seaborn, HoloViews, Altair, Bokeh, plotly
#
# [matplotlib dokumentacija]( https://matplotlib.org/index.html)
#
# Standartiškai pakuotė importuojama `plt` vardu taip trumpinant rašymą

# +
import matplotlib.pyplot as plt
import matplotlib as mpl

# %matplotlib inline
# -

# matplotlib.pyplot yra paišymo branduolys kurį dažniausiai ir naudosime.

x = [1, 2, 3, 4]
y = [1, 1, 0, 1]
plt.plot(x, y);

# ### Python versijų įtaka
#
# matplotlib pakuotė valdo ne vien tik komandas paišymo bet ir renkasi kas ir
# kaip kompiuteryje generuos grafikus.
#
# Nurodžius vietoj inline qt grafikai iššoka

# %matplotlib qt
plt.plot(x, y);

# Taupant laiką mes beveik visada naudosime inline metodą

# %matplotlib inline

# Paišant grafikus ne ipython, o python terminale grafikai nebus
# vaizduojami kol nebus įgyvendinta komanda:

plt.show()

# Po šios komandos norėdami galėti dar keisti paveikslėli reikia įjungti
# interaktyvų paišymą.

plt.ion()

# Jei interaktyvių funkcijų nenorime (pvz jei automatiškai paišome daug grafikų
# ir svarbu optimizuoti resursus) išjungiame ioff metodu

plt.ioff()

# ### Paveikslų sukūrimas ir saugojimas
#
# Norint išsaugoti grafiką dabartinėje aktyvioje direktorijoje

fig = plt.figure() # sukuriam figūrą
plt.plot(x,y) # nupaišome ant jos
fig.savefig('test.png') # užsaugome png formatu

# Norint išsaugoti kitoje vietoje reik nurodyti pilną kelią.
#
# Formatai kuriais galima išsaugoti

fig.canvas.get_supported_filetypes()

# Kurdami figūrą galime nurodyti jos dydį, tada ant figūros nupaišome
# drobę/ašis.

fig = plt.figure(figsize=(6,6))
ax = plt.axes()

# Figūros objektą dažniausiai priskiriame kintamajam `fig`, o ašių `ax`.
# Šių objektų pagalba nurodome tiksliai kur paišyti.
#
# Jei kintamųjų nepriskyrėme juos galime gauti gcf komanda.
# plt.gcf kintamasis saugo paskutinę aktyvią figūrą.

fig = plt.gcf() # get current figure

# Ašis panašiai gauname `gca` komanda

ax = plt.gca() # (get current axes)
ax.plot(x,y)

# Pavyzdžiuose dažnai matysite paišymą atliekama kitokiu stiliumi.
# Vietoj objektų kūrimo dažnai rašomos paišymo komandos kurios užduotis
# automatiškai atlieka paskutiniame aktyviame elemente.

plt.figure()
plt.plot(x,y)

# `plt.komanda`  įgyvendina `komandą` paskutiniame aktyviame elemente.
#
# Tokiu būdu dažnai sutaupoma rašymo vieta, lengviau perskaityt kodą.
# Kitas didelis pranašumas tai kad atmetus plt. dalį komandos tampa tolygios matlab ar julia programavimo kalbų komandoms.
#
# Bet toks stilius sukuria ir daug problemų ir apsunkina kūrimą sudėtingų
# grafikų.
#
# ### Bazė
#
# Pirmiausiai sukursime duomenis tolimesniam paišymui.
#
# `sin_wave`  funkcija generuos sinusoidę kuria nupiešime

# +
import math

def sin_wave(freq,t):
    y = []
    f =freq # Hz
    for x in t:
       x=x/1000
       y.append(math.sin(2*math.pi*x*f))
    return y


def line_points(t,shift):
    y=[]
    for x in t:
        y.append(x+shift)
    return y


# -

t = list(range(0,1000))
fig = plt.figure()
ax = plt.axes()         #  - a) Sukūrimas ašių
ax.plot(t,sin_wave(10,t)) #  - b) paišymas sinusoidės
ax.plot(t,sin_wave(20,t)) #  - c) paišymas tame pačiame grafike
#  fig.show()              #  - d) papildomos komanodos

# Sukurtos funkcijos sinusoidės paišymui neefektyvios.
# Tokiom užduotims mes galime panaudoti NumPy vektorizaciją.

# +
def sin_wave(Hz=10, sample_rate=1000, length_sec=1):
    t = np.linspace(0, length_sec, length_sec * sample_rate, endpoint=False)
    x = np.sin(Hz * 2 * np.pi * t)
    return(t, x)

def line_points(shift, sample_rate=1000, length_sec=1):
    t = np.linspace(0, length_sec, length_sec * sample_rate, endpoint=False)
    x = t+shift
    return(t, x)


# -

fig = plt.figure()
ax = plt.axes()         #  - a) Sukūrimas ašių
ax.plot(*sin_wave(10)) #  - b) paišymas sinusoidės
ax.plot(*sin_wave(20)) #  - c) paišymas tame pačiame grafike
#  fig.show()              #  - d) papildomos komanodos

# ## Pagražinimas
#
# Spalvos priskiriamos automatiškai, bet norint galima nurodyti `color`
# raktažodžiu

ax = plt.axes()
ax.plot(*sin_wave(1), color='blue')         # specifinė spalva
ax.plot(*sin_wave(2), color='g')           # trumpinys (rgbcmyk)
ax.plot(*sin_wave(3), color='0.75')        # tarp 0 ir 1
ax.plot(*sin_wave(4), color='#FFDD44')     # Hex kodas (RRGGBB 00 iki FF)
ax.plot(*sin_wave(5), color=(1.0,0.2,0.3)) # RGB, 0 iki 1
ax.plot(*sin_wave(6), color='chartreuse'); # HTML vardai


# Linijų stilius keičiamas `linestyle` raktažodžiu

fig=plt.figure(figsize=(8,8))
ax = plt.axes()
ax.plot(*line_points(0), linestyle='solid')
ax.plot(*line_points(10), linestyle='dashed')
ax.plot(*line_points(20), linestyle='dashdot')
ax.plot(*line_points(30), linestyle='dotted');

# Arba simboliais

fig=plt.figure(figsize=(8,8))
ax = plt.axes()
ax.plot(*line_points(0), linestyle='-')  # solid
ax.plot(*line_points(10), linestyle='--') # dashed
ax.plot(*line_points(20), linestyle='-.') # dashdot
ax.plot(*line_points(30), linestyle=':'); # dotted

# Priartinimas ir atitolinimas grafiko nustatomas ašių koordinatėmis

fig = plt.figure()
ax = plt.axes()
ax.plot(*line_points(0), linestyle='-')
ax.plot(*line_points(10), linestyle='--')
ax.plot(*line_points(20), linestyle='-.')
ax.plot(*line_points(30), linestyle=':')
ax.set_xlim([0, .5])
ax.set_ylim([0, 5]);
# plt.xlim([0, 100]) # Skiriasi sintaksė
# plt.ylim([0, 100]) # Skiriasi sintaksė

# Apverčiam ašis

fig = plt.figure()
ax = plt.axes()
ax.plot(*line_points(0), linestyle='-')
ax.plot(*line_points(10), linestyle='--')
ax.plot(*line_points(20), linestyle='-.')
ax.plot(*line_points(30), linestyle=':')
ax.set_xlim([0, 1])
ax.set_ylim([30, 0]);

# Tuo pat metu  x ir y galima nustatyti `axis` metodu

fig = plt.figure()
ax = plt.axes()
ax.plot(*line_points(0), linestyle='-')
ax.plot(*line_points(10), linestyle='--')
ax.plot(*line_points(20), linestyle='-.')
ax.plot(*line_points(30), linestyle=':')
ax.axis([0,1,0,30]);

fig = plt.figure()
ax = plt.axes()
ax.plot(*line_points(0), linestyle='-')
ax.plot(*line_points(10), linestyle='--')
ax.plot(*line_points(20), linestyle='-.')
ax.plot(*line_points(30), linestyle=':')
ax.axis('equal')

fig = plt.figure()
ax = plt.axes()
ax.plot(*line_points(0), linestyle='-')
ax.plot(*line_points(10), linestyle='--')
ax.plot(*line_points(20), linestyle='-.')
ax.plot(*line_points(30), linestyle=':')
ax.axis('tight')

# ### Anotacijos

fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(1), label='sin(x)') # legendai skirtas tekstas
ax.set_xlabel("Laikas")
ax.set_ylabel("Amplitudė")
ax.set_title("1 Hz sine wave") # pavadinimas
ax.legend(); # legenda

# `plt` --> xlabel, ylabel title

plt.figure()
plt.plot(*sin_wave(1), label = 'sin(x)')
plt.legend()

# `loc`  parametras nurodo kur atsiras legenda

fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(1), label='1 Hz')
ax.plot(*sin_wave(2), label='2 Hz')
ax.set_xlabel("Laikas")
ax.set_ylabel("Amplitudė")
ax.set_title("Sinusoidės")
ax.legend(loc='upper left',frameon=False)

# Stilių elementų galima nurodyti gana detaliai

fig = plt.figure(figsize=(10,10))
ax = plt.axes()
ax.plot(*sin_wave(1), label='1 Hz')
ax.plot(*sin_wave(2), label='2 Hz')
ax.plot(*sin_wave(3)) # nenurodžius neatsiras legendoje
ax.set_xlabel("Laikas")
ax.set_ylabel("Amplitudė")
ax.set_title("Sinusoidės")
ax.legend(ncol=2, borderpad=1, shadow=True, framealpha=1, fancybox=True, title='Frequency')

# Nenurodžius žymės (label) legendoje nebus įtrauktas elementas.
# Legendą galima nurodyti vėliau

ax.legend(['1 Hz', '2 Hz', '3 Hz'])
fig

# Norint sukurti daugiau negu vieną legendą reikia pridėti naują legendos
# objektą iš matplotlib.

fig1 = plt.figure()
ax1 = plt.axes()
lines = []
lines += ax1.plot(*sin_wave(1))
lines += ax1.plot(*sin_wave(2))
ax1.legend(lines[:1],['1 Hz'],loc='upper left',frameon=False)
leg2 = mpl.legend.Legend(ax1,lines[1:2],['2 Hz'],loc='lower right')
ax1.add_artist(leg2)

# ## Sklaidos grafikai
#
# Pradžioje sugeneruosim atsitiktinių taškų vizualizacijai

t = np.linspace(0, 1, 10, endpoint=False)
points = np.random.random(10)

# Standartinė plot funkcija yra universali.
# Sklaidos grafikus galime brėžti nurodžius taškus žymėti `o` simboliu.

plt.plot(t,points, 'o')

import random
ax = plt.axes()
for symbol in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    ax.plot(random.random(), random.random(), symbol, label=f"symbol={symbol}")
    ax.plot(random.random(), random.random(), symbol)
    ax.plot(random.random(), random.random(), symbol)
    ax.plot(random.random(), random.random(), symbol)
    ax.plot(random.random(), random.random(), symbol)
ax.legend(numpoints=1, loc='upper right')

# Įvairius parametrus galima maišyti ir gauti bet kokį grafiką.

plt.plot(t, points, '-d', color='gray',
         markersize=20, linewidth=5,
         markeredgecolor='gray',
         markerfacecolor='blue',
         markeredgewidth=3)

# ### plt.scatter
#
# Visgi tokiems dažniems grafikams yra specifinės komandos palengvinančios vizualizaciją .

plt.scatter(t,points, marker = 'd')

# `scatter` komanda turi daug metodų būtent šiam vizualizacijos tipui kas
# leidžia daug greičiau pasiekti norimą rezultatą.

x = random.sample(list(range(1000)),20)
y = random.sample(list(range(1000)),20)
colors = random.sample(list(range(1000)),20)
sizes = random.sample(list(range(1000)),20)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5,
            cmap='viridis')
plt.colorbar()
for size in [300, 500, 700]:
    plt.scatter([],[],color='black',alpha=.3,s=size, label=f"{size}")
plt.legend(scatterpoints=1,frameon=False,labelspacing=1,title='Size')


# Scatter funkcija turi daugiau metodų ir parametrų.
# Tai palengvina grafikų kūrimą, bet taip pat ir sulėtina programos darbą.
# Paprastiems sklaidos grafikams turint didelius duomenų masyvus geriau naudoti plot funkciją
#
# ### Spalvų žemėlapiai (colormaps)
#
# Susikuriam funkciją kurios pagalba vaizdinsim žemėlapius

def view_cmap(cmap):
    ax = plt.axes()
    cmap = plt.cm.get_cmap(cmap)
    cmap = cmap(list(range(cmap.N)))
    ax.imshow([cmap],extent=[0,10,0,1])


# Yra be galo daug spalvų žemėlapių, bet juos visus galima padalinti į grupes:
#
# - Nuoseklūs --- tęstinės nepertraukiamos spalvos. Tai dažniausiai naudojami žemėlapiai.
# Juos lengva interpretuoti, dažniausiai spalvos ryškis kinta su
# duomenimis.

view_cmap('binary')

view_cmap('viridis')

# - Išsiskiriantys --- naudojamos skirtingos spalvos.
# Šie žemėlapiai labiausiai tinkami parodyti dvi skirtingas puses.

view_cmap('RdBu')

view_cmap('PuOr')

# - Kokybiniai: daugelio spalvų mišinys

view_cmap('rainbow')

view_cmap('jet')

# ### Spalvų juostos parametrai
#
# Kartais norint paryškinti efektus reikia pakeisti z ašies ribas.

x = random.sample(list(range(1000)),100)
y = random.sample(list(range(1000)),100)
colors = random.sample(list(range(1000)),100)
sizes = random.sample(list(range(1000)),100)
fig = plt.figure()
ax = plt.axes()
scat = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5,
            cmap=plt.cm.get_cmap('viridis',6))
fig.colorbar(scat, extend='max',boundaries=list(range(501)))
# plt.colorbar()
# plt.clim(0, 500)

# ### Statistiniai elementai
#
# Seaborn pakuotė yra geriau pritaikyta šiems elementams vaizduoti.

error=.11
plt.errorbar(*sin_wave(10, sample_rate=100), yerr=error, fmt='o',color='gray',
        ecolor = 'lightgray',elinewidth=3,capsize=0)

# Nurodant nuolatinį nuokrypį užpildome erdvę tarp dviejų verčių

x,y = sin_wave(10)
plt.plot(x,y+.1, 'o-')
plt.fill_between(x,y-.3, y+.3, # arba plt.fill
                 color='gray', alpha=0.2)

# ### Histograma
#
# `hist` paišo histogramas.
# Dauguma parametrų yra tokie patys kaip ir prieš tai minėtuose
# funkcijose.
# Prisideda tik duomenų normalizavimas ir suskirstymas.

plt.hist(y, bins=10, density=True, alpha=.4,
        color='gray',edgecolor='none'
        )

# ## Daugiaašiai grafikai (subplots)
#
# Daugiausiai kontrolės turintis būdas yra sukurti naujas ašis nurodytuose koordinatėse.

fig=plt.figure(figsize=(5,5))
ax1 = plt.axes()
# pradžia nuo figūros kairės, apačios, ilgis, aukštis
ax2 = plt.axes([0.3, 0.5, 0.4, 0.2])

# arba pridedant ašis prie figūros

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8,0.4])
ax2 = fig.add_axes([0.1, 0, 0.8,0.4])

# Paprasčiau yra naudoti `subplot` funkciją kur nurodome skaičių
# stulpelių, eilučių ir kaip jie dalinasi ašis.

fig, ax = plt.subplots(ncols= 2, nrows=3, sharex='col', sharey='row')
for i in range(3):
    for j in range(2):
        ax[i, j].text(0.5, 0.5, str((i, j)), # ax contains all the axes
                      fontsize=18, ha='center')

# Sudėtingesniems grafikams naudojamas `gridspec`

x = random.sample(list(range(1000)),100)
y = random.sample(list(range(1000)),100)
colors = random.sample(list(range(1000)),100)
sizes = random.sample(list(range(1000)),100)
fig = plt.figure()
grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2) # creates 4 by 4 grid with spacing
ax=fig.add_subplot(grid[:-1, 1:]) # subplot will take space from top to 2nd from bottom element and from 2nd element from left to right
ax1=fig.add_subplot(grid[:-1, 0]) # subplot will take space from top to 2nd from bottom element and first from left
ax2=fig.add_subplot(grid[-1, 1:]) # subplot will take space at the bottom and from 2nd element from left to right
ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
ax1.hist(x,orientation='horizontal',color='gray')
ax2.hist(y,orientation='vertical',color='gray')
ax1.invert_xaxis()
ax2.invert_yaxis()

# ### Žymės (ticks)

fig = plt.figure(figsize=(10,10))
ax = plt.axes(xscale='log',yscale='linear')
ax.plot(*sin_wave(2))
ax.grid()

# Grafike matome pagrindinius (major) ir šalutinius (minor) žymenis.
# Jie kontroliuojami per ašių xaxis ir yaxis objektus.
#
# Naudojimo pvz:
#
# Išjungti skaičius ir žymenis

fig = plt.figure(figsize=(10,10))
ax = plt.axes(xscale='log',yscale='linear')
ax.plot(*sin_wave(2))
ax.grid()
ax.yaxis.set_major_locator(plt.NullLocator()) # locator keičia vertes
ax.xaxis.set_major_formatter(plt.NullFormatter()) # formatter keičia išvaizdą.

# Žymenų dažnis

fig = plt.figure(figsize=(10,10))
ax = plt.axes()
ax.plot(*sin_wave(2))
ax.grid()
ax.yaxis.set_major_locator(plt.MaxNLocator(3))
ax.xaxis.set_major_locator(plt.MaxNLocator(3))

# Specifinių žymenų parinkimas

fig = plt.figure(figsize=(10,10))
ax = plt.axes()
ax.plot(* sin_wave(2))
ax.grid()
ax.xaxis.set_major_locator(plt.MultipleLocator(125)) # multiples of
ax.xaxis.set_minor_locator(plt.MultipleLocator(25))

fig = plt.figure(figsize=(10,10))
ax = plt.axes()
ax.plot(*sin_wave(2))
ax.grid()
ax.xaxis.set_major_locator(plt.FixedLocator([145, 333, 897]))
ax.xaxis.set_major_formatter(plt.FixedFormatter(['a', 'b', 'c']))

# Visi parametrai:
#
# Pirmiausiai pasirenkame tarp pagrindinių ir šalutinių žymenų
#
# Tada renkamės tarp locator ir formatter metodų
#
# - locator keičia kur žymenys yra:
#   - AutoLocator: numatytasis
#   - NullLocator: nėr žymenų
#   - FixedLocator: pagal sąrašą
#     - LinearLocator: vienodai išdėstyti tarp dviejų taškų
#     - LogLocator:  logaritminis išdėstymas
#     - MultipleLocator: išdėstyti kas x vienetų
#     - MaxNLocator: automatiškai išdėsto N žymenų
# - formatter pakeičia išvaizdą (tekstą)
#   - ScalarFormatter ar LogFormatter: pagal ašis numatytasis
#   - NullFormatter: nėra teksto
#   - FixedFormatter: žymenys iš sąrašo
#   - FuncFormatter: žymenys iš funkcijos
#
# ### Anotacijos
#
# Norint pavaizduoti tekstą x,y koordinatėse `plt.text(x,y,message,ha='')`

fig = plt.figure(figsize=(20,20))
ax = plt.axes()
ax.plot(*sin_wave(10))
ax.text(0,0,'Start',ha='center')
ax.text(.5,0,'Middle',ha='center')
ax.text(.51,1,'Peak',ha='center')

# X ir Y yra koordinatės duomenų atžvilgiu.
# Kartais norime dėti žymenis grafiko atžvilgiu.

fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])
ax.text(2, 2, ". Data: (2, 2)", transform=ax.transData) # default
ax.text(0.4, 0.5, ". Axes: (0.5, 0.1)", transform=ax.transAxes) # ašių dimensijos
ax.text(0.2, 0.5, ". Figure: (0.2, 0.2)", transform=fig.transFigure) # Figūros dimensijos

# Jei dabar pakeistumėme ašių ribas pasikeis tik `transData` variantas.

fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])
ax.text(2, 2, ". Data: (2, 2)", transform=ax.transData)
ax.text(0.4, 0.5, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.5, ". Figure: (0.2, 0.2)", transform=fig.transFigure)
ax.set_xlim(1, 3)
ax.set_ylim(0,6)

# Rodyklę sukuriame annotate komanda
# annotate(text, xy=koordinatės rodyklės galvos, xytext = teksto koordinatės, arrowprops = rodyklės stilius)

fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(10))
ax.set_ylim(-2,2)
ax.set_xlim(0,1)
ax.annotate('local maximum',xy=(0.12,1),xytext=(0.12,2),arrowprops=dict(facecolor='black',shrink=0.05))
ax.annotate('local minimum', xy=(0.6, -1), xytext=(0.6, -2), bbox=dict(boxstyle="round4,pad=.5", fc="0.9"), arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=-90"))

# ### Stilius grafikų
#
# Numatytasis stilius grafiko: plt.rcParams

style = plt.rcParams.copy()
style

# Galime numatytąjį stilių pakeisti

plt.rc('grid', color='blue', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='in', color='gray')
plt.rc('patch', edgecolor='white')
plt.rc('lines', linewidth=2)
fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(10))
ax.grid()

# Bet lengviau pasirinkti vieną iš daugelio sukurtų stilių

plt.style.available

plt.style.use('default')
fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(10),label='SIN')
ax.legend()

plt.style.use('ggplot')
fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(10),label='SIN')
ax.legend()

plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(10),label='SIN')
ax.legend()

plt.style.use('grayscale')
fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(10),label='SIN')
ax.legend()

plt.style.use('seaborn')
fig = plt.figure()
ax = plt.axes()
ax.plot(*sin_wave(10),label='SIN')
ax.legend()

# [Matplotlib galerija skirtingų grafikų](https://matplotlib.org/gallery.html)






