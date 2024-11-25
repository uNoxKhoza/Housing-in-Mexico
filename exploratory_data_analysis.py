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

'''
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