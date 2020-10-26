# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
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

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ![datacamp](../images/datacamp.png)
#
# - Data manipulation with python
# - Python Toolbox
#     - Dealing with Missing Data in Python
#     - Working with Dates and Times in Python

# ---
# >> **UŽDUOTIS**
# >>
# >> http://insideairbnb.com/get-the-data.html
# >>
# >> Atsisiųskite vieną iš miestų ir atsakykite į klausimus
# >> 1. Top 10 savininkų (daugiausiai nuomoja, uždirba)
# >> 2. Kaip dienos kaina kinta jeigu nuomojamasi savaitei/mėnesiui/dienai (listings)
# >> 3. Kaip kaina priklauso nuo vietos mieste įvertinimo? Švaros? ir t.t
# >> 4. Rasti savininkus įvardintus kaip 'superhosts'. Kokią dalį visų
# nuomotojų jie sudaro?
# >> 5. Ilgiausias komentaras (reviews_details)
# >> 6. Daugiausiai komentarų turinti vieta
# >> 7. Iš komentarų datų (reviews) suraskite kada daugiausiai turistų mieste (plot comments vs dates)
# >> 8. Savo klausimą
# >> 9. Savo klausimą
# >> 10. Savo klausimą
# >>
# ---
#































































#  Atsakymai

listings = pd.read_csv(
    "~/Documents/biod2020/data/Athens/listings.csv", index_col="id")
listings_details = pd.read_csv(
    "~/Documents/biod2020/data/Athens/listings_details.csv",
    index_col="id",
    low_memory=False,
)
calendar = pd.read_csv(
    "~/Documents/biod2020/data/Athens/calendar.csv",
    parse_dates=["date"],
    index_col=["listing_id"],
)
reviews = pd.read_csv(
    "~/Documents/biod2020/data/Athens/reviews.csv",
    parse_dates=["date"],
    index_col=["listing_id"],
)
reviews_details = pd.read_csv(
    "~/Documents/biod2020/data/Athens/reviews_details.csv",
    parse_dates=["date"],
    index_col=["listing_id"],
)

#  to display all the data
pd.set_option("display.max_column", 500)
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_seq_items", 500)
pd.set_option("display.max_colwidth", 500)
pd.set_option("expand_frame_repr", True)


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
listings = listings.drop(columns=["neighbourhood_group"])
listings["host_response_rate"] = pd.to_numeric(
    listings["host_response_rate"].str.strip("%")
)

# >> 1. Top 10 savininkų (daugiausiai nuomoja, uždirba)

#  - daugiausiai nuomoja

top10Id = (
    listings.groupby(["host_id"])["host_name"]
    .count()
    .reset_index(name="count")
    .sort_values(by="count", ascending=False)
    .head(10)
)
print(top10Id)

for t_id in top10Id["host_id"].to_numpy():
    print(listings.loc[listings["host_id"] == t_id].iloc[1, 2])

# - uždirba

top100Id = (
    listings.groupby(["host_id"])["host_name"]
    .count()
    .reset_index(name="count")
    .sort_values(by="count", ascending=False)
    .head(100)
)

cummulative_sum = (
    listings[listings["host_id"].isin(top100Id["host_id"])]
    .groupby("host_id")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

for c_id, c_sum in zip(cummulative_sum.index.to_numpy(), cummulative_sum.to_numpy()):
    print(
        f'{listings.loc[listings["host_id"] == c_id].iloc[1, 2]} earns {c_sum}')

# >>  2. Kaip dienos kaina kinta jeigu nuomojamasi savaitei/mėnesiui/dienai (listings)

listings.columns

listings.price.head()

listings.weekly_price.head()

listings["weekly_price"] = pd.to_numeric(
    listings["weekly_price"].str.strip("$").str.replace(",", "")
)
listings.weekly_price.head()

listings.monthly_price.head()

listings["monthly_price"] = pd.to_numeric(
    listings["monthly_price"].str.strip("$").str.replace(",", "")
)
listings.monthly_price.head()

# per dieną

(listings.monthly_price / 30).dropna().mean()

(listings.weekly_price / 7).dropna().mean()

listings.price.mean()

# >> 3. Kaip kaina priklauso nuo vietos mieste įvertinimo? Švaros? ir t.t


listings.columns
plt.scatter(listings.review_scores_location, listings.price)
plt.xlabel("review score of location")
plt.ylabel("price")

listings.groupby("review_scores_location").price.mean()

listings.boxplot(column="price", by="review_scores_location")

listings.boxplot(column="price", by="review_scores_cleanliness")


# >> 4. Rasti savininkus įvardintus kaip 'superhosts'. Kokią dalį visų

listings.columns

listings.host_is_superhost.isnull().sum()

total = listings.host_is_superhost.shape[0]
total

superhosts = listings.host_is_superhost.str.count(r"t").sum()
superhosts

print(f" Super hosts are {superhosts/total*100:.3}% of all the landlords")

# >> 5. Ilgiausias komentaras (reviews_details)

reviews_details.comments.iloc[0]

len(reviews_details.comments.iloc[0])

#  listing id su ilgiausiu komentaru

reviews_details.comments.str.len().sort_values(ascending=False).head()

reviews_details.loc[26716805]

for review in reviews_details.loc[26716805].comments:
    print(len(review))

#  ilgiausio komentaro id

reviews_details.loc[26716805].set_index("id")["comments"].str.len()

# >> 6. Daugiausiai komentarų turinti vieta

reviews_details.groupby("listing_id")["id"].count(
).sort_values(ascending=False).head(1)

reviews_details.loc[1177492]


# >> 7. Iš komentarų datų (reviews) suraskite kada daugiausiai turistų mieste (plot comments vs dates)

reviews.head()

reviews["count"] = 1
reviews

reviews.groupby("date").sum().plot(figsize=(20, 20));




