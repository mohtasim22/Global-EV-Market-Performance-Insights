import pandas as pd
import math

# Loading the dataset into a pandas DataFrame
df = pd.read_csv('ev_cars_details.csv')

# Displaying the first 10 rows
print(df.head(5))

# Displaying basic information of the dataset
print(df.info())

# Handling missing values like 0, null and unknown values
df = df.dropna()
df = df[(df != 0).all(axis=1)]
df = df[~df.apply(lambda row: row.astype(str).str.lower().str.contains("unknown").any(), axis=1)]

df.reset_index(drop=True, inplace=True)

# Checking for duplicate rows based on model
duplicates_count = df.duplicated(subset=["Model"]).sum()
print("Number of duplicate Models:", duplicates_count)

# Remove duplicates if any
df.drop_duplicates(subset=["Model"], keep="first", inplace=True)
df.reset_index(drop=True, inplace=True)


# Normalize Categorical Columns
df["Brand"] = df["Brand"].str.title().str.strip()
df["Model"] = df["Model"].str.strip()
df["Segment"] = df["Segment"].str.upper()

# Cleaning "Price($)" Column
def convert_to_usd(x):
    x = str(x)
    if "€" in x:
        rate = 1.10  # EUR → USD
    elif "£" in x:
        rate = 1.32  # GBP → USD
    else:
        rate = 1.00

    # clean numeric portion
    value = x.replace("€", "").replace("£", "").replace("$", "").replace(",", "").replace("*", "")

    if value.strip() == "" or value == "N/A":
        return None

    return math.ceil(float(value) * rate)


# Apply to Price column
df["Price($)"] = df["Price($)"].apply(convert_to_usd)

# Strip units like "kg", "Wh/km", "sec" etc. & cast to float
cols = [
    "Range(km)", "Efficiency(Wh/km)", "Weight(kg)", "0-100(sec)",
    "1-Stop Range(km)", "Battery(kWh)", "Fastcharge(kW)",
    "Towing(kg)", "Cargo Volume(L)","Price/range(/km)"
]

for col in cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r"[^0-9.]", "", regex=True)
        .replace("", None)
        .astype(float)
    )

print(df.info())
print(df.head(5))

# Converting df to csv
df.to_csv("ev_cars_details_clean.csv", index=False)


