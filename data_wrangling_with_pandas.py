import pandas as pd

'''The first part of any data science project is preparing your 
data, which means making sure its in the right place and format
for you to conduct your analysis. The first step of any data
preparation is importing your raw data and cleaning it.
'''

# Load CSV files into DataFrames
df1 = pd.read_csv("data/mexico-real-estate-1.csv",encoding="ISO-8859-1")
df2 = pd.read_csv("data/mexico-real-estate-2.csv" , encoding="ISO-8859-1")
df3 = pd.read_csv("data/mexico-real-estate-3.csv", encoding="ISO-8859-1")


'''
Clean df1 by dropping rows with NaN values. Then remove the "$" 
and "," characters from "price_usd" and recast the values in the 
column as floats.
'''
# Drop rows with any NaN values from df1
df1.dropna(inplace=True)

# Ensure "price_usd" is treated as a string before cleaning
df1["price_usd"] = (
    df1["price_usd"]
    .astype(str)  # Ensure values are strings for .str operations
    .str.replace("$", "", regex=False)  # Remove "$"
    .str.replace(",", "")  # Remove ","
    .astype(float)  # Convert cleaned strings to float
)


'''
Clean df2
First, drop rows with NaN values in df2. Next, use the "price_mxn"
column to create a new column named "price_usd". (Keep in mind 
that, when this data was collected in 2014, a dollar cost 19 pesos.)
Finally, drop the "price_mxn" from the DataFrame.
'''
# removing unwanted column called  "unamed: 0"
df2.drop(columns = ["Unnamed: 0"], inplace = True)

#drop all NaN rows
df2.dropna(inplace= True)
#create new column "price_used" from price_mxm(mexican pesos) and drop price_mxn column
#data was collected in 2014, a dollar cost 19 pesos
df2['price_usd'] = (df2['price_mxn'] / 19).round(2)
df2.drop(columns = ['price_mxn'], inplace = True)

