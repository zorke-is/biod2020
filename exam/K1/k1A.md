---
jupytext:
  cell_metadata_filter: -all
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,py:light,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Bioduomenų surinkimas ir analizė

2020-10-06

Sprendimus siųskite (vardas_pavarde_k1.ipynb; ipynb ir pdf/html formatais)
iki 2020-10-10 23:55 į avoicikas@gmail.com

+++

Įveskite savo vardą ir pavardę

```{raw-cell}

```

Vertinimas

- Komentarai (veiksmų planas ir paaiškinimas) 50 %
- Programos kodas 25 %
- Rezultatas 25 %

+++

---
>> **1. UŽDUOTIS**
>>
>> - Python pagrindai
>>

---

## a) Gauti elementus iš sąrašo

```{code-cell} ipython3
listA1 = ['12345', ['a', 'b', ['c', 'df'], 6], 78]
listA1
```

### 78

```{code-cell} ipython3
listA1[2]
```

### 2

```{code-cell} ipython3
int(listA1[0][1])
```

### b

```{code-cell} ipython3
print(listA1[1][1])
```

### d

```{code-cell} ipython3
print(listA1[1][2][1][0])
```

### a,b

```{code-cell} ipython3
print(listA1[1][0]+','+listA1[1][1])
```

### 234

```{code-cell} ipython3
int(listA1[0][1:4])
```

## b) Naudojant du sąrašus `listB1` ir `listB2` sukurti sąrašą

res_list --> ['two', 4+9j]

```{code-cell} ipython3
listB1 = [1, 'two', False, 3.14, 4+9j]
listB2 = [1, 4]
```

```{code-cell} ipython3
res_list = []
for element in listB2:
    res_list.append(listB1[element])

res_list
```

## c) Gauti elementus iš žodyno

```{code-cell} ipython3
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
```

### Bioethics

```{code-cell} ipython3
Classes["Monday"][0]
```

### Biophysics of Neuron

```{code-cell} ipython3
Classes["Thursday"][2]
```

### ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']

```{code-cell} ipython3
list(Classes.keys())
```

### Thursday

```{code-cell} ipython3
list(Classes.keys())[2]
```

### Nanotechnolog

```{code-cell} ipython3
Classes["Tuesday"][0][12:25]
```

### friday

```{code-cell} ipython3
list(Classes.keys())[4].lower()
```

### d) Sukurti žodyną kurio raktai `keys` skaičiai nuo 1 iki 1000, o vertės `values` raktų kvadratai

Out[1]: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, .....}

```{code-cell} ipython3
zodynas = {}
type(zodynas)

for element in range(1, 1001):
    zodynas[element] = element ** 2

print(zodynas)
```

```{code-cell} ipython3
zodynas = {x:x**2 for x in range(1,1001)}
print(zodynas)
```

### e) Naudojant sąrašų metodus apjungti list2B1, list2B2 ir list2B3 ir gauti list2B4

list2B4 --> [1, 'two', False, 3.14, (3+4j), [[4, 5]], 7, 8]

```{code-cell} ipython3
list2B1 = [1, 'two', False, 3.14, 3+4j]
list2B2 = [[4, 5]]
list2B3 = [7, 8]
```

```{code-cell} ipython3
list2B4 = list2B1.copy()
list2B4.append(list2B2)
list2B4.extend(list2B3)
list2B4
```

### f) Apjungti list2C2 ir list2C3 taip kad gauti

```{code-cell} ipython3
list2C2 = [10, 5, 91, 5, 2, 42, 8, 3, 5, 4, 9, 5, 45, 68, 3, 2, 48]
list2C3 = [0, 3, 5, 88, 94, 5, 21, 9, 5, 0, 0, 5, 6, 0, 0, 8, 5]
```

- list2C1 turintį tik bendrus list2C2 ir list2C3 sąrašams elementus:

list2C1 = [8, 9, 3, 5]

```{code-cell} ipython3
setA = set(list2C2)
setB = set(list2C3)

listC = list(setA.intersection(setB))
listC
```

- list2C4 unikalius elementus

list2C4 = [2, 4, 10, 42, 45, 48, 68, 91]

```{code-cell} ipython3
listD = list(setA.difference(setB))
listD.sort()
listD
```

### g) Parašykite `print` komandą ir suformatuokit tekstą

a) Output:

```{raw-cell}
 one two
 three four      five
 six\                 seven
```

```{code-cell} ipython3
print(f'one two\n three four\t five\nsix\\{"seven".center(40)}')
```

b) Output:

```{raw-cell}
 integer\bfloat\rstring\\boolean{5+5}
```

```{code-cell} ipython3
print(r"integer\bfloat\rstring\\boolean{5+5}")
```

---
>> **2. UŽDUOTIS**
>>
>> Parašykite mini programą/funkciją kuri automatiškai sukurtų jūsų projektų direktorijų medį ir jame esančius startinius failus.
>>
>> Minimalus veikimas:
>>
>> - norime sukurti nauja projektą. pvz kursinis
>> - rašome funkciją mkprojektas(`direktorija`,`kursinis`)
>> - funkcija sukuria:
>>   - Bent 3 direktorijos
>>   - README.txt ar README.md failą kuriame yra įrašytas jūsų vardas
>>
---

mkpr.py file

```{code-cell} ipython3
ls
```

```{code-cell} ipython3
%run mkpr test2
```

---
>> **3. UŽDUOTIS**
>>
>> Dažnai gauname duomenis keistame pavidale ir norėdami juos importuoti
>> darbui turime aprašyti importavimo funkciją
>>
>> Sukurkite funkciją kuri nuskaitytų duomenis pateiktus faile:
>>
>> biod2020/exam/K1/coords.txt
>>
>> Funkcijos išeigoje turi būti keturi sąrašai:
>>
>> - image: talpinantis nuskaitytus paveiksliukų pavadinimus
>> - scale: talpinantis nuskaitytas skales
>> - id: talpinantis eilės numerį
>> - coord: talpinantis koordinates (2d sąrašai sąraše 5x10)
>>
>> image, scale,id, coord = konvertuojam('coords.txt')
>>
>>
---

```{code-cell} ipython3
def readcoords(input):
    tps_file = open(input, 'r')
    tps = tps_file.read().splitlines()
    tps_file.close()
    lm, im, ID, coords_array, sc = [], [], [], [], []
    for i, ln in enumerate(tps):
        if ln.startswith("LM"):
            lm_num = int(ln.split('=')[1])
            lm.append(lm_num)
            coords_mat = []
            for j in range(i + 1, i + 1 + lm_num):
                coords_mat.append([float(element) for element in tps[j].split(' ')])
            coords_array.append(coords_mat)
        if ln.startswith("IMAGE"):
            im.append(ln.split('=')[1])
        if ln.startswith("ID"):
            ID.append(int(ln.split('=')[1]))
        if ln.startswith("SCALE"):
            sc.append(float(ln.split('=')[1]))
    return {'lm': lm, 'im': im, 'id': ID, 'coords': coords_array, 'sc': sc}
```

```{code-cell} ipython3
ats=readcoords('./coords.txt')
ats
```

---
>> **4. UŽDUOTIS**
>>
>> Parašykite programą kuri nuskaitytų visus failų vardus biod2020 direktorijoje ir jos subdirektorijose ir susumuotų juose esančius skaičius
>>
>> K1.ipynb, lect12.py... = 1+1+2...=4
>>
---

```{code-cell} ipython3
import pathlib
import re
def find_files_re(directory, pattern):
    files = [element for element in list(pathlib.Path(directory).rglob("./*"))]
    files = [element for element in files if re.search(pattern, element.name)]
    return files

bioa_dir = pathlib.Path.joinpath(pathlib.Path.home(), "Documents", "biod2020")
file_list = find_files_re(bioa_dir, r".*txt")
file_list
```

```{code-cell} ipython3
len(file_list)
```

```{code-cell} ipython3
numbers_str = [re.findall(r'\d',number.name) for number in file_list]
```

```{code-cell} ipython3
numbers2 = []
for num in numbers_str:
    numbers2.append([int(number) for number in num])
```

```{code-cell} ipython3
sum([sum(element) for element in numbers2])
```

```{code-cell} ipython3

```
