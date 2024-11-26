import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

'''
Read the CSV file that you created on data wrangling with pandas
("data/mexico-real-estate-clean.csv") into a DataFrame 
named df.
'''
# Import "data/mexico-real-estate-clean.csv"
df = pd.read_csv("data/mexico-real-estate-clean.csv")

# Print object type, shape, and head
print(type(df))
print(df.shape)
print(df.head())

'''
Location Data: "lat" and "lon"
Add "lat" and "lon" to the code below, and run the code. You'll
see a map that's centered on Mexico City, and you can use the
"Zoom Out" button in the upper-right corner of the map so that
you can see the whole country. 
'''
# Use plotly express to create figure
fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat= "lat",
    lon= "lon",
    center={"lat": 19.43, "lon": -99.13},  # Map will be centered on Mexico City
    width=600,  # Width of map
    height=600,  # Height of map
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

# Add mapbox_style to figure layout
fig.update_layout(mapbox_style="open-street-map")

# Show figure
fig.show()

'''
Categorical Data: "state"
Use the value_counts method on the "state" column to determine 
the 10 most prevalent states in our dataset.
'''
# Get value counts of "state" column
print(df["state"].value_counts().head(10))

'''
Numerical Data: "area_m2" and "price_usd
Use the describe method to print the mean, standard deviation, 
and quartiles for the "area_m2" and "price_usd" columns.
'''
# Describe "area_m2", "price_usd" columns
print(df[["area_m2","price_usd"]].describe())

'''
Create a histogram of "area_m2". Make sure that the x-axis has 
the label "Area [sq meters]", the y-axis has the label "Frequency"
,and the plot has the title "Distribution of Home Sizes".
'''
# Use Matplotlib to create histogram of "area_m2"
plt.hist(df['area_m2'])

# Add x-axis label
plt.xlabel("Area [sq meters]")

# Add y-axis label
plt.ylabel("Frequency")

# Add title
plt.title("Distribution of Home Sizes");