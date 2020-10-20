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

# # [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
#
# 2020-10-20
#
# - Pandas pagrindai
# - Duomenų manipuliacijos
# - Importavimas
# - Grafikai
# - Stilius

import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ## Pagrindai
#
# [Pandas](https://pandas.pydata.org/)
# praplečia NumPy duomenų struktūromis bei metodais iš
# SAS, STATA, SQL, R data.frame ir panašių duomenų analizės įrankių.
#
# [Dokumentacija](https://pandas.pydata.org/pandas-docs/stable/user_guide/)

# ### [Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)
#
# Pagrindinėse Pandas duomenų struktūros: Series, DataFrame ir Index.
#
# Series - paprasčiausia struktūra reprezentuojanti vienos dimensijos masyvą.

data = pd.Series([0.25, 0.5, 0.75, 1])
data

# Paversti NumPy masyvu duomenis galime

data.values

# Prie paprasto NumPy masyvo pandas prideda stulpelių ir eilučių
# pavadinimus kas įgalina konstruoti loginius sakinius.
# Vertės turi automatiškai priskirtą indeksą, bet galima ir priskirti
# specifinius vardus.

data = pd.Series([0.25, 0.5, 0.75, 1], index=['a', 'b', 'c', 'd'])
data

# Indeksas gali būti bet kokia  tvarka bet kokie simboliai

pd.Series(5, index=[5, 10, 1])  # Vienos vertės Series

pd.Series({2: 'a', 1: 'b', 3: 'c'})

pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 2])  # tik nurodyti lieka

# Skirtingai nuo žodynų Series karpyti duomenis galima raktų pagalba.

tel_dict = {'Ona': 867183231,
            'Tomas': 863173231,
            'Jonas': 867199292,
            'Petras': 860183037,
            'Rita': 864132431}
tel_nr = pd.Series(tel_dict)
tel_nr['Tomas':'Petras']

# ### [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
#
# Svarbiausia struktūra: dvimatis masyvas, lentelė
#
# Lengviausia formuoti iš Series

eil_nr = pd.Series({'Ona': 1,
                    'Tomas': 60,
                    'Jonas': 82,
                    'Petras': 8,
                    'Rita': 11})
eil_nr

firma = pd.Series({'Ona': 'Sony',
                   'Tomas': 'Nokia',
                   'Jonas': 'HTC',
                   'Petras': 'Samsung',
                   'Rita': 'Apple'})
firma

tel_knyga = pd.DataFrame({'tel_nr': tel_nr, 'tel_firma': firma})
tel_knyga

# Formuojant iš kitų elementų pravartu nurodyti ir stulpelių bei eilučių vardus

pd.DataFrame(np.zeros((3, 4)), columns=[
             'a', 'b', 'C', 'd'], index=[100, 200, 300])

# Nenurodžius jie priskiriami automatiškai

pd.DataFrame([[1, 4, 5], [7, 8, 9]])

pd.DataFrame([[[1, 4], [5, 8]], [[9, 8], [7, 5]]])

# ## [Index](https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html)
#
# Pandas indeksą galima naudot kaip atskira duomenų struktūrą.

indA = pd.Index([1, 2, 3, 4])
indA

# Index elementai yra nekeičiami.

indA[1] = 5

# pd.Index turi daug standartinės struktūros `set` operacijų

indB = pd.Index([1, 8, 9, 4])
indB

indA & indB

indA.intersection(indB)

indA | indB

indA ^ indB

# ### Elementų pasiekimas (Series)

data = pd.Series(np.arange(1, 8, 2), index=list('abcd'))
data

data['b']

data[1]

# In tikrina eilučių vardus

'a' in data

# Ne duomenis

1 in data

# Eilučių vardus galime gauti

data.keys()

# Poras vardų ir verčių

list(data.items())

# ### Karpymas (Series)

data['a':'b']

data[0:2]

data[['d', 'a']]

data[(data > 3) & (data < 7)]

data[np.logical_and(data > 3, data < 7)]

# Norint išvengi neaiškumų (kai indeksas pvz yra iš skaičių) naudojami iloc ir loc indeksavimo metodai

data = pd.Series(np.arange(9, 17, 2), index=np.arange(1, 8, 2))
data

# Neaišku ką turim omenyje (indekso eilės nr ar pavadinimą) kai rašom

data[1:3]

data[1]

# .loc visada indekso vertės

data.loc[1:3]

data.loc[1]

data.loc[0]

# .iloc  visada elemento vietos indeksas

data.iloc[1:3]

data.iloc[0]

# ### DataFrame (df) karpymas (slicing) ir elementų paėmimas (indexing)
#
# Norint pasiekti tam tikrą stulpelį geriau naudot jo pilną pavadinimą

tel_knyga.tel_nr

# Per tašką šaukiami ir metodai tad geriau kreiptis laužtiniuose skliaustuose.

tel_knyga['tel_nr']

# Vieni laužtiniai skliaustai gražina Series struktūrą.
# Norint gauti DataFrame reikia naudoti [[]]

tel_knyga[['tel_nr']]

# Karpymas skiriasi nuo indeksavimo
#
# Mes karpome eilutes

tel_knyga[:'Petras']

tel_knyga[:'tel_firma']

# O tiesiogiai kreipiamės į stulpelį

tel_knyga['tel_firma']

tel_knyga['Ona']

# Geriau kaip ir Series naudot iloc ir loc

tel_knyga.iloc[:1, :1]  # iki antro (0,1) elemento

tel_knyga.iloc[1, 1]  # Antras elementas

tel_knyga.iloc[0, 0]  # Pirmas elementas

tel_knyga.loc[:'Tomas', :'tel_firma']

# ### Operacijos su DataFrame (df)

dfA = pd.DataFrame(np.arange(8).reshape(
    2, 4), columns=list('abcd'), index=[1, 2])
dfA

dfB = pd.DataFrame(np.arange(6).reshape(2, 3),
                   columns=list('abd'), index=[1, 2])
dfB

# Skirtingai nuo NumPy galima atlikti operacijas su skirtingų dimensijų
# masyvais.
# Svarbu eilučių/stulpelių pavadinimų sutapimas.

dfA + dfB

dfA.subtract(dfB)

# Operacijas galima atlikti skirtingomis kryptimis, dimensijomis

dfA.subtract(dfA.iloc[1], axis=1)  # axis 1 numatytas

dfA.subtract(dfA.iloc[1, 1])  # axis 1 numatytas

dfA.subtract(dfA['a'], axis=0)

dfA.subtract(dfA.iloc[:1, :2], axis=1)

# ## Daugiau nei dvi dimensijos
#
# Dvimatė lentelė df reprezentuoja vieno dalyvio (subj1), rezultatus (min max) skirtingose sąlygose (baseline ir test)

df = pd.DataFrame(np.arange(4).reshape(2, 2), index=[
                  'baseline', 'test'], columns=['min', 'max'])
df

# Norėdami pridėti daugiau dimensijų į lentelę (kitus dalyvius, etc. ) galime:
#
# - kurti skirtingoms sąlygoms kitą lentelę. Greitai atsirastų be galo daug kintamųjų
# - naudoti NumPy masyvus kur 3 ir 4 dimensijos saugotų dalyvius, laikotarpius.
# Tai dažnas sprendimas kai norim skaičiuoti.
# Bet saugojimui patogiau viska turėti vienoje vietoje
# - naudoti 3 dimensijų pd.Panel arba 4 dimensijų pd.Panel4D.
# Taip sukuriame per daug skirtingo tipo duomenų tampa sunkiau organizuot juos.
# - kurti dvimatę lentelę ir saugoti papildomas dimensijas skirtingais vardais.
# Tampa sunku karpyt ir indeksuot duomenis dėl didelės pavadinimų įvairovės

df = pd.DataFrame(np.arange(16).reshape(4, 4), index=[
                  'baseline2018', 'test2018', 'baseline2019', 'test2019'],
                  columns=['subj1min', 'subj1max', 'subj2min', 'subj2max'])
df

# Dvimatėje lentelėje saugoti daugiau nei dvi dimensijas galima su `pd.MultIndex`

ind = pd.MultiIndex(levels=[['basline', 'test'], [2018, 2019]],
                    codes=[[0, 0, 1, 1], [0, 1, 0, 1]])
df = pd.DataFrame(np.arange(8).reshape(4, 2), index=ind,
                  columns=['min', 'max'])
df

# MultiIndex galima sukurti naudojant kintamuosius: arrays, tuples, dataFrames

# +
# pd.MultiIndex?
# -

index = pd.MultiIndex.from_product([['baseline', 'test'],
                                    [2018, 2019]],
                                   names=['kondicija', 'metai'])
columns = pd.MultiIndex.from_product([['subj1', 'subj2', 'subj3'],
                                      ['min', 'max']],
                                     names=['tiriamasis', 'matavimas'])
data = np.arange(24).reshape(4, 6)
df = pd.DataFrame(data, index=index, columns=columns)
df

# Visus indeksus ir pavadinimus galima sukurti tiesiogiai DataFrame kūrimo metu:

dft = pd.DataFrame(np.arange(8).reshape(4, 2),
                   index=[['baseline', 'baseline', 'testas', 'testas'],
                          [2019, 2018, 2019, 2018]], columns=['min', 'max'])
dft.index.names = ['kondicija', 'metai']
dft

# ### MultiIndex indeksavimas

df['subj1', 'min']

df[:'baseline']

df.iloc[:3, :1]

df.iloc[3:4, 2:4]

df[df < 5]

# Detaliam karpymui pagal vardus  galima naudot IndexSlice objektą
#
# Jo pagalba lengvai išskiriam kiekvieną dimensiją stulpeliuose ir eilutėse.

idx = pd.IndexSlice
df.loc[idx[:, 2018], idx['subj2':'subj3',:]]

df.loc[idx['baseline', 2018], idx['subj2':'subj3']]

df.loc[idx['baseline', 2018], idx['subj2', 'max']]

# ## Filtravimas duomenų
#
# ### `where`

df[df<10]

df[df.isin([2])]

df.where(df<10)

# Taip pat galima pakeisti vertes kurios neatitiko filtro

df.where(df<9, -df)

# `where` gražina kopiją duomenų.
# Norint pakeisti df reikia arba priskirti išeigą arba naudoti opciją `inplace=True`
#
# ### `mask`
#
# Priešingybė `where` metodui

df.mask(df<9)

# ### `query`
#
# query metodas pasiskolintas iš SQL.
#
# Įgalina rašyti užklausas loginiais sakiniais.

df.query('metai > 2018')

df.query('metai > 2018 and kondicija=="baseline"')

# ## Manipuliacijos lentelių
#
# Sumažinti dimensijas

df = df.droplevel(level=1,axis=1)
df

# pakeisti stulpelių vardus galime columns komanda

df.columns

df.columns = ['sub1min','sub1max','sub2min','sub2max','sub3min','sub3max',]
df

# Lenteles performatuoti, ir dimensijas išskleisti ar sutraukti galima daugeliu būdu:

df.unstack(level=1)

df.unstack(level=0)

df.unstack().stack()  # Atgal sugrąžina stack

df_flat = df.reset_index()
df_flat

df_flat.set_index(['kondicija', 'metai'])  # Sugrąžinti atgal

# Žmogui lentelė df yra lengvai skaitoma ir suprantama (plataus formato)

df

df_flat

# Bet rašyti kodą kompiuteriui tokioms lentelėms yra ne visada lengva.
# Metodas 'melt' pertvarko lentelę sutraukdamas indeksus ir stulpelius.

df_flat.melt()

# `id_vars` nurodo stulpelius kurie turi likti ir ju pagrindu formuoja lentelę

df_flat.melt(id_vars=['kondicija'])

df_flat.melt(id_vars=['kondicija', 'metai'])

# ## Sujungimas lentelių
#
# pandas turi funkcija pd.concat kuri panaši i np.concatenate.
#
# pd.concat(objs, axis=0, join='outer',
#           join_axes=None, ignore_index=False,
#           keys=None, levels=None, names=None, verify_integrity=False,
#           copy=True)

dfs1min = df[['sub1min']]
dfs2min = df[['sub2min']]
pd.concat([dfs1min, dfs2min])

pd.concat([df['sub1min'], df['sub2min']], axis=1)

pd.concat([dfs1min, dfs2min], ignore_index=True)

pd.concat([dfs1min, dfs2min], keys=['a', 'b'])

# append paprastesnis metodas

df['sub1min'].append(df['sub2min'])

# Dažnai tenka sujungti lenteles turinčias skirtingus ar tik dalį sutampančiu indeksų:

df1 = pd.DataFrame({'kursas': [1, 2, 3, 4],
                    'paskaita': ['mat', 'bio', 'fiz', 'bio']})
df1

df2 = pd.DataFrame({'paskaita': ['mat', 'bio', 'fiz'],
                    'vieta': ['212', '242', '242']})
df2

pd.concat([df1, df2], sort=True)

# Tik bendrą informaciją palieka join opcija
# (inner = intersection, outer = union, right = raktai iš kairės df, left = raktai is dešinės df)

pd.concat([df1, df2], join='inner')

df1.append(df2, sort=True)

# ### merge
#
# Pandas gali sujungti lenteles atsižvelgdama į jų stulpelių vardus

pd.merge(df1, df2)

# `merge` gali sujungti dvi gana skirtingas lenteles.
#
# df.merge(dfA, # kita lentelė kurią bandom prijungti prie dfA
#          on='col1', # stulpelio vardas kurį naudosime prijungimui (gali
#          buti sąrašas stulepių)
#          suffixes=('_df','_dfA'), # priedas prie stulpelių vardų norint
#          atskirti iš kurios lentelės jis atsirado
#          how='inner', # sujungimo būdas (inner outer right left)
#          rigth_on='col1', # on stuleplis dešinėj lentelėj
#          left_on='col1', # on stulpelis kairėj
#          validate='one_to_one'
# )

dfs1min.merge(dfs2min, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='outer')

df1=df[['sub1min']][:'baseline']
df2=df[['sub2min']]
df1.merge(df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='left')

df1.merge(df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='right')

df1.merge(df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'),
how='inner')

# #### merge_ordered()

pd.merge_ordered(df1,df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'), how='outer')

pd.merge_ordered(df1,df2, on=['metai', 'kondicija'], suffixes=('_df1','_df2'), how='outer',fill_method='ffill')

# ### pivot

df_flat

pd.pivot(data=df_flat,index='kondicija',columns='metai',
values='sub1min')

# ### pivot_table
#
# Performatuoja lentelę ir sutraukia naudodamas aggregate nurodyta metodą

pd.pivot_table(data=df_flat,index='kondicija',columns='metai',
values='sub1min')

dfmelt = df_flat.melt(id_vars=['kondicija','metai'])
dfmelt

# Numatytoje aggregate funkcija vidurkis

pd.pivot_table(data=dfmelt,index='kondicija',columns='metai',
values='value')


# ## [Duomenų importavimas](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)

# +
def find_files(directory, pattern):
    files = []
    p = pathlib.Path(directory).glob(pattern)
    files = [x for x in p]
    return files


directory = '/home/aleks/Documents/biod2020/data/'
pattern = '**/temp.csv'
files = find_files(directory, pattern)
files
# -

# Pandas turi daugybę metodų importuoti duomenis iš skirtingų duomenų
# tipų.
#
# `pd.read_csv` skirtas importuoti csv failus

dfCSV = pd.read_csv(files[0], skiprows=0)
dfCSV

# Dažnai importuoti failai yra dideli ir mes nenorime pavaizduoti visos
# informacijos.
# Norint pavaizduoti pirmas 5 eilutes naudojame komandą `head`

dfCSV.head()

# Kitą eilučių skaičių

dfCSV.head(2)

# Panašiai norint pamatyti paskutines 5 eilutes

dfCSV.tail()

# Grįžtam prie `read_csv` metodo.
# Duomenys dažnai būna suformatuoti unikaliai ir reikia pritaikyti
# naudojamas funkcijas kiekvienam atvejui individualiai.

# +
# pd.read_csv?
# -

# output = pd.read_csv(filename or path , additional options)
#
# - sep --- atskiriamasis elementas, numatytasis yra , (comma separated values)
# - header: eilutę naudot kaip stulpelių vardus
# - names: stulpelių vardai
# - skiprows: praleisti x eilučių prieš importuojant
#
# Importavus duomenis galime apžvelgti įvairiais metodais

dfCSV.describe()

# Galime pasirinkti atsitiktinę imtį:
#
# - replacement: False tą pačią eilutę gražins tik kartą
# - weights: vienodi visiems jei nenustatyta
# - axis
# - random_state

dfCSV.sample(n=3, replace=False)

# Kita informacija apie lentelę

dfCSV.info()

dfCSV.shape

# Norint pasiekti vertes

dfCSV.values

dfCSV.columns

dfCSV.index

# Surūšiuoti indeksą

df.sort_index(level=1,ascending=True)

# Surūšiuoti vertes

dfCSV.sort_values(['Date'], ascending=True)

# ### Datos formatavimas
#
# Kodas| Reikšmė
# ---|---
# # %Y| Metai 1999
# # %m| Mėnuo 03
# # %d| Diena 01
# # %H | Valanda (24)
# # %M | Minutė 09
# # %S | Sekundė 05

dfCSV['Date']=pd.to_datetime(dfCSV['Date'], format='%Y-%m-%d')

dfCSV.info()

# ### `Groupby`
#
# Duomenis galima sugrupuoti `groupby` metodu. Panašiai kaip ir
# pivot_table.
# Šis metodas veikia trimis etapais:
#
# - Padalinimas nurodytais parametrais
# - Funkcijos pritaikymas
# - Surinkimas atgal

dfCSV.groupby('Source').mean()

dfCSV.groupby('Source').count()

dfCSV.groupby('Source').describe()

# Groupby su multiIndex

df

df.groupby(level=0).mean()

df.groupby(level=1).mean()

df.groupby(level=0, axis=1).mean()

# Grupės pasirinkimas

dfCSV.groupby('Source').get_group('GCAG').head()

# ### Aggregate
#
# `aggregate` funkcija kartu su `groupby` leidžia pritaikyti visas
# funkcijas.

dfCSV.groupby('Source').aggregate([min, np.mean, 'count'])

# Skirtingiems stulpeliams galia pritaikyti skirtingas funkcijas  su žodynu

dfCSV.head()

dfCSV.groupby('Source').aggregate({'Date': min, 'Mean': 'mean'})

# ### Iteravimas per duomenis
#
# #### iterrows

for i, row in dfCSV.head(5).iterrows():
    print(row['Date'])

# #### itertuples

for namedtuplerow in dfCSV.head(5).itertuples():
  print(namedtuplerow.Date)

#   
# #### Apply
#
# Kiekvienai eilutei pritaiko funkciją

dfCSV.apply(np.max, axis=0)

# ## [Grafikai](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
#
# Pandas grafikus galima koreguoti matplotlib pakuotės komandomis.

dfCSV.pivot(index='Date', columns='Source',
            values='Mean').plot(figsize=(8, 8));

# Raktažodis `kind` lemia grafiko tipą

dfCSV.pivot(index='Date', columns='Source', values='Mean').plot(
    figsize=(5, 5), kind='box');

dfCSV.pivot(index='Date', columns='Source', values='Mean').plot(
    figsize=(10, 10), kind='hist', alpha=0.5, stacked=False);

dfCSV.pivot(index='Date', columns='Source', values='Mean').plot(
    figsize=(10, 10), subplots=True, layout=(2, 1), sharex=True);

# ## [Stilius](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)
#
# Lentelių ir kitų pandas elementų stilių/vizualizaciją galima koreguoti.
#
# Kai spausdinam ilgą lentelę pandas pavaizduoja tik dalį.
# Maksimalus skaičius eilučių kurias dar vaizduoja pilnai nustatomas `max_rows` opcija.

mm = pd.options.display.max_rows
mm

pd.Series(np.arange(mm))

# Dar vieno elemento pridėjimas pakeičia vizualizaciją

pd.Series(np.arange(mm+1))

# Parametrus galime keisti tiesiogiai arba su metodais:
# get_option, set_option, reset_option
#
# Visus parametrus galime matyti

pd.describe_option()

# Parametrus galime filtruoti su regex

pd.describe_option('^display*')

# Norint kad parametrai išliktu juos galime surašyti į ipython starto failą (Linux, ~/.ipython/profile_default/startup).

dfCSV


# Lentelės vaizdą taip pat galime pakeisti
#
# Pvz visas vertes mažesnes už 6 galime pavaizduoti raudona spalva.

# +
def color_red(val):
    color = 'red' if val < 6 else 'black'
    return 'color: %s' % color


s = df.style.applymap(color_red)
s


# -

# Arba

# +
def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]


df.style.apply(highlight_max)
# -

# Lab work:

# - documentation
# - datacamp

# ![pandas](../images/datacamp.png)

# Skill track | Course
# ---|---
# Importing & Cleaning Data with Python | Introduction to importing...
# Data Manipulation with Python | Data manipulation with pandas


