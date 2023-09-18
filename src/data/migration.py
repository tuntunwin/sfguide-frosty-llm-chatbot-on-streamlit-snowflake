import pyodbc

# Define your database connection parameters
server = 'localhost'
database = 'LTA'
username = 'sa'
password = 'Secr3t999'

# Create a connection to the SQL Server database
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Define the SQL statement to create the "Incident" table
create_table_sql = '''
    CREATE TABLE Incident (
        IncidentID INT PRIMARY KEY IDENTITY(1,1),
        Location_lat FLOAT,
        Location_lon FLOAT,
        Junctions VARCHAR(50),
        WeatherConditions VARCHAR(50),
        LightingConditions VARCHAR(50),
        CasualtyClass VARCHAR(50),
        CasualtySeverity VARCHAR(50),
        CasualtySex CHAR(1),
        CasualtyType VARCHAR(50),
        TimeOfDay VARCHAR(50),
        DayOfWeek VARCHAR(50),
        RoadType VARCHAR(50),
        RoadClass VARCHAR(50),
        SurfaceCondition VARCHAR(50),
        SpeedLimit INT,
        VehicleType VARCHAR(50),
        Towing BIT,
        Maneuver VARCHAR(50),
        Town VARCHAR(255),
        IncidentDateTime DATETIME
    )
'''

try:
    # Execute the SQL statement to create the "Incident" table
    cursor.execute(create_table_sql)
    connection.commit()
    print("Incident table created successfully.")
except Exception as e:
    print("Error:", e)
finally:
    # Close the database connection
    cursor.close()
    connection.close()
