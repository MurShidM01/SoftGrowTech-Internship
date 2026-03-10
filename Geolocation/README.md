# Geolocation

![Python](https://img.shields.io/badge/Python-3.8%2B-1f6feb?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-ip--api.com-0ea5e9?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2ea043?style=for-the-badge)

A Python tool that fetches IP location data using the ip-api.com service and generates an interactive HTML map showing the location.

**Highlights**

- Fetches location data for any IP address or your own IP
- Displays city, region, country, ISP, timezone, and coordinates
- Generates an interactive map using Folium
- Saves the map as an HTML file for viewing in a browser

**Tech**

- Python 3.8+
- `requests` - HTTP requests
- `folium` - Interactive map generation

**Install Dependencies**

```bash
pip install requests folium
```

**Run**

```bash
python geolocation.py
```

**Usage**

1. Run the script
2. Enter an IP address (or leave blank to get your own IP location)
3. View the location details in the terminal
4. Open `ip_location_map.html` in your browser to see the interactive map

**Sample Output**

```
IP GEOLOCATION INFORMATION
----------------------------
IP Address : 8.8.8.8
City       : Mountain View
Region     : California
Country    : United States
ISP        : Google Public DNS
Timezone   : America/Los_Angeles
Latitude   : 37.4223
Longitude  : -122.0848

Map saved as: ip_location_map.html
```

**Project Structure**

- `geolocation.py` - Main script
- `ip_location_map.html` - Generated map (created after running)
