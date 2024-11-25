import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

'''
Read the CSV file that you created on data wrangling with pandas
("../small-data/mexico-real-estate-clean.csv") into a DataFrame 
named df
'''
# Import "data/mexico-real-estate-clean.csv"
df = pd.read_csv("data/mexico-real-estate-clean.csv")

# Print object type, shape, and head
print(type(df))
print(df.shape)
print(df.head())
