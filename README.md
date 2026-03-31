#House Price Prediction

##Overview
This project is created for educational purpose to understand the end to end machine learning workflow using house price dataset

##Dataset
-India house price dataset
-Approximately 25,000 records
-CSV format

##Project Structure
-data/  :contains the dataset
-src/   :contains source code
-main.py  :entry point of the project
-README.md :project documentation

##Workflow
1.Load dataset
2.Split the data into training and test sets
3.Perform data preprocessing (cleaning, encoding, feature preparation)

##Data Preprocessing

* Removed high-cardinality features such as `Locality` and `Amenities`
* Separated features (X) and target variable (Price_in_Lakhs)
* Applied one-hot encoding to categorical variables
* Used `drop_first=True` to avoid redundant columns
* Ensured same structure for train and test data using column alignment



##Disclaimer
This project is for educational purposes only and is not intended for real world house price prediction

