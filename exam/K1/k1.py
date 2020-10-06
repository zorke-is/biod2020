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

# # Bioduomenų surinkimas ir analizė
#
# 2020-10-06
#
# Sprendimus siųskite (vardas_pavarde_k1.ipynb; ipynb ir pdf/html formatais)
# iki 2020-10-10 23:55 į avoicikas@gmail.com

# Įveskite savo vardą ir pavardę

# + active=""
#
# -

# Vertinimas
#
# - Komentarai (veiksmų planas ir paaiškinimas) 50 %
# - Programos kodas 25 %
# - Rezultatas 25 %

# ---
# >> **1. UŽDUOTIS**
# >>
# >> - Python pagrindai
# >>
#
# ---
#
# ## a) Gauti elementus iš sąrašo

listA1 = ['12345', ['a', 'b', ['c', 'df'], 6], 78]
listA1

# ### 78



# ### 2



# ### b



# ### d



# ### a,b



# ### 234



# ## b) Naudojant du sąrašus `listB1` ir `listB2` sukurti sąrašą
#
# res_list --> ['two', 4+9j]

listB1 = [1, 'two', False, 3.14, 4+9j]
listB2 = [1, 4]

res_list =

# ## c) Gauti elementus iš žodyno

Classes = {
            'Monday': ['Bioethics'],
            'Tuesday': ['Biophysical Nanotechnologies'],
            'Thursday': ['Biological Membranes', 'Biophysics of Control Systems', 'Biophysics of Neuron'],
            'Wednesday': ['Cell Technologies', 'Biological data analysis'],
            'Friday': 'Research project',
            'Saturday': 'None',
            'Sunday': 'None'
           }
Classes

# ### Bioethics



# ### Biophysics of Neuron



# ### ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']



# ### Thursday



# ### Nanotechnolog



# ### friday



# ### d) Sukurti žodyną kurio raktai `keys` skaičiai nuo 1 iki 1000, o vertės `values` raktų kvadratai
#
# Out[1]: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, .....}



# ### e) Naudojant sąrašų metodus apjungti list2B1, list2B2 ir list2B3 ir gauti list2B4
#
# list2B4 --> [1, 'two', False, 3.14, (3+4j), [[4, 5]], 7, 8]

list2B1 = [1, 'two', False, 3.14, 3+4j]
list2B2 = [[4, 5]]
list2B3 = [7, 8]

list2B4=

# ### f) Apjungti list2C2 ir list2C3 taip kad gauti

list2C2 = [10, 5, 91, 5, 2, 42, 8, 3, 5, 4, 9, 5, 45, 68, 3, 2, 48]
list2C3 = [0, 3, 5, 88, 94, 5, 21, 9, 5, 0, 0, 5, 6, 0, 0, 8, 5]

# - list2C1 turintį tik bendrus list2C2 ir list2C3 sąrašams elementus:
#
# list2C1 = [8, 9, 3, 5]



# - list2C4 unikalius elementus
#
# list2C4 = [2, 4, 10, 42, 45, 48, 68, 91]



# ### g) Parašykite `print` komandą ir suformatuokit tekstą
#
# a) Output:

# + active=""
#  one two
#  three four      five
#  six\                 seven
# -



# b) Output:

# + active=""
#  integer\bfloat\rstring\\boolean{5+5}
# -



# ---
# >> **2. UŽDUOTIS**
# >>
# >> Parašykite mini programą/funkciją kuri automatiškai sukurtų jūsų projektų direktorijų medį ir jame esančius startinius failus.
# >>
# >> Minimalus veikimas:
# >>
# >> - norime sukurti nauja projektą. pvz kursinis
# >> - rašome funkciją mkprojektas(`direktorija`,`kursinis`)
# >> - funkcija sukuria:
# >>   - Bent 3 direktorijos
# >>   - README.txt ar README.md failą kuriame yra įrašytas jūsų vardas
# >>
# ---



# ---
# >> **3. UŽDUOTIS**
# >>
# >> Dažnai gauname duomenis keistame pavidale ir norėdami juos importuoti
# >> darbui turime aprašyti importavimo funkciją
# >>
# >> Sukurkite funkciją kuri nuskaitytų duomenis pateiktus faile:
# >>
# >> biod2020/exam/K1/coords.txt
# >>
# >> Funkcijos išeigoje turi būti keturi sąrašai:
# >>
# >> - image: talpinantis nuskaitytus paveiksliukų pavadinimus
# >> - scale: talpinantis nuskaitytas skales
# >> - id: talpinantis eilės numerį
# >> - coord: talpinantis koordinates (2d sąrašai sąraše 5x10)
# >>
# >> image, scale,id, coord = konvertuojam('coords.txt')
# >>
# >>
# ---



# ---
# >> **4. UŽDUOTIS**
# >>
# >> Parašykite programą kuri nuskaitytų visus failų vardus biod2020 direktorijoje ir jos subdirektorijose ir susumuotų juose esančius skaičius
# >>
# >> K1.ipynb, lect12.py... = 1+1+2...=4
# >>
# ---


