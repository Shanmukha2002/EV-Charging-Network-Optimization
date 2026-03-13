import pandas as pd
import osmnx as ox
import networkx as nx

def find_nearest_station():

    print("Loading EV charging station data...\n")

    stations = pd.read_csv("data/ev_stations.csv")

    print(stations)

    print("\nDownloading Bengaluru road network...\n")

    G = ox.graph_from_place("Bangalore, India", network_type="drive")

    # Example user location
    user_lat = 12.9352
    user_lon = 77.6245

    print("\nUser location:", user_lat, user_lon)

    user_node = ox.distance.nearest_nodes(G, user_lon, user_lat)

    nearest_station = None
    shortest_distance = float("inf")

    for index, row in stations.iterrows():

        station_node = ox.distance.nearest_nodes(
            G,
            row["longitude"],
            row["latitude"]
        )

        distance = nx.shortest_path_length(
            G,
            user_node,
            station_node,
            weight="length"
        )

        if distance < shortest_distance:

            shortest_distance = distance
            nearest_station = row["station"]

    print("\nNearest EV Charging Station:")
    print(nearest_station)

    print("\nDistance (meters):", shortest_distance)


if __name__ == "__main__":

    find_nearest_station()