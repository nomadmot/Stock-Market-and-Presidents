import pandas as pd

# set local variables
data_source = "Dow Performance by President.csv"

# function reads the data and returns a pandas dataframe
def market_data():
    return pd.read_csv(data_source)