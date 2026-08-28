# Bike Share Network Optimizer

A Python model for planning and evaluating bike-share networks. It supports station placement scoring, rider-flow estimation, transit integration analysis, fleet-mix recommendations, and dock-capacity recommendations.

## Features

- Demand estimation from historical trip counts
- Rider-flow matrix generation
- Gravity-model flow estimates for proposed stations
- Haversine geographic distance calculations
- Transit integration scoring within a 500 m radius
- Candidate station ranking using POI, equity, and distance factors
- E-bike vs. regular-bike fleet-mix recommendations
- Station capacity recommendations based on modeled inflow/outflow
- Reproducible demo dataset

## Requirements

- Python 3.9+
- NumPy
- pandas

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the demo

```bash
python bike_share_optimizer.py
```

The script creates synthetic station, trip, and transit data, builds the demand and flow models, and prints recommended new stations, fleet mix, and station capacities.

## Basic usage

```python
from bike_share_optimizer import BikeShareOptimizer

optimizer = BikeShareOptimizer(existing_stations, potential_locations)
optimizer.load_data(trip_data=trip_data, transit_nodes=transit_nodes)
optimizer.build_demand_model()
optimizer.predict_rider_flow()

new_stations = optimizer.optimize_new_stations(num_stations=5, equity_weight=0.6)
fleet_mix = optimizer.optimize_fleet_mix(total_bikes=1000)
capacity = optimizer.recommend_station_capacity()
```

## Expected data columns

### Existing stations

- `station_id`
- `latitude`
- `longitude`
- `capacity`
- `has_charger`

### Potential locations

- `location_id`
- `latitude`
- `longitude`
- `poi_score`
- `equity_score`

### Trip data

- `start_station`
- `end_station`
- `distance` (optional for fleet-mix analysis)

### Transit nodes

- `node_id`
- `latitude`
- `longitude`
- `type`
- `ridership`

## Notes

This repository is a planning-model prototype. The built-in POI scoring method generates demonstration values when an external POI dataset is unavailable. For production use, replace synthetic/demo inputs with validated operational, demographic, transit, and POI datasets.
