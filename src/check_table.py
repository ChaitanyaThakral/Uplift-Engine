import sqlite3

conn = sqlite3.connect("uplift.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM uplift_dataset;")

data = cursor.fetchall()
for i in range(5):
    print(data[i])

conn.close()
