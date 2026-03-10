import requests
import folium

def get_ip_location(ip_address=""):
    
    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url)
    data = response.json()

    if data["status"] != "success":
        print("Failed to retrieve location data.")
        return

    ip = data["query"]
    city = data["city"]
    region = data["regionName"]
    country = data["country"]
    lat = data["lat"]
    lon = data["lon"]
    isp = data["isp"]
    timezone = data["timezone"]

    print("\nIP GEOLOCATION INFORMATION")
    print("----------------------------")
    print(f"IP Address : {ip}")
    print(f"City       : {city}")
    print(f"Region     : {region}")
    print(f"Country    : {country}")
    print(f"ISP        : {isp}")
    print(f"Timezone   : {timezone}")
    print(f"Latitude   : {lat}")
    print(f"Longitude  : {lon}")

    location_map = folium.Map(location=[lat, lon], zoom_start=10)

    popup_info = f"""
    IP: {ip}<br>
    City: {city}<br>
    Region: {region}<br>
    Country: {country}<br>
    ISP: {isp}<br>
    Timezone: {timezone}
    """

    folium.Marker(
        [lat, lon],
        popup=popup_info,
        tooltip="IP Location"
    ).add_to(location_map)

    location_map.save("ip_location_map.html")

    print("\nMap saved as: ip_location_map.html")


ip = input("Enter an IP address (leave blank for your IP): ")

get_ip_location(ip)