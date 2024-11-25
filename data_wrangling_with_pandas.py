import pandas as pd

'''The first part of any data science project is preparing your 
data, which means making sure its in the right place and format
for you to conduct your analysis. The first step of any data
preparation is importing your raw data and cleaning it.
'''

# Load CSV files into DataFrames
df1 = pd.read_csv("data/mexico-real-estate-1.csv",encoding="ISO-8859-1")
# df2 = pd.read_csv("data/mexico-real-estate-2.csv" , encoding="ISO-8859-1")
# df3 = pd.read_csv("data/mexico-real-estate-3.csv", encoding="ISO-8859-1")

# print(df1.head())
# print(df2.head())
# print(df3.head())

'''
Clean df1 by dropping rows with NaN values,Remove column "unnamed". Then remove the "$" 
and "," characters from "price_usd" and recast the values in the 
column as floats.
'''
# Drop rows with any NaN values from df1
df1.dropna(inplace=True)

# removing unwanted column called  "unamed: 0"
df1.drop(columns = ["Unnamed: 0"], inplace = True)

# Ensure "price_usd" is treated as a string before cleaning
df1["price_usd"] = (
    df1["price_usd"]
    .astype(str)  # Ensure values are strings for .str operations
    .str.replace("$", "", regex=False)  # Remove "$"
    .str.replace(",", "")  # Remove ","
    .astype(float)  # Convert cleaned strings to float
)

# Print the cleaned dataframe's first 5 rows
print(df1.head())
