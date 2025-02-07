#!/usr/bin/python

# example script for calling the wimbylulc plugin
import json

import windlulc

# basic config

CONFIG_FILENAME = "windlulc.yaml"
TGEOJSON_FILENAME = "test/spain.geojson"

# rasterfiles

RASTERDATA = {
    "CLC100": {
        "path": "data/U2018_CLC2018_V2020_20u1.tif",
        "result_type": "count",
    },
    "SLOPE90": {
        "path": "data/Copernicus_SLOPE_90m_COG_3035.tif",
        "result_type": "mean",
    },
}


def run_wrapper():
    # Read the turbines GeoJSON from file
    #
    try:
        with open(TGEOJSON_FILENAME, "r") as f:
            turbines_geojson = json.load(f)
        print("Turbines GeoJSON loaded successfully.")
    except FileNotFoundError:
        print(f"Error: File '{TGEOJSON_FILENAME}' not found.")
        turbines_geojson = {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{TGEOJSON_FILENAME}': {e}")
        turbines_geojson = {}

    print(CONFIG_FILENAME)
    print(TGEOJSON_FILENAME)
    print(RASTERDATA)

    # Call the package's main function with the YAML config filename and GeoJSON dictionary
    windlulc.main(
        str(CONFIG_FILENAME), RASTERDATA, turbines_geojson, DEBUG=True
    )


if __name__ == "__main__":
    run_wrapper()
