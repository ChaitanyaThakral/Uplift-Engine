import sqlite3

conn = sqlite3.connect("uplift.db")
cursor = conn.cursor()

query ='''
DROP TABLE IF EXISTS uplift_dataset;

CREATE TABLE uplift_dataset AS
SELECT 
    recency,
    history_segment,
    history,
    mens,
    womens,
    zip_code,
    newbie,
    channel,
    CASE 
        WHEN segment = 'No E-Mail' THEN 0
        ELSE 1
    END AS treatment,
    visit,
    CASE 
        WHEN conversion = 1 THEN 1 
        ELSE 0
    END AS target
FROM hillstrom_raw;'''

cursor.executescript(query)
conn.commit()
conn.close()