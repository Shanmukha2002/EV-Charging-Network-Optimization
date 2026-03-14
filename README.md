# Graph Analytics for EV Charging Network Optimization

## Project Overview

Electric vehicles require efficient charging infrastructure.
This project analyzes EV charging station locations using graph analytics and data science techniques.

The system helps identify:

* Nearest EV charging stations
* Optimal routes to charging stations
* High demand areas for future charging infrastructure

## Technologies Used

* Python
* Pandas
* NetworkX
* OSMNX
* Folium
* Scikit-learn

## Project Features

* Load EV charging station dataset
* Build Bengaluru road network graph
* Map charging stations to road network
* Find nearest charging station for a user
* Visualize EV stations on an interactive map
* Detect high demand areas using clustering

## Project Structure

EV-Charging-Network-Optimization

data

* ev_stations.csv

maps

* ev_map.html

src

* load_data.py
* build_graph.py
* station_mapper.py
* route_finder.py
* map_visualization.py
* optimization.py

## Future Improvements

* Add real-time EV charging data
* Integrate traffic analysis
* Build web dashboard for EV charging network

## Author

Shanmukhana Gouda
