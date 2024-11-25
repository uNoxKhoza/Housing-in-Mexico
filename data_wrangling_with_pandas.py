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
# removing unwanted column called  "unamed: 0"
df2.drop(columns = ["Unnamed: 0"], inplace = True,errors='ignore')

# Drop rows with any NaN values from df1
df1.dropna(inplace=True)

# Ensure "price_usd" is treated as a string before cleaning
df1["price_usd"] = (
    df1["price_usd"]
    .astype(str)  # Ensure values are strings for .str operations
    .str.replace("$", "", regex=False)  
    .str.replace(",", "")  
    .astype(float) 
)


'''
Clean df2
First, drop rows with NaN values in df2. Next, use the "price_mxn"
column to create a new column named "price_usd". (Keep in mind 
that, when this data was collected in 2014, a dollar cost 19 pesos.)
Finally, drop the "price_mxn" from the DataFrame.
'''


#drop all NaN rows
df2.dropna(inplace= True)

#create new column "price_used" from price_mxm(mexican pesos)
df2['price_usd'] = (df2['price_mxn'] / 19).round(2)
# drop price_mxn column
df2.drop(columns = ['price_mxn'], inplace = True)

'''
Clean df3 
Drop rows with NaN values in df3. Then use the split method to 
create two new columns from "lat-lon" named "lat" and "lon", 
respectively.
'''
 # removing unwanted column called  "unamed: 0"
df3.drop(columns = ["Unnamed: 0"], inplace = True ,errors='ignore')

 # Drop null values from df3
df3.dropna(inplace=True)

# # Create "lat" and "lon" columns for df3
df3[["lat", "lon"]] = df3["lat-lon"].str.split("," , expand=True)


'''
Use the split method again, this time to extract the state for 
every house. (Note that the state name always appears after
"México|" in each string.) Use this information to create a 
"state" column. Finally, drop the "place_with_parent_names" and 
"lat-lon" columns from the DataFrame.
'''
# Create "state" column for df3
df3["state"] = df3["place_with_parent_names"].str.split("|", expand=True)[2]

# Drop "place_with_parent_names" and "lat-lon" from df3
df3.drop(columns=["place_with_parent_names" ,"lat-lon"], inplace=True)

'''
Use pd.concat to concatenate df1, df2, df3 as new DataFrame named
 df. Your new DataFrame should have 1,736 rows and 6 columns:
 "property_type", "state", "lat", "lon", "area_m2", and "price_usd". 
'''
# Concatenate df1, df2, and df3
df = pd.concat([df1,df2,df3])
print(df.head())

'''Save df as a CSV file using the to_csv method. The file path 
should be "./data/mexico-real-estate-clean.csv". Be sure to set 
the index argument to False.
'''
# Save df
df.to_csv("data/mexico-real-estate-clean.csv" , index=False)
