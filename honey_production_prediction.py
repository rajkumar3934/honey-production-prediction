import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Load the honey production data into a Pandas DataFrame
df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

# Group the data by year and calculate the mean total production for each year
prod_per_year = df.groupby('year').totalprod.mean().reset_index()

# Extract the year and total production values
X = prod_per_year['year']
y = prod_per_year['totalprod']

# Reshape the X data from a 1D array to a 2D array with one column
X = X.values.reshape(-1,1)

# Create a scatter plot of the data with proper axis labels
plt.scatter(X, y)
plt.xlabel('Year')
plt.ylabel('Total Production (lbs)')

# Fit a linear regression model to the data and plot the predicted values
regr = linear_model.LinearRegression()
regr.fit(X,y)
y_predict = regr.predict(X)
plt.plot(X,y_predict)
plt.show()
# Plot the predicted values for future years
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1,1)
future_predict = regr.predict(X_future)
plt.plot(X_future,future_predict)

# Add proper axis labels and show the plot
plt.xlabel('Year')
plt.ylabel('Total Production (lbs)')
plt.show()
