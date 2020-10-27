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

# # Duomenų tvarkymas
#
# 2020-10-27
#
# - Trūkstamos vertės
# - Duomenų tvarkymas
# - Interpoliacija

import datetime
import re
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.signal as signal
sns.set()

# ## Trūkstamos vertės
#
# Duomenys retai kada būna tvarkingi.
# Tyrimuose neišvengiamai supainiojami pavadinimai, praleidžiami tyrimo etapai.
# Duomenų masyvų dimensijos ar tyrimų eiga nesutampa ir t.t.
# Viena iš dažniausių problemų --- trūkstamos vertės.
#
# Python kalba turi specifinį objektą trūkstamoms vertėms reprezentuoti -- `None`.

numbers = [1, None, 3, 4]
numbers

# Dauguma funkcijų nežino ką daryti su šiomis vertėmis ir tiesiog neveikia

sum(numbers)

# NumPy `None` keičia masyvo tipą

numbers = np.array([1, 2, 3, 4])
numbers.dtype

numbers = np.array([1, None, 3, 4])
numbers.dtype

# Numpy problemoms spręsti sukūrė atskirą `float` tipo elementą `np.nan`

numbers = np.array([1, np.nan, 3, 4])
numbers.dtype

# Funkcijos nebemeta klaidos, bet rezultatas vis dar netinkamas

np.sum(numbers)

type(np.nan)

# Pandas interpretuoja `None` ir `np.nan` vienodai. Pakeičia į `NaN`

numbers = pd.Series([1, np.nan, None, 4])
numbers

# NaN tipą galimą keisti optimizuojant kodą

numbers = pd.Series([1, np.nan, None, 4], dtype=pd.Int64Dtype())
numbers

# Dauguma funkcijų veikia tiesiog praleisdamos NaN elementus

np.sum(numbers)

np.mean(numbers)

# ### Tvarkymas NaN verčių
#
# Importuojam duomenis. Excelio faile rezultatai ecog tyrimo su žiurkėmis. Suskaičiuotos vidutinės vertės įvairių matavimų, ties skirtingom stimuliacijomis ir sąlygomis.

missing_data_file = pathlib.Path('../data/MissingData.xlsx')
missing_data = pd.read_excel(missing_data_file)
missing_data.head(5)

# Importavimo metu svarbu suprasti duomenų struktūrą.
# Paanalizavus xlsx failą matome kad duomenys yra A1 lape.

missing_data = pd.read_excel(
    missing_data_file, sheet_name="A1")
missing_data.head(5)

# Duomenų pradžioje esantis tarpas (header) šiuo atveju nėra svarbus.
# Praleidžiam pradines eilutes.

missing_data = pd.read_excel(
    missing_data_file, sheet_name="A1", skiprows=3
)
missing_data.head(5)

missing_data.tail(5)

# `head` ir `tail` funkcijos padeda greitai apžvelgti duomenis
#
# `NaN` vertes randame  `isnull` ir `isnan` metodais

missing_data.isnull()

# Atvirkštinis metodas  `notnull`

pd.set_option("max_rows", 50)
missing_data.notnull()

# Vizuolizuoti trūkstamas vertes galima su `missingno` pakuote

pip install missingno

import missingno as msno

msno.matrix(missing_data);

# `dropna` metodas pašalina trūkstamas vertes

droped_Nan = missing_data.dropna()
droped_Nan

pd.set_option("max_rows", 15)

# `dropna` gali trinti tiek stulpelius tiek eilutes

missing_data.dropna(axis="columns")

# arba trinti tik kai visas stulpelis ar eilutė yra NaN vertės

missing_data.dropna(how="all")

# Galime nustatyti limitą NaN verčių  turinčių eit iš eilės kad būtų
# pašalinta eilutė/stulpelis

missing_data.dropna(axis="rows", thresh=6)

# Duomenų pašalinimas yra skausmingas.
# Bet tai dažnai lengviausias ir mažiausiai klausimų keliantis kelias.
#
# Jei duomenų negalime trinti naudojame įvairius duomenų atkūrimo metodus.
# Paprasčiausias metodas yra užpildyti trūkstamas vertes fiksuota verte.

a = missing_data.fillna(0)
a

# Dažnai vertės užpildomas su artimiausia verte

missing_data.fillna(method="ffill")  # bfill; axis

# Arba vidurkiu (mediana ar pan)

missing_data["baseline avg"] = missing_data["baseline avg"].fillna(
    missing_data["baseline avg"].mean()
)
missing_data

# `filter` metodas padeda greitai išfiltruoti stulpelių ir indekso vardus

missing_data.filter(items=["baseline avg"])

missing_data.filter(regex="g$")

missing_data.filter(regex="g$").mean()

# `transform` metodo pagalba galima greitai pritaikyti funkcijas
# sugrupuotiems duomenims

missing_data.groupby("channel group").mean()

missing_data.loc[:, "baseline avg":"test avg"] = missing_data.groupby(
    "channel group"
).transform(lambda x: x - x.mean())


# ---------------
#
# >> ### Lambda
# >>
# >>  Anoniminės funkcijos.
# Kaip ir sąrašų kūrimo atveju 'comprehensions' sintaksė pagreitina kodo kūrimą.
# >>
# >> Sintaksė:
# >>
# >> `lambda arguments: expression`

def testf(x):
    result = x-x.mean()
    return result


testf(np.array([1, 2, 3]))

# Tai tas pats kaip

a=lambda x: x-x.mean()
a(np.array([1,2,3]))

# --------------------

# ### Apply

missing_data.groupby("channel group").mean()

# `apply` metodas veikia iškarto su visa lentele.
# Taigi galime pasiekti lambdos viduje stulpelius ir eilutes visos lentelės
# (transform mato elementus po groupby padalinimo)

missing_data.groupby("channel group").apply(
    lambda x: x["test avg"] - x["baseline avg"].mean()
)

# ### drop
#
# Ištrina stulpelius arba eilutes (`level` raktažodis multiindex atveju)

missing_data = missing_data.dropna().drop(
    ["dataType", "measure", "channels"], axis=1)
missing_data.head()

# ### Review
#
# - Atidarymas

missing_data = pd.read_excel(missing_data_file, sheet_name="A1")
missing_data.head(5)

missing_data.info()

missing_data.describe()

# - Stulpelių vardų pakeitimas

missing_data.columns = missing_data.loc[2]
missing_data.head(5)

missing_data.columns.name = ""
missing_data.head(5)

# Pašalinimas eilučių

missing_data = missing_data.drop([0, 1, 2])
missing_data.head()

# Indekso numeracijos pakeitimas

missing_data=missing_data.reset_index()
missing_data.head()

# Pašalinimas nereikalingų stulpelių

missing_data = missing_data.drop(
    ["measure",'index', "dataType", "channels", "type"], axis=1)
missing_data.head()

# Sukuriam naują stulpelį vaizduojantį dalyvio numerį

rat_nr = ["".join([x, str(y)])
          for x, y in zip(["subj"] * 10, np.arange(1, 11))]
rat_nr

rat_nr = rat_nr * int((len(missing_data) / len(rat_nr)))
missing_data.insert(0, "rat_nr", rat_nr, True)
missing_data.head()

# Užpildom trūkstamus stulpelius vidurkiu

# +
missing_data["baseline avg"] = missing_data["baseline avg"].fillna(
    missing_data["baseline avg"].mean()
)

missing_data["test avg"] = missing_data["test avg"].fillna(
    missing_data["test avg"].mean()
)
# -

missing_data.isna().sum()

# Pataisom klaidas rašybos

missing_data.groupby('channel group').count()

missing_data["channel group"] = missing_data["channel group"].str.replace(
    r"(^[F]$)", "Frontal"
)

missing_data.groupby('channel group').count()

# Tą patį galėtumėme padaryti su replace

missing_data.replace(r"^F$", "Frontal", regex=True)

# Rezultatas

missing_data.groupby("channel group").describe()

missing_data.groupby("channel group").boxplot()

missing_data.boxplot()

# ## Pvz: Airbnb duomenų apžvalga
#
# Importuojam duomenis

import zipfile
with zipfile.ZipFile('../data/Athens.zip', 'r') as zip_ref:
    zip_ref.extractall('../data/')

# +
listings = pd.read_csv(
    "../data/Athens/listings.csv", index_col="id")
listings_details = pd.read_csv(
    "../data/Athens/listings_details.csv",
    index_col="id",
    low_memory=False,
)

calendar = pd.read_csv(
    "../data/Athens/calendar.csv",
    parse_dates=["date"],
    index_col=["listing_id"],
)

reviews = pd.read_csv(
    "../data/Athens/reviews.csv",
    parse_dates=["date"],
    index_col=["listing_id"],
)

reviews_details = pd.read_csv(
    "../data/Athens/reviews_details.csv",
    parse_dates=["date"],
    index_col=["listing_id"],
)
# -

# - listings.csv -- bendra informacija apie būstus
# - listings_details.csv -- detali informacija apie būstus
# - calendar.csv -- datos
# - reviews -- atsiliepimai
# - reviews_details -- detali atsiliepimų informacija
#
# id - unikalus skelbimo numeris
#
# Apžvelgiam duomenis

pd.set_option("display.max_column", 500)
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_seq_items", 500)
pd.set_option("display.max_colwidth", 500)
pd.set_option("expand_frame_repr", True)

listings.head(3)

listings.shape

listings.columns

listings_details.shape

listings_details.columns

# Atrenkame grupę stulpelių

target_columns = [
    "property_type",
    "accommodates",
    "first_review",
    "review_scores_value",
    "review_scores_cleanliness",
    "review_scores_location",
    "review_scores_accuracy",
    "review_scores_communication",
    "review_scores_checkin",
    "review_scores_rating",
    "maximum_nights",
    "listing_url",
    "host_is_superhost",
    "host_about",
    "host_response_time",
    "host_response_rate",
    "street",
    "weekly_price",
    "monthly_price",
    "market",
]
listings = pd.merge(
    listings, listings_details[target_columns], on="id", how="left")

listings.head(1)

listings.dtypes

listings.shape

listings.info()

# `neighbourhood_group`  neturi duomenų

listings["neighbourhood_group"].head()

# Ištrinam

listings = listings.drop(columns=["neighbourhood_group"])

# `host_response_rate` yra teksto tipo su % ženklu

listings["host_response_rate"].head(2)

# Norint atlikti skaičiavimus ištrinam % ženklą ir paverčiam į skaičių

listings["host_response_rate"] = pd.to_numeric(
    listings["host_response_rate"].str.strip("%")
)
listings["host_response_rate"].head(2)

# Randame NaN verčių kiekį

listings.isnull().sum()

msno.matrix(listings);

msno.heatmap(listings);

msno.dendrogram(listings);

# Kuris rajonas turi daugiausiai skelbimų

listings["neighbourhood"].value_counts().sort_values(ascending=True).plot.barh(
    figsize=(10, 10), color="b", width=1
)
plt.title("Listings", fontsize=20)
plt.xlabel("Count of Listings", fontsize=12);

# Yra daug būdu kaip nubraižyti žemėlapį rodanti visus skelbimus.
# Paprasčiausias būdas yra braižyti sklaidos grafiką.

lats = listings["latitude"].tolist()
lons = listings["longitude"].tolist()
locations = list(zip(lats, lons))
plt.scatter(lats, lons);

# `folium` pakuotė kitas paprastas būdas greitai nubraižyti interaktyvų žemėlapį.

pip install folium

import folium
from folium.plugins import FastMarkerCluster

map1 = folium.Map(location=[37.9838, 23.7275], zoom_start=11.5)
FastMarkerCluster(data=locations).add_to(map1)
map1

# Dažniausi kambarių tipai

listings["room_type"].value_counts().sort_values(ascending=True).plot.barh(
    figsize=(15, 3), width=1, color=["g", "b", "r"]
);

# Visi būstų tipai

listings.property_type.unique()

# Kiek ir kokio tipo būstų yra nuomojama?

prop = listings.groupby(["property_type", "room_type"]).room_type.count()
prop

prop = prop.unstack()
prop

prop["total"] = prop.iloc[:, 0:3].sum(axis=1)
prop

prop = prop.sort_values(by=["total"])
prop

prop = prop[prop["total"] >= 100]
prop

prop = prop.drop(columns=["total"])
prop.plot(
    kind="barh",
    stacked=True,
    color=["r", "b", "g"],
    linewidth=1,
    grid=True,
    figsize=(25, 8),
    width=1,
)
plt.title("Property type", fontsize=18)
plt.xlabel("Listings count", fontsize=14)
plt.ylabel("")
plt.legend(loc=4, prop={"size": 13});

# Kiek žmonių gali atvykti į būstą

listings["accommodates"].describe()

listings["accommodates"].value_counts().sort_index().plot.bar(
    figsize=(20, 8), color="b", width=1, rot=0
)
plt.ylabel("Listings", fontsize=12)
plt.xlabel("Accommodates", fontsize=12);

# Kokia dalis visų būstų yra nuomojama profesionalių nuomotojų
#
# Sugrupuojam ir suskaičiuojam kiek skirtingi žmonės nuomoja būstų

freq = (
    listings.groupby(["host_id"])["host_name"]
    .count()
    .reset_index(name="Number of apartments")
)
freq.head()

# Suskaičiuojam kiek yra skirtingų nuomotojų

host = (
    freq.groupby(["Number of apartments"])["host_id"]
    .count()
    .reset_index(name="Number of hosts")
)
host.head()

# Proporcija profesionalių

(host[host["Number of apartments"] > 1].sum() / host.sum())["Number of hosts"]

# Daugiausiai būstų nuomoja

freq[freq["Number of apartments"] >= 30].sort_values(by=["Number of apartments"], ascending=False)

listings.loc[listings['host_id']==77457889]

listings[listings['host_id'].isin([77457889])]

# Vidutinės kaitos rajone

avg_price = (
    listings.groupby("neighbourhood")[
        "price"].mean().sort_values(ascending=True)
)
avg_price.plot.barh(figsize=(20, 15), color="b", width=1)
plt.xlabel("Average price (USD)", fontsize=12);

# Vidutinės kainos visam namui/butui

listings[listings["room_type"] == "Entire home/apt"].groupby("neighbourhood")[
    "price"
].mean().sort_values(ascending=True).plot.barh(figsize=(20, 15), color="b", width=1)
plt.xlabel("Average price (USD)", fontsize=12);

# Kaip kainos priklauso nuo vietos ir būsto tipo?

plt.figure(figsize=(20, 15))
sns.scatterplot(
    x=lats,
    y=lons,
    hue=listings["property_type"],
    size=listings["price"],
    s=20,
    palette="rainbow",
);

# Dažnai naudojama kita biblioteka paišymui [`plotly`](https://github.com/plotly/plotly.py#jupyterlab-support-python-35
# )
#
# ---
# $ pip install jupyterlab "ipywidgets>=7.5"
#
# arba
#
# $ conda install jupyterlab "ipywidgets=7.5"
#
# Then run the following commands to install the required JupyterLab extensions (note that this will require node to be installed):
#
# #### JupyterLab renderer support
# jupyter labextension install jupyterlab-plotly@4.11.0
#
# #### OPTIONAL: Jupyter widgets extension
# jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.11.0
#
# ---

from plotly import express as px
from plotly import graph_objects as go

# +
cscale = [
    [0.0, "rgb(165,0,38)"],
    [0.0005, "rgb(215,48,39)"],
    [0.007, "rgb(250, 152, 122)"],
    [0.08, "rgb(208, 254, 144)"],
    [0.1, "rgb(0, 255, 179)"],
    [0.3, "rgb(171,217,233)"],
    [0.7, "rgb(116,173,209)"],
    [0.9, "rgb(69,117,180)"],
    [1.0, "rgb(49,54,149)"],
]

fig = px.scatter_mapbox(
    listings,
    lat="latitude",
    lon="longitude",
    color="price",
    color_continuous_scale=cscale,
    size_max=20,
    height=760,
    zoom=10,
    title="Scatter map",
    range_color=(0, 700),
)
fig.update_layout(mapbox_style="open-street-map")
fig.show()
# -

# Kainų pasiskirstymas kiekvienam tipui

fig, ax = plt.subplots(figsize=(20, 8))
sns.violinplot(x="room_type", y="price",
               data=listings[listings["price"] <= 700], ax=ax);

# Kiek laisvų kambarių yra iki 2019-12-31?
#
# Norint suskaičiuoti turim ištaisyti kainas ($8,000.00 -> 8000.00)

calendar.head(2)

calendar.price = calendar.price.str.replace(",", "")
calendar["price"] = pd.to_numeric(calendar["price"].str.strip("$"))
calendar = calendar[calendar.date < "2019-12-31"]
calendar.head(2)

free_count = (
    calendar[calendar.available == "t"]
    .groupby(["date"])
    .size()
    .to_frame(name="available")
    .reset_index()
)
free_count.head()

free_count["weekday"] = free_count["date"].dt.day_name()
free_count = free_count.set_index("date")
free_count

free_count.plot(y="available", title="Amount of places", legend="");

# Vidutinės kainos laisvų būstų

avg_price = (
    calendar[(calendar.available == "t")]
    .groupby(["date"])
    .mean()
    .astype(np.int64)
    .reset_index()
)
avg_price["weekday"] = avg_price["date"].dt.day_name()
avg_price = avg_price.set_index("date")
avg_price.plot(y="price", title="Avg price", figsize=(20, 10));

# ## Pavyzdys: nvidia akcijos kaina
#
# Įdiegiam pakuotę skirtą atsisiųst duomenims

pip install pandas_datareader

import pandas_datareader.data as web

# Pirmiausiai atsisiunčiam ir vizualizuojame duomenis
#
# - Nvidia kainos kaita nuo 2004

nvidia = web.DataReader("nvda", start="2004", end="2021", data_source="yahoo")
nvidia.head()

fig = plt.figure(figsize=(20, 20))
ax = plt.axes()
ax.plot(nvidia["Close"], color="red", linestyle="-")
ax.plot(nvidia["Open"], color="blue", linestyle="-")
ax.axis("tight")
ax.set_title("Nvidia price chart")
ax.set_xlabel("Year")
ax.set_ylabel("Price")
ax.legend(["Closing price", "Opening price"]);

# ## Data

nvidia.index

# a) Python

datetime.datetime(year=2019, month=10, day=1)

# datetime.datetime(2019, 10, 1, 0, 0)
#
# b) NumPy

date = np.array("2019-10-01", dtype=np.datetime64)
date

# c) Pandas timestamp

pd.to_datetime(["2020-03-26"])

pd.to_datetime(["1/1/2018", np.datetime64("2018-01-01"),
                datetime.datetime(2018, 1, 1)])

pd.Timestamp(1513393355.5, unit="s")

pd.Timestamp(year=2020, month=1, day=1, hour=12)

pd.Timestamp(year=2020, month=1, day=2, hour=12).strftime("%A")

pd.Timestamp(year=2020, month=1, day=2, hour=12).isocalendar()

pd.Timestamp.today()

# `pd.NaT` koduoja trūkstamas datas

pd.Timestamp(pd.NaT)

# Aritmetika su datom

date + pd.to_timedelta(np.arange(3), "D")

# Generuojam masyvą datų

start = datetime.datetime(2011, 1, 1)
end = datetime.datetime(2012, 1, 1)
index = pd.date_range(start, end)
index

idx = pd.date_range("today", periods=7, freq="D")
idx

pd.date_range(start, periods=1000, freq="M")

# [Trumpiniai datų](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases)
#
# `Timedelta` vaizduoja trukmę\skirtumą tarp datų

pd.Timestamp.today() + pd.Timedelta("1 day")

# Datas dažniausiai naudoja indeksui

data = pd.Series(np.arange(7), index=idx)
data

data["2020-10-28"]

data["2020-10-28":"2020-10-30"]

nvidia["2018"]

nvidia["2018-10":"2018-12"]

nvidia.index.resolution

nvidia.truncate(after="2008-11", before="2006")

# ### `shift`

fig, ax = plt.subplots(3, sharey=True, figsize=(20, 20))
nvidia = nvidia.asfreq("D", method="pad")
nvidia["Close"].plot(ax=ax[0])
nvidia["Close"].shift(900).plot(ax=ax[1])  # shift values
nvidia["Close"].tshift(900).plot(ax=ax[2]);  # shift index

# ### `resample`

idx = pd.date_range("2018-01-01", periods=5, freq="H")
idx

ts = pd.Series(range(len(idx)), index=idx)
ts

ts.resample("2H").mean()

# `resample`  skaičiuoja vidutines vertes
#
# `asfreq` naudoja paskutinę vertę

plt.figure(figsize=(20, 20))
nvidia["Close"].plot(alpha=0.5, style="-", color="red", label='original')
resampled_mean = nvidia["Close"].resample("BA").mean()
resampled_mean.plot(style=":", color="blue", label='resample')
resampled_asfreq = nvidia["Close"].asfreq("BA")
resampled_asfreq.plot(style="--", color="black", label='asfreq')
plt.legend();

# Panašiai veikia slenkantis langas (rolling window)

plt.figure(figsize=(10, 10))
nvidia["Close"].plot()
nvidia["Close"].rolling(1000).mean().plot();

# scipy.signal keičią dažnį naudodamas Fourier

resampled_nvidia = pd.DataFrame(signal.resample(
    nvidia["Close"], 17), index=resampled_mean.index)
plt.figure(figsize=(10, 10))
plt.plot(nvidia["Close"], label="original")
plt.plot(resampled_mean, label="resample")
plt.plot(resampled_asfreq, label="asfreq")
plt.plot(resampled_nvidia, label="scipy resample")
plt.legend(loc="upper left");

# ## Interpoliacija
#
# Trūkstami elementai gali būti atstatyti naudojant juos supančius elementus
#
# Pirmiausiai ištrinam dalį duomenų algoritmų vizualizacijos tikslais

nvidia_spoiled = nvidia["Close"].copy()
nvidia_spoiled["2018"] = np.nan
nvidia_spoiled["2014"] = np.nan

# Dažniausiai naudojami metodai:
#
# - Tiesinė interpoliacija - veda tiesia liniją tarp dviejų artimiausių taškų
# - Artimiausių kaimynų metodas užpildo vertes artimiausių kaimynų
#   vertėmis.
# Puikiai veikia su daugiadimensiais duomenimis.

# +
fig, ax = plt.subplots(2, 2, sharey=True, sharex=True, figsize=(10, 10))
nvidia["Close"].plot(alpha=0.5, style="-", color="red",
                     ax=ax[0, 0], title="orginalas")
nvidia_spoiled.plot(alpha=0.5, style="-", color="black",
                    ax=ax[0, 1], title="sugadinti duomenys")

nvidia_spoiled.interpolate(method="linear").plot(
    alpha=0.5, style="-", color="orange", ax=ax[1, 0], title="tiesinė interpoliacija"
)
nvidia_spoiled.interpolate(method="nearest").plot(
    alpha=0.5, style="-", color="blue", ax=ax[1, 1], title="artimiausi kaimynai"
);
# -

# - Polynomials. Trūkstami taškai aprašomi lygtimi naudojant visus duomenis.
# - Spline. Matrica lygčių
# - akima. Optimizuotas spline naudojantis tik artimiausius taškus.
# - pchip. Panašus į akima, mažiau glotnus.

fig, ax = plt.subplots(3, 2, sharey=True, sharex=True, figsize=(10, 10))
nvidia["Close"].plot(alpha=0.5, style="-", color="red",
                     ax=ax[0, 0], title="orginalus")
nvidia_spoiled.plot(alpha=0.5, style="-", color="black",
                    ax=ax[0, 1], title="sugadintas")
nvidia_spoiled.interpolate(method="polynomial", order=2).plot(
    alpha=0.5, style="-", color="blue", ax=ax[1, 0], title="2 laipnsio polinomas"
)
nvidia_spoiled.interpolate(method="spline", order=3).plot(
    alpha=0.5, style="-", color="orange", ax=ax[1, 1], title="3 laipnsio spline"
)
nvidia_spoiled.interpolate(method="akima").plot(
    alpha=0.5, style="-", color="grey", ax=ax[2, 0], title="akima"
)
nvidia_spoiled.interpolate(method="pchip").plot(
    alpha=0.5, style="-", color="brown", ax=ax[2, 1], title="pchip"
);


