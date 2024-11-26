import matplotlib.pyplot as plt
import pandas as pd

'''
Read the CSV file that you created in data wrangling("data/mexico-real-estate-clean.csv")
into a DataFrame named df
'''
# Import "data/mexico-real-estate-clean.csv"
df = pd.read_csv("data/mexico-real-estate-clean.csv")
df = df.drop(columns=["Unnamed: 0"]) 

# Print object type, shape, and head
# print("df type:", type(df))
# print("df shape:", df.shape)
print(df.head())
# print(df.columns)
