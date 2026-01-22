import pandas as pd
import sqlite3

df = pd.read_csv("data/hillstrom.csv")

conn = sqlite3.connect("uplift.db")

df.to_sql("hillstrom_raw",conn,if_exists = "replace", index = False)

conn.close()
