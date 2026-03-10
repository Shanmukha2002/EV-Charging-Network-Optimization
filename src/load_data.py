import pandas as pd

def load_station_data():

    data = pd.read_csv("data/ev_stations.csv")

    print("EV Charging Stations Dataset:\n")

    print(data)

    return data


# run the function
if __name__ == "__main__":

    load_station_data()