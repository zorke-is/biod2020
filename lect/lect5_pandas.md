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

# [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)

2020-10-20

- Pandas pagrindai
- Duomenų manipuliacijos
- Importavimas
- Grafikai
- Stilius

```{code-cell} ipython3
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## Pagrindai

[Pandas](https://pandas.pydata.org/)
praplečia NumPy duomenų struktūromis bei metodais iš
SAS, STATA, SQL, R data.frame ir panašių duomenų analizės įrankių.

[Dokumentacija](https://pandas.pydata.org/pandas-docs/stable/user_guide/)

+++

### [Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

Pagrindinėse Pandas duomenų struktūros: Series, DataFrame ir Index.

Series - paprasčiausia struktūra reprezentuojanti vienos dimensijos masyvą.

```{code-cell} ipython3
data = pd.Series([0.25, 0.5, 0.75, 1])
data
```

Paversti NumPy masyvu duomenis galime

```{code-cell} ipython3
data.values
```

Prie paprasto NumPy masyvo pandas prideda stulpelių ir eilučių
pavadinimus kas įgalina konstruoti loginius sakinius.
Vertės turi automatiškai priskirtą indeksą, bet galima ir priskirti
specifinius vardus.

```{code-cell} ipython3
data = pd.Series([0.25, 0.5, 0.75, 1], index=['a', 'b', 'c', 'd'])
data
```

Indeksas gali būti bet kokia  tvarka bet kokie simboliai

```{code-cell} ipython3
pd.Series(5, index=[5, 10, 1])  # Vienos vertės Series
```

```{code-cell} ipython3
pd.Series({2: 'a', 1: 'b', 3: 'c'})
```

```{code-cell} ipython3
pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 2])  # tik nurodyti lieka
```

Skirtingai nuo žodynų Series karpyti duomenis galima raktų pagalba.

```{code-cell} ipython3
tel_dict = {'Ona': 867183231,
            'Tomas': 863173231,
            'Jonas': 867199292,
            'Petras': 860183037,
            'Rita': 864132431}
tel_nr = pd.Series(tel_dict)
tel_nr['Tomas':'Petras']
```

### [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

Svarbiausia struktūra: dvimatis masyvas, lentelė

Lengviausia formuoti iš Series

```{code-cell} ipython3
eil_nr = pd.Series({'Ona': 1,
                    'Tomas': 60,
                    'Jonas': 82,
                    'Petras': 8,
                    'Rita': 11})
eil_nr
```

```{code-cell} ipython3
firma = pd.Series({'Ona': 'Sony',
                   'Tomas': 'Nokia',
                   'Jonas': 'HTC',
                   'Petras': 'Samsung',
                   'Rita': 'Apple'})
firma
```

```{code-cell} ipython3
tel_knyga = pd.DataFrame({'tel_nr': tel_nr, 'tel_firma': firma})
tel_knyga
```

Formuojant iš kitų elementų pravartu nurodyti ir stulpelių bei eilučių vardus

```{code-cell} ipython3
pd.DataFrame(np.zeros((3, 4)), columns=[
             'a', 'b', 'C', 'd'], index=[100, 200, 300])
```

Nenurodžius jie priskiriami automatiškai

```{code-cell} ipython3
pd.DataFrame([[1, 4, 5], [7, 8, 9]])
```

```{code-cell} ipython3
pd.DataFrame([[[1, 4], [5, 8]], [[9, 8], [7, 5]]])
```

## [Index](https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html)

Pandas indeksą galima naudot kaip atskira duomenų struktūrą.

```{code-cell} ipython3
indA = pd.Index([1, 2, 3, 4])
indA
```

Index elementai yra nekeičiami.

```{code-cell} ipython3
indA[1] = 5
```

pd.Index turi daug standartinės struktūros `set` operacijų

```{code-cell} ipython3
indB = pd.Index([1, 8, 9, 4])
indB
```

```{code-cell} ipython3
indA & indB
```

```{code-cell} ipython3
indA.intersection(indB)
```

```{code-cell} ipython3
indA | indB
```

```{code-cell} ipython3
indA ^ indB
```

### Elementų pasiekimas (Series)

```{code-cell} ipython3
data = pd.Series(np.arange(1, 8, 2), index=list('abcd'))
data
```

```{code-cell} ipython3
data['b']
```

```{code-cell} ipython3
data[1]
```

In tikrina eilučių vardus

```{code-cell} ipython3
'a' in data
```

Ne duomenis

```{code-cell} ipython3
1 in data
```

Eilučių vardus galime gauti

```{code-cell} ipython3
data.keys()
```

Poras vardų ir verčių

```{code-cell} ipython3
list(data.items())
```

### Karpymas (Series)

```{code-cell} ipython3
data['a':'b']
```

```{code-cell} ipython3
data[0:2]
```

```{code-cell} ipython3
data[['d', 'a']]
```

```{code-cell} ipython3
data[(data > 3) & (data < 7)]
```

```{code-cell} ipython3
data[np.logical_and(data > 3, data < 7)]
```

Norint išvengi neaiškumų (kai indeksas pvz yra iš skaičių) naudojami iloc ir loc indeksavimo metodai

```{code-cell} ipython3
data = pd.Series(np.arange(9, 17, 2), index=np.arange(1, 8, 2))
data
```

Neaišku ką turim omenyje (indekso eilės nr ar pavadinimą) kai rašom

```{code-cell} ipython3
data[1:3]
```

```{code-cell} ipython3
data[1]
```

.loc visada indekso vertės

```{code-cell} ipython3
data.loc[1:3]
```

```{code-cell} ipython3
data.loc[1]
```

```{code-cell} ipython3
data.loc[0]
```

.iloc  visada elemento vietos indeksas

```{code-cell} ipython3
data.iloc[1:3]
```

```{code-cell} ipython3
data.iloc[0]
```

### DataFrame (df) karpymas (slicing) ir elementų paėmimas (indexing)

Norint pasiekti tam tikrą stulpelį geriau naudot jo pilną pavadinimą

```{code-cell} ipython3
tel_knyga.tel_nr
```

Per tašką šaukiami ir metodai tad geriau kreiptis laužtiniuose skliaustuose.

```{code-cell} ipython3
tel_knyga['tel_nr']
```

Vieni laužtiniai skliaustai gražina Series struktūrą.
Norint gauti DataFrame reikia naudoti [[]]

```{code-cell} ipython3
tel_knyga[['tel_nr']]
```

Karpymas skiriasi nuo indeksavimo

Mes karpome eilutes

```{code-cell} ipython3
tel_knyga[:'Petras']
```

```{code-cell} ipython3
tel_knyga[:'tel_firma']
```

O tiesiogiai kreipiamės į stulpelį

```{code-cell} ipython3
tel_knyga['tel_firma']
```

```{code-cell} ipython3
tel_knyga['Ona']
```

Geriau kaip ir Series naudot iloc ir loc

```{code-cell} ipython3
tel_knyga.iloc[:1, :1]  # iki antro (0,1) elemento
```

```{code-cell} ipython3
tel_knyga.iloc[1, 1]  # Antras elementas
```

```{code-cell} ipython3
tel_knyga.iloc[0, 0]  # Pirmas elementas
```

```{code-cell} ipython3
tel_knyga.loc[:'Tomas', :'tel_firma']
```

### Operacijos su DataFrame (df)

```{code-cell} ipython3
dfA = pd.DataFrame(np.arange(8).reshape(
    2, 4), columns=list('abcd'), index=[1, 2])
dfA
```

```{code-cell} ipython3
dfB = pd.DataFrame(np.arange(6).reshape(2, 3),
                   columns=list('abd'), index=[1, 2])
dfB
```

Skirtingai nuo NumPy galima atlikti operacijas su skirtingų dimensijų
masyvais.
Svarbu eilučių/stulpelių pavadinimų sutapimas.

```{code-cell} ipython3
dfA + dfB
```

```{code-cell} ipython3
dfA.subtract(dfB)
```

Operacijas galima atlikti skirtingomis kryptimis, dimensijomis

```{code-cell} ipython3
dfA.subtract(dfA.iloc[1], axis=1)  # axis 1 numatytas
```

```{code-cell} ipython3
dfA.subtract(dfA.iloc[1, 1])  # axis 1 numatytas
```

```{code-cell} ipython3
dfA.subtract(dfA['a'], axis=0)
```

```{code-cell} ipython3
dfA.subtract(dfA.iloc[:1, :2], axis=1)
```

## Daugiau nei dvi dimensijos

Dvimatė lentelė df reprezentuoja vieno dalyvio (subj1), rezultatus (min max) skirtingose sąlygose (baseline ir test)

```{code-cell} ipython3
df = pd.DataFrame(np.arange(4).reshape(2, 2), index=[
                  'baseline', 'test'], columns=['min', 'max'])
df
```

Norėdami pridėti daugiau dimensijų į lentelę (kitus dalyvius, etc. ) galime:

- kurti skirtingoms sąlygoms kitą lentelę. Greitai atsirastų be galo daug kintamųjų
- naudoti NumPy masyvus kur 3 ir 4 dimensijos saugotų dalyvius, laikotarpius.
Tai dažnas sprendimas kai norim skaičiuoti.
Bet saugojimui patogiau viska turėti vienoje vietoje
- naudoti 3 dimensijų pd.Panel arba 4 dimensijų pd.Panel4D.
Taip sukuriame per daug skirtingo tipo duomenų tampa sunkiau organizuot juos.
- kurti dvimatę lentelę ir saugoti papildomas dimensijas skirtingais vardais.
Tampa sunku karpyt ir indeksuot duomenis dėl didelės pavadinimų įvairovės

```{code-cell} ipython3
df = pd.DataFrame(np.arange(16).reshape(4, 4), index=[
                  'baseline2018', 'test2018', 'baseline2019', 'test2019'],
                  columns=['subj1min', 'subj1max', 'subj2min', 'subj2max'])
df
```

Dvimatėje lentelėje saugoti daugiau nei dvi dimensijas galima su `pd.MultIndex`

```{code-cell} ipython3
ind = pd.MultiIndex(levels=[['basline', 'test'], [2018, 2019]],
                    codes=[[0, 0, 1, 1], [0, 1, 0, 1]])
df = pd.DataFrame(np.arange(8).reshape(4, 2), index=ind,
                  columns=['min', 'max'])
df
```

MultiIndex galima sukurti naudojant kintamuosius: arrays, tuples, dataFrames

```{code-cell} ipython3
pd.MultiIndex?
```

```{code-cell} ipython3
index = pd.MultiIndex.from_product([['baseline', 'test'],
                                    [2018, 2019]],
                                   names=['kondicija', 'metai'])
columns = pd.MultiIndex.from_product([['subj1', 'subj2', 'subj3'],
                                      ['min', 'max']],
                                     names=['tiriamasis', 'matavimas'])
data = np.arange(24).reshape(4, 6)
df = pd.DataFrame(data, index=index, columns=columns)
df
```

Visus indeksus ir pavadinimus galima sukurti tiesiogiai DataFrame kūrimo metu:

```{code-cell} ipython3
dft = pd.DataFrame(np.arange(8).reshape(4, 2),
                   index=[['baseline', 'baseline', 'testas', 'testas'],
                          [2019, 2018, 2019, 2018]], columns=['min', 'max'])
dft.index.names = ['kondicija', 'metai']
dft
```

### MultiIndex indeksavimas

```{code-cell} ipython3
df['subj1', 'min']
```

```{code-cell} ipython3
df[:'baseline']
```

```{code-cell} ipython3
df.iloc[:3, :1]
```

```{code-cell} ipython3
df.iloc[3:4, 2:4]
```

```{code-cell} ipython3
df[df < 5]
```

Detaliam karpymui pagal vardus  galima naudot IndexSlice objektą

Jo pagalba lengvai išskiriam kiekvieną dimensiją stulpeliuose ir eilutėse.

```{code-cell} ipython3
idx = pd.IndexSlice
df.loc[idx[:, 2018], idx['subj2':'subj3',:]]
```

```{code-cell} ipython3
df.loc[idx['baseline', 2018], idx['subj2':'subj3']]
```

```{code-cell} ipython3
df.loc[idx['baseline', 2018], idx['subj2', 'max']]
```

## Filtravimas duomenų

### `where`

```{code-cell} ipython3
df[df<10]
```

```{code-cell} ipython3
df[df.isin([2])]
```

```{code-cell} ipython3
df.where(df<10)
```

Taip pat galima pakeisti vertes kurios neatitiko filtro

```{code-cell} ipython3
df.where(df<9, -df)
```

`where` gražina kopiją duomenų.
Norint pakeisti df reikia arba priskirti išeigą arba naudoti opciją `inplace=True`

### `mask`

Priešingybė `where` metodui

```{code-cell} ipython3
df.mask(df<9)
```

### `query`

query metodas pasiskolintas iš SQL.

Įgalina rašyti užklausas loginiais sakiniais.

```{code-cell} ipython3
df.query('metai > 2018')
```

```{code-cell} ipython3
df.query('metai > 2018 and kondicija=="baseline"')
```

## Manipuliacijos lentelių

Sumažinti dimensijas

```{code-cell} ipython3
df = df.droplevel(level=1,axis=1)
df
```

pakeisti stulpelių vardus galime columns komanda

```{code-cell} ipython3
df.columns
```

```{code-cell} ipython3
df.columns = ['sub1min','sub1max','sub2min','sub2max','sub3min','sub3max',]
df
```

Lenteles performatuoti, ir dimensijas išskleisti ar sutraukti galima daugeliu būdu:

```{code-cell} ipython3
df.unstack(level=1)
```

```{code-cell} ipython3
df.unstack(level=0)
```

```{code-cell} ipython3
df.unstack().stack()  # Atgal sugrąžina stack
```

```{code-cell} ipython3
df_flat = df.reset_index()
df_flat
```

```{code-cell} ipython3
df_flat.set_index(['kondicija', 'metai'])  # Sugrąžinti atgal
```

Žmogui lentelė df yra lengvai skaitoma ir suprantama (plataus formato)

```{code-cell} ipython3
df
```

```{code-cell} ipython3
df_flat
```

Bet rašyti kodą kompiuteriui tokioms lentelėms yra ne visada lengva.
Metodas 'melt' pertvarko lentelę sutraukdamas indeksus ir stulpelius.

```{code-cell} ipython3
df_flat.melt()
```

`id_vars` nurodo stulpelius kurie turi likti ir ju pagrindu formuoja lentelę

```{code-cell} ipython3
df_flat.melt(id_vars=['kondicija'])
```

```{code-cell} ipython3
df_flat.melt(id_vars=['kondicija', 'metai'])
```

## Sujungimas lentelių

pandas turi funkcija pd.concat kuri panaši i np.concatenate.

pd.concat(objs, axis=0, join='outer',
          join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)

```{code-cell} ipython3
dfs1min = df[['sub1min']]
dfs2min = df[['sub2min']]
pd.concat([dfs1min, dfs2min])
```

```{code-cell} ipython3
pd.concat([df['sub1min'], df['sub2min']], axis=1)
```

```{code-cell} ipython3
pd.concat([dfs1min, dfs2min], ignore_index=True)
```

```{code-cell} ipython3
pd.concat([dfs1min, dfs2min], keys=['a', 'b'])
```

append paprastesnis metodas

```{code-cell} ipython3
df['sub1min'].append(df['sub2min'])
```

Dažnai tenka sujungti lenteles turinčias skirtingus ar tik dalį sutampančiu indeksų:

```{code-cell} ipython3
df1 = pd.DataFrame({'kursas': [1, 2, 3, 4],
                    'paskaita': ['mat', 'bio', 'fiz', 'bio']})
df1
```

```{code-cell} ipython3
df2 = pd.DataFrame({'paskaita': ['mat', 'bio', 'fiz'],
                    'vieta': ['212', '242', '242']})
df2
```

```{code-cell} ipython3
pd.concat([df1, df2], sort=True)
```

Tik bendrą informaciją palieka join opcija
(inner = intersection, outer = union, right = raktai iš kairės df, left = raktai is dešinės df)

```{code-cell} ipython3
pd.concat([df1, df2], join='inner')
```

```{code-cell} ipython3
df1.append(df2, sort=True)
```

### merge

Pandas gali sujungti lenteles atsižvelgdama į jų stulpelių vardus

```{code-cell} ipython3
pd.merge(df1, df2)
```

`merge` gali sujungti dvi gana skirtingas lenteles.

df.merge(dfA, # kita lentelė kurią bandom prijungti prie dfA
         on='col1', # stulpelio vardas kurį naudosime prijungimui (gali
         buti sąrašas stulepių)
         suffixes=('_df','_dfA'), # priedas prie stulpelių vardų norint
         atskirti iš kurios lentelės jis atsirado
         how='inner', # sujungimo būdas (inner outer right left)
         rigth_on='col1', # on stuleplis dešinėj lentelėj
         left_on='col1', # on stulpelis kairėj
         validate='one_to_one'
)

```{code-cell} ipython3
dfs1min.merge(dfs2min, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='outer')
```

```{code-cell} ipython3
df1=df[['sub1min']][:'baseline']
df2=df[['sub2min']]
df1.merge(df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='left')
```

```{code-cell} ipython3
df1.merge(df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='right')
```

```{code-cell} ipython3
df1.merge(df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='inner')
```

#### merge_ordered()

```{code-cell} ipython3
pd.merge_ordered(df1,df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'), how='outer')
```

```{code-cell} ipython3
pd.merge_ordered(df1,df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'), how='outer',fill_method='ffill')
```

### pivot

```{code-cell} ipython3
df_flat
```

```{code-cell} ipython3
pd.pivot(data=df_flat,index='kondicija',columns='metai',
values='sub1min')
```

### pivot_table

Performatuoja lentelę ir sutraukia naudodamas aggregate nurodyta metodą

```{code-cell} ipython3
pd.pivot_table(data=df_flat,index='kondicija',columns='metai',
values='sub1min')
```

```{code-cell} ipython3
dfmelt = df_flat.melt(id_vars=['kondicija','metai'])
dfmelt
```

Numatytoje aggregate funkcija vidurkis

```{code-cell} ipython3
pd.pivot_table(data=dfmelt,index='kondicija',columns='metai',
values='value')
```

## [Duomenų importavimas](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)

```{code-cell} ipython3
def find_files(directory, pattern):
    files = []
    p = pathlib.Path(directory).glob(pattern)
    files = [x for x in p]
    return files


directory = '/home/aleks/Documents/biod2020/data/'
pattern = '**/temp.csv'
files = find_files(directory, pattern)
files
```

Pandas turi daugybę metodų importuoti duomenis iš skirtingų duomenų
tipų.

`pd.read_csv` skirtas importuoti csv failus

```{code-cell} ipython3
dfCSV = pd.read_csv(files[0], skiprows=0)
dfCSV
```

Dažnai importuoti failai yra dideli ir mes nenorime pavaizduoti visos
informacijos.
Norint pavaizduoti pirmas 5 eilutes naudojame komandą `head`

```{code-cell} ipython3
dfCSV.head()
```

Kitą eilučių skaičių

```{code-cell} ipython3
dfCSV.head(2)
```

Panašiai norint pamatyti paskutines 5 eilutes

```{code-cell} ipython3
dfCSV.tail()
```

Grįžtam prie `read_csv` metodo.
Duomenys dažnai būna suformatuoti unikaliai ir reikia pritaikyti
naudojamas funkcijas kiekvienam atvejui individualiai.

```{code-cell} ipython3
pd.read_csv?
```

output = pd.read_csv(filename or path , additional options)

- sep --- atskiriamasis elementas, numatytasis yra , (comma separated values)
- header: eilutę naudot kaip stulpelių vardus
- names: stulpelių vardai
- skiprows: praleisti x eilučių prieš importuojant

Importavus duomenis galime apžvelgti įvairiais metodais

```{code-cell} ipython3
dfCSV.describe()
```

Galime pasirinkti atsitiktinę imtį:

- replacement: False tą pačią eilutę gražins tik kartą
- weights: vienodi visiems jei nenustatyta
- axis
- random_state

```{code-cell} ipython3
dfCSV.sample(n=3, replace=False)
```

Kita informacija apie lentelę

```{code-cell} ipython3
dfCSV.info()
```

```{code-cell} ipython3
dfCSV.shape
```

Norint pasiekti vertes

```{code-cell} ipython3
dfCSV.values
```

```{code-cell} ipython3
dfCSV.columns
```

```{code-cell} ipython3
dfCSV.index
```

Surūšiuoti indeksą

```{code-cell} ipython3
df.sort_index(level=1,ascending=True)
```

Surūšiuoti vertes

```{code-cell} ipython3
dfCSV.sort_values(['Date'], ascending=True)
```

### Datos formatavimas

Kodas| Reikšmė
---|---
%Y| Metai 1999
%m| Mėnuo 03
%d| Diena 01
%H | Valanda (24)
%M | Minutė 09
%S | Sekundė 05

```{code-cell} ipython3
dfCSV['Date']=pd.to_datetime(dfCSV['Date'], format='%Y-%m-%d')
```

```{code-cell} ipython3
dfCSV.info()
```

### `Groupby`

Duomenis galima sugrupuoti `groupby` metodu. Panašiai kaip ir
pivot_table.
Šis metodas veikia trimis etapais:

- Padalinimas nurodytais parametrais
- Funkcijos pritaikymas
- Surinkimas atgal

```{code-cell} ipython3
dfCSV.groupby('Source').mean()
```

```{code-cell} ipython3
dfCSV.groupby('Source').count()
```

```{code-cell} ipython3
dfCSV.groupby('Source').describe()
```

Groupby su multiIndex

```{code-cell} ipython3
df
```

```{code-cell} ipython3
df.groupby(level=0).mean()
```

```{code-cell} ipython3
df.groupby(level=1).mean()
```

```{code-cell} ipython3
df.groupby(level=0, axis=1).mean()
```

Grupės pasirinkimas

```{code-cell} ipython3
dfCSV.groupby('Source').get_group('GCAG').head()
```

### Aggregate

`aggregate` funkcija kartu su `groupby` leidžia pritaikyti visas
funkcijas.

```{code-cell} ipython3
dfCSV.groupby('Source').aggregate([min, np.mean, 'count'])
```

Skirtingiems stulpeliams galia pritaikyti skirtingas funkcijas  su žodynu

```{code-cell} ipython3
dfCSV.head()
```

```{code-cell} ipython3
dfCSV.groupby('Source').aggregate({'Date': min, 'Mean': 'mean'})
```

### Iteravimas per duomenis

#### iterrows

```{code-cell} ipython3
for i, row in dfCSV.head(5).iterrows():
    print(row['Date'])
```

#### itertuples

```{code-cell} ipython3
for namedtuplerow in dfCSV.head(5).itertuples():
  print(namedtuplerow.Date)
```

  
#### Apply

Kiekvienai eilutei pritaiko funkciją

```{code-cell} ipython3
dfCSV.apply(np.max, axis=0)
```

## [Grafikai](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

Pandas grafikus galima koreguoti matplotlib pakuotės komandomis.

```{code-cell} ipython3
dfCSV.pivot(index='Date', columns='Source',
            values='Mean').plot(figsize=(8, 8));
```

Raktažodis `kind` lemia grafiko tipą

```{code-cell} ipython3
dfCSV.pivot(index='Date', columns='Source', values='Mean').plot(
    figsize=(5, 5), kind='box');
```

```{code-cell} ipython3
dfCSV.pivot(index='Date', columns='Source', values='Mean').plot(
    figsize=(10, 10), kind='hist', alpha=0.5, stacked=False);
```

```{code-cell} ipython3
dfCSV.pivot(index='Date', columns='Source', values='Mean').plot(
    figsize=(10, 10), subplots=True, layout=(2, 1), sharex=True);
```

## [Stilius](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)

Lentelių ir kitų pandas elementų stilių/vizualizaciją galima koreguoti.

Kai spausdinam ilgą lentelę pandas pavaizduoja tik dalį.
Maksimalus skaičius eilučių kurias dar vaizduoja pilnai nustatomas `max_rows` opcija.

```{code-cell} ipython3
mm = pd.options.display.max_rows
mm
```

```{code-cell} ipython3
pd.Series(np.arange(mm))
```

Dar vieno elemento pridėjimas pakeičia vizualizaciją

```{code-cell} ipython3
pd.Series(np.arange(mm+1))
```

Parametrus galime keisti tiesiogiai arba su metodais:
get_option, set_option, reset_option

Visus parametrus galime matyti

```{code-cell} ipython3
pd.describe_option()
```

Parametrus galime filtruoti su regex

```{code-cell} ipython3
pd.describe_option('^display*')
```

Norint kad parametrai išliktu juos galime surašyti į ipython starto failą (Linux, ~/.ipython/profile_default/startup).

```{code-cell} ipython3
dfCSV
```

Lentelės vaizdą taip pat galime pakeisti

Pvz visas vertes mažesnes už 6 galime pavaizduoti raudona spalva.

```{code-cell} ipython3
def color_red(val):
    color = 'red' if val < 6 else 'black'
    return 'color: %s' % color


s = df.style.applymap(color_red)
s
```

Arba

```{code-cell} ipython3
def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]


df.style.apply(highlight_max)
```

Lab work:

+++

- documentation
- datacamp

+++

![pandas](../images/datacamp.png)

+++

Skill track | Course
---|---
Importing & Cleaning Data with Python | Introduction to importing...
Data Manipulation with Python | Data manipulation with pandas

```{code-cell} ipython3

```
