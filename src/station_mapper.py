import pandas as pd
import osmnx as ox

def map_stations():

    print("Loading EV station dataset...")

    data = pd.read_csv("data/ev_stations.csv")

    print(data)

    print("\nDownloading Bengaluru road network...")

    G = ox.graph_from_place("Bangalore, India", network_type="drive")

    station_nodes = []

    print("\nMapping stations to nearest road nodes...\n")

    for index, row in data.iterrows():

        node = ox.distance.nearest_nodes(
            G,
            row["longitude"],
            row["latitude"]
        )

        station_nodes.append((row["station"], node))

        print(f"{row['station']} → Node {node}")

    return station_nodes


if __name__ == "__main__":

    map_stations()