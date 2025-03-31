import geopandas as gpd

# Use raw string literal for the file path or double backslashes
geojson_file = r"C:\Users\isaia\Downloads\export (1).geojson"

# Load the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(geojson_file)

# Show the first few rows of the data
print(gdf.head())

