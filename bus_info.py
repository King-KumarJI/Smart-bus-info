import mysql.connector
import random
import time

# -------------------- DB Connection --------------------
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",     # your MySQL password
    database="databases"   # your database name
)
cursor = db.cursor()

# -------------------- Sample Data --------------------
depots = ["North Depot", "South Depot", "East Depot", "West Depot"]
routes = ["Route A", "Route B", "Route C", "Route D"]
stops = ["Stop 1", "Stop 2", "Stop 3", "Stop 4", "Stop 5"]

# -------------------- Insert Data (only if empty) --------------------
cursor.execute("SELECT COUNT(*) FROM bus_info")
if cursor.fetchone()[0] == 0:
    for bus_id in range(1, 11):  # 10 buses
        cursor.execute(
            "INSERT INTO bus_info VALUES (%s, %s, %s, %s, %s, %s)",
            (bus_id,
             random.choice(routes),
             random.choice(stops),
             random.choice(stops),
             random.randint(5, 20),
             random.choice(depots))
        )
    db.commit()
    print("✅ Initial 10 buses inserted successfully!\n")

# -------------------- Real-Time Simulation (limited rounds) --------------------
for update_round in range(1, 6):  # 5 update rounds
    print(f"\n--- Update Round {update_round} ---")

    bus_id = random.randint(1, 10)
    next_stop = random.choice(stops)
    eta = random.randint(2, 15)

    cursor.execute("""
        UPDATE bus_info
        SET current_stop=%s, next_stop=%s, eta=%s
        WHERE bus_id=%s
    """, (next_stop, random.choice(stops), eta, bus_id))
    db.commit()

    cursor.execute("SELECT * FROM bus_info")
    for row in cursor.fetchall():
        print(row)

    print("-" * 50)
    time.sleep(2)

print("\n Simulation completed successfully!")
db.close()
