import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def find_high_demand_areas():

    print("Loading EV charging station data...")

    stations = pd.read_csv("data/ev_stations.csv")

    coords = stations[["latitude", "longitude"]]

    print("\nRunning clustering algorithm...")

    kmeans = KMeans(n_clusters=3)

    stations["cluster"] = kmeans.fit_predict(coords)

    print("\nCluster Results:\n")

    print(stations)

    # plot clusters
    plt.scatter(
        stations["longitude"],
        stations["latitude"],
        c=stations["cluster"]
    )

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.title("EV Charging Station Clusters")

    plt.show()


if __name__ == "__main__":

    find_high_demand_areas()