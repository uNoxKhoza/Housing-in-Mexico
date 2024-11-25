import pandas as pd

# Load CSV files into DataFrames
df1 = pd.read_csv("data/mexico-real-estate-1.csv",encoding="ISO-8859-1")
df2 = pd.read_csv("data/mexico-real-estate-2.csv" , encoding="ISO-8859-1")
df3 = pd.read_csv("data/mexico-real-estate-3.csv", encoding="ISO-8859-1")

print(df1.head())
print(df2.head())
print(df3.head())
