import requests, json
import psycopg2
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

try:
    conn = psycopg2.connect(
            user=environ.get("DB_USER"),
            password=environ.get("DB_PASSWORD"),
            host="localhost",
            port="5432",
            database="scoop"
    )
except:
    print("Database connection failed.")

cursor = conn.cursor()
helsinki_places_json = requests.get('http://open-api.myhelsinki.fi/v2/places/').json()
data = helsinki_places_json["data"]

for place in data:
    insert_query = "insert into scoop.venue(id, name, info_url, description, street_address, postal_code, city, neighbourhood) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    if place["name"]["fi"] == None:
        continue

    is_restaurant_or_cafe = False

    for tag in place["tags"]:
        tag_name = tag["name"].lower()
        if tag_name == "restaurants" or tag_name == "cafes" or tag_name == "islandrestaurant" or tag_name == "restaurant" or tag_name == "cafe" or tag_name == "cafesummer" or tag_name == "restaurantsummer":
            is_restaurant_or_cafe = True
            continue

    if is_restaurant_or_cafe == False:
        continue

    cursor.execute(
        insert_query,
        (
            place["id"],
            place["name"]["fi"],
            place["info_url"],
            place["description"]["intro"],
            place["location"]["address"]["street_address"],
            place["location"]["address"]["postal_code"],
            place["location"]["address"]["locality"],
            place["location"]["address"]["neighbourhood"],
        )
    )
    conn.commit()
conn.close()

"""helsinki_places_json = requests.get('http://open-api.myhelsinki.fi/v2/places/').json()
data = helsinki_places_json["data"]
for place in data:
    print(place["name"]["en"])
    print(place["info_url"])
    print(place["description"]["intro"])
    print(place["location"]["address"]["street_address"])
    print(place["location"]["address"]["postal_code"])
    print(place["location"]["address"]["locality"])
    print(place["location"]["address"]["neighbourhood"])

for data in helsinki_places_json:
    print(data)"""
