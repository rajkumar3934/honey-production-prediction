# Honey Production Prediction

This Python script uses linear regression to predict future honey production based on historical data. The script reads in honey production data from a CSV file, groups the data by year, and calculates the mean total production for each year. It then fits a linear regression model to the data and plots the predicted values, including predicted values for future years.

## Dependencies

- Python 3.x
- Pandas
- Matplotlib
- NumPy
- scikit-learn

## Installation

To use this script, first clone the repository:

$ git clone https://github.com/rajkumar3934/honey-production-prediction.git
$ cd honey-production-prediction

Then, install the required dependencies:

$ pip install pandas matplotlib numpy scikit-learn


## Usage

To run the script, simply execute the `honey_production_prediction.py` file:

$ python honey_production_prediction.py


The script will generate two plots: one showing the historical honey production data and the predicted values, and one showing the predicted values for future years.

![image](https://user-images.githubusercontent.com/27536166/230705381-d62ea2bc-ea2d-4119-8c96-11a005c1fb26.png)

## Contributing

If you'd like to contribute to this project, please fork the repository and create a new branch for your changes. Then, submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
