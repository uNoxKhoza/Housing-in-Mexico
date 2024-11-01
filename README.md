
About the Project

Purpose
This project aims to build a predictive model to estimate apartment prices in Mexico City, considering features like size, location, and borough. Understanding these factors can benefit buyers and sellers in the real estate market.

Data
Using open-source property data, the project cleaned and processed five CSV files to retain essential columns: price, surface covered, location (latitude and longitude), and borough. This cleaning process ensured the data’s quality and transparency.

Methods
The main techniques used were:

    Ridge Regression to prevent overfitting by penalizing large coefficients.
    OneHotEncoder to convert categorical borough data into a binary format suitable for modeling.
    SimpleImputer to replace missing values with the mean or median as needed.

Results
The model identified key boroughs affecting apartment prices. It includes a prediction function for apartment prices based on features like size and location, and an interactive widget that allows users to explore how different inputs influence predicted prices.

Usage
This project is for educational purposes only and not for real-world decision-making without further validation.

Conclusion
This project demonstrates how data science can offer insights into Mexico City's real estate market, serving as a practical example of predictive modeling in property pricing.