import pandas as pd

# set local variables
data_source = "market-performance-by-president.csv"

# function reads the data and returns a pandas dataframe
def market_data():
    return pd.read_csv(data_source)


def main():
    data = market_data()
    print(data.head())

if __name__ == "__main__":
    main()