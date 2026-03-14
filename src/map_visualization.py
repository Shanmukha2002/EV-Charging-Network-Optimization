import pandas as pd
import folium

def create_ev_map():

    print("Loading EV station dataset...")

    stations = pd.read_csv("data/ev_stations.csv")

    # center of Bengaluru
    map_center = [12.9716, 77.5946]

    m = folium.Map(
    location=map_center,
    zoom_start=12,
    tiles="OpenStreetMap",
    control_scale=True
)

    # Example user location
    user_location = [12.9352, 77.6245]

    folium.Marker(
        user_location,
        popup="User Location",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    # Add EV charging stations
    for index, row in stations.iterrows():

        folium.Marker(
            [row["latitude"], row["longitude"]],
            popup=row["station"],
            icon=folium.Icon(color="green", icon="bolt")
        ).add_to(m)

    # Save map
    m.save("maps/ev_map.html")

    print("Map created successfully!")


if __name__ == "__main__":

    create_ev_map()