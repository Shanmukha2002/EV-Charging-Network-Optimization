import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.title("EV Charging Network Dashboard")

st.write("Find EV charging stations in Bengaluru.")

data = pd.read_csv("data/ev_stations.csv")

st.subheader("EV Charging Stations Dataset")
st.dataframe(data)

# user input
st.subheader("Enter Your Location")

lat = st.number_input("Latitude", value=12.9716)
lon = st.number_input("Longitude", value=77.5946)

# create map
map_center = [lat, lon]

m = folium.Map(location=map_center, zoom_start=12, tiles="CartoDB positron")

# user marker
folium.Marker(
    [lat, lon],
    popup="Your Location",
    icon=folium.Icon(color="blue")
).add_to(m)

# station markers
for index, row in data.iterrows():

    folium.Marker(
        [row["latitude"], row["longitude"]],
        popup=row["station"],
        icon=folium.Icon(color="green", icon="bolt")
    ).add_to(m)

st.subheader("EV Charging Map")

folium_static(m)