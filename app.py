import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import math

# -------------------------------
# Page Title
# -------------------------------

st.title("EV Charging Network Dashboard")
st.write("Find EV charging stations in Bengaluru and locate the nearest charger.")

# -------------------------------
# Load Dataset
# -------------------------------

data = pd.read_csv("data/ev_stations.csv")

st.subheader("EV Charging Stations Dataset")
st.dataframe(data)

# -------------------------------
# User Location Input
# -------------------------------

st.subheader("Enter Your Location")

lat = st.number_input("Latitude", value=12.9716)
lon = st.number_input("Longitude", value=77.5946)

# -------------------------------
# Distance Function
# -------------------------------

def distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# -------------------------------
# Find Nearest Station
# -------------------------------

nearest_station = None
min_distance = float("inf")

for index, row in data.iterrows():
    d = distance(lat, lon, row["latitude"], row["longitude"])

    if d < min_distance:
        min_distance = d
        nearest_station = row

# -------------------------------
# Create Map
# -------------------------------

map_center = [lat, lon]

m = folium.Map(
    location=map_center,
    zoom_start=11,
    tiles="CartoDB positron"
)

# -------------------------------
# User Marker
# -------------------------------

folium.Marker(
    [lat, lon],
    popup="Your Location",
    icon=folium.Icon(color="blue", icon="user")
).add_to(m)

# -------------------------------
# EV Charging Station Markers
# -------------------------------

for index, row in data.iterrows():

    folium.Marker(
        [row["latitude"], row["longitude"]],
        popup=f"{row['station']} (Capacity: {row['capacity']})",
        icon=folium.Icon(color="green", icon="bolt")
    ).add_to(m)

# -------------------------------
# Highlight Nearest Station
# -------------------------------

folium.Marker(
    [nearest_station["latitude"], nearest_station["longitude"]],
    popup="Nearest Station: " + nearest_station["station"],
    icon=folium.Icon(color="red")
).add_to(m)

# -------------------------------
# Draw Route Line
# -------------------------------

folium.PolyLine(
    locations=[
        [lat, lon],
        [nearest_station["latitude"], nearest_station["longitude"]]
    ],
    color="blue",
    weight=5,
    opacity=0.7
).add_to(m)

# -------------------------------
# Display Map
# -------------------------------

st.subheader("EV Charging Map")

folium_static(m)

# -------------------------------
# Show Result
# -------------------------------

st.subheader("Nearest EV Charging Station")

st.success(
    f"Nearest Station: {nearest_station['station']} "
    f"(Capacity: {nearest_station['capacity']})"
)