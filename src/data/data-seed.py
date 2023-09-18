import pyodbc
import random

# Define a list of Singapore town names
towns_in_sg = [
    "Ang Mo Kio", "Bedok", "Bishan", "Bukit Batok", "Bukit Merah",
    "Bukit Panjang", "Bukit Timah", "Central Water Catchment", "Choa Chu Kang", "Clementi",
    "Downtown Core", "Geylang", "Hougang", "Jurong East", "Jurong West",
    "Kallang/Whampoa", "Lim Chu Kang", "Mandai", "Marine Parade", "Museum",
    "Newton", "North-Eastern Islands", "Novena", "Orchard", "Outram",
    "Pasir Ris", "Paya Lebar", "Punggol", "Queenstown", "River Valley",
    "Rochor", "Seletar", "Sembawang", "Sengkang", "Serangoon",
    "Singapore River", "Southern Islands", "Sungei Kadut", "Tampines", "Tanglin",
    "Toa Payoh", "Tuas", "Western Islands", "Western Water Catchment", "Woodlands", "Yishun"
]

# Connect to the SQL Server database
conn = pyodbc.connect(
    "Driver={SQL Server};Server=localhost;Database=LTA;Trusted_Connection=yes;"
)
cursor = conn.cursor()


town_bounding_boxes = {
    "Ang Mo Kio": (1.3700, 103.8375, 1.3860, 103.8560),
    "Bedok": (1.3120, 103.9130, 1.3310, 103.9460),
    "Bishan": (1.3410, 103.8380, 1.3640, 103.8550),
    "Bukit Batok": (1.3460, 103.7460, 1.3610, 103.7700),
    "Bukit Merah": (1.2700, 103.8080, 1.2940, 103.8270),
    "Bukit Panjang": (1.3700, 103.7590, 1.3890, 103.7820),
    "Bukit Timah": (1.3150, 103.7790, 1.3410, 103.8040),
    "Central Water Catchment": (1.3590, 103.7970, 1.3860, 103.8250),
    "Choa Chu Kang": (1.3710, 103.7270, 1.3980, 103.7590),
    "Clementi": (1.3050, 103.7670, 1.3260, 103.7880),
    "Downtown Core": (1.2760, 103.8310, 1.2990, 103.8530),
    "Geylang": (1.3070, 103.8680, 1.3280, 103.8890),
    "Hougang": (1.3570, 103.8660, 1.3820, 103.8890),
    "Jurong East": (1.3210, 103.7210, 1.3430, 103.7460),
    "Jurong West": (1.3360, 103.6950, 1.3580, 103.7200),
    "Kallang/Whampoa": (1.3020, 103.8580, 1.3230, 103.8750),
    "Lim Chu Kang": (1.4230, 103.7110, 1.4400, 103.7320),
    "Mandai": (1.4060, 103.7960, 1.4280, 103.8210),
    "Marine Parade": (1.2920, 103.9000, 1.3090, 103.9150),
    "Museum": (1.2850, 103.8370, 1.3000, 103.8540),
    "Newton": (1.3030, 103.8250, 1.3170, 103.8400),
    "North-Eastern Islands": (1.3940, 104.0340, 1.4240, 104.0570),
    "Novena": (1.3120, 103.8260, 1.3290, 103.8450),
    "Orchard": (1.2980, 103.8240, 1.3130, 103.8400),
    "Outram": (1.2770, 103.8290, 1.2920, 103.8450),
    "Pasir Ris": (1.3660, 103.9370, 1.3820, 103.9550),
    "Paya Lebar": (1.3420, 103.8710, 1.3580, 103.8880),
    "Punggol": (1.3960, 103.8860, 1.4130, 103.9050),
    "Queenstown": (1.2780, 103.7840, 1.2990, 103.8010),
    "River Valley": (1.2880, 103.8260, 1.3050, 103.8440),
    "Rochor": (1.2960, 103.8370, 1.3130, 103.8550),
    "Seletar": (1.3920, 103.8610, 1.4150, 103.8890),
    "Sembawang": (1.4250, 103.8060, 1.4450, 103.8260),
    "Sengkang": (1.3820, 103.8780, 1.4000, 103.8990),
    "Serangoon": (1.3410, 103.8650, 1.3600, 103.8830),
    "Singapore River": (1.2830, 103.8430, 1.2970, 103.8560),
    "Southern Islands": (1.2190, 103.8290, 1.2500, 103.8600),
    "Sungei Kadut": (1.3980, 103.7320, 1.4210, 103.7510),
    "Tampines": (1.3430, 103.9240, 1.3640, 103.9470),
    "Tanglin": (1.2960, 103.8040, 1.3180, 103.8220),
    "Toa Payoh": (1.3250, 103.8410, 1.3430, 103.8550),
    "Tuas": (1.3090, 103.6300, 1.3340, 103.6610),
    "Western Islands": (1.1620, 103.6670, 1.2200, 103.7360),
    "Western Water Catchment": (1.3360, 103.6700, 1.3550, 103.6980),
    "Woodlands": (1.4170, 103.7610, 1.4410, 103.7890),
    "Yishun": (1.4130, 103.8200, 1.4350, 103.8400),
}


# Function to generate random latitude and longitude within town boundaries
def generate_random_point(town):
    min_lat, min_lon, max_lat, max_lon = town_bounding_boxes.get(town, (0, 0, 0, 0))
    
    random_lat = round(random.uniform(min_lat, max_lat), 6)
    random_lon = round(random.uniform(min_lon, max_lon), 6)
    
    return random_lat, random_lon

# Insert test data into the "Incident" table
for _ in range(10000):  # Insert 100 rows as an example
    townName = random.choice(towns_in_sg)
    locationPoint = generate_random_point(townName)
    print(f"{locationPoint[0]}, {locationPoint[1]}")
    location_lat = f"{locationPoint[0]}"
    location_lon = f"{locationPoint[1]}"
    junctions = f"Junctions{random.randint(1, 10)}"
    weather_conditions = random.choice(["Clear", "Rain", "Fog", "Snow"])
    lighting_conditions = random.choice(["Daylight", "Twilight", "Dark"])
    casualty_class = random.choice(["Driver", "Passenger", "Pedestrian"])
    casualty_severity = random.choice(["Fatal", "Serious", "Minor"])
    casualty_sex = random.choice(["M", "F", "U"])
    casualty_type = random.choice(["Injury", "Fatality"])
    time_of_day = random.choice(["Morning", "Afternoon", "Evening", "Night"])
    day_of_week = random.choice(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    road_type = random.choice(["Highway", "Residential", "Urban Street"])
    road_class = random.choice(["Arterial", "Collector", "Local"])
    surface_condition = random.choice(["Dry", "Wet", "Icy"])
    speed_limit = random.randint(20, 80)
    vehicle_type = random.choice(["Car", "Motorcycle", "Truck"])
    towing = random.choice([True, False])
    maneuver = random.choice(["Turning Left", "Changing Lanes", "Stopped"])
    town = townName
    incident_date_time = f"20{random.randint(10, 23)}-{random.randint(1, 9)}-{random.randint(1, 28)} {random.randint(0, 23)}:{random.randint(0, 59)}:00"

    insert_query = f"""
        INSERT INTO Incident (
            Location_lat, Location_lon, Junctions, WeatherConditions, LightingConditions,
            CasualtyClass, CasualtySeverity, CasualtySex, CasualtyType,
            TimeOfDay, DayOfWeek, RoadType, RoadClass, SurfaceCondition,
            SpeedLimit, VehicleType, Towing, Maneuver, Town, IncidentDateTime
        ) VALUES (
            {location_lat}, {location_lon}, '{junctions}', '{weather_conditions}', '{lighting_conditions}',
            '{casualty_class}', '{casualty_severity}', '{casualty_sex}', '{casualty_type}',
            '{time_of_day}', '{day_of_week}', '{road_type}', '{road_class}', '{surface_condition}',
            {speed_limit}, '{vehicle_type}', {int(towing)}, '{maneuver}', '{town}', '{incident_date_time}'
        )
    """
    print(insert_query)
    cursor.execute(insert_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Test data inserted successfully.")
