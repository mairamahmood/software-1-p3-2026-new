import mysql.connector
from geopy.distance import geodesic

# Connect to database
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="testuser",
    password="123"
)

cursor = connection.cursor()

# ---------------- TASK 1 ----------------
print("\nTask 1 - Get airport name and municipality")
icao = input("Enter ICAO code: ").upper()

sql = "SELECT name, municipality FROM airport WHERE ident=%s"
cursor.execute(sql, (icao,))
result = cursor.fetchone()

if result:
    print("Airport name:", result[0])
    print("Municipality:", result[1])
else:
    print("Airport not found.")


# ---------------- TASK 2 ----------------
print("\nTask 2 - Airports by country code")
country = input("Enter country code (example FI): ").upper()

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country=%s
GROUP BY type
ORDER BY type
"""

cursor.execute(sql, (country,))
results = cursor.fetchall()

print("Airport types in", country)
for row in results:
    print(row[0], ":", row[1])


# ---------------- TASK 3 ----------------
print("\nTask 3 - Distance between two airports")
icao1 = input("Enter first ICAO code: ").upper()
icao2 = input("Enter second ICAO code: ").upper()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"

cursor.execute(sql, (icao1,))
coord1 = cursor.fetchone()

cursor.execute(sql, (icao2,))
coord2 = cursor.fetchone()

if coord1 and coord2:
    location1 = (coord1[0], coord1[1])
    location2 = (coord2[0], coord2[1])

    distance = geodesic(location1, location2).kilometers
    print("Distance between airports:", round(distance, 2), "km")
else:
    print("One or both airports not found.")


# Close connection
cursor.close()
connection.close()




