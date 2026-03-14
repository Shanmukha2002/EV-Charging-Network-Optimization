from src.load_data import load_station_data
from src.build_graph import build_city_graph
from src.station_mapper import map_stations
from src.route_finder import find_nearest_station
from src.map_visualization import create_ev_map
from src.optimization import find_high_demand_areas


def main():

    print("\nEV Charging Network Optimization Project\n")

    print("1. Loading EV station dataset...")
    load_station_data()

    print("\n2. Building road network graph...")
    build_city_graph()

    print("\n3. Mapping stations to road network...")
    map_stations()

    print("\n4. Finding nearest charging station...")
    find_nearest_station()

    print("\n5. Creating EV charging map...")
    create_ev_map()

    print("\n6. Running optimization analysis...")
    find_high_demand_areas()

    print("\nProject execution completed.")


if __name__ == "__main__":
    main()