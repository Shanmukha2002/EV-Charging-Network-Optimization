import osmnx as ox

def build_city_graph():

    print("Downloading Bengaluru road network...")

    city = "Bangalore, India"

    G = ox.graph_from_place(city, network_type="drive")

    print("\nGraph created successfully!")

    print("Number of nodes:", len(G.nodes))
    print("Number of edges:", len(G.edges))

    return G


if __name__ == "__main__":

    build_city_graph()