import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def run_eda():
    conn = sqlite3.connect("uplift.db")
    df = pd.read_sql("SELECT * FROM uplift_dataset",conn)
    conn.close()

    # GOAL: Prove that the people who got the email (Treatment) are identical to the people who didn't (Control). 
    print(df.head())
    counts =  df.groupby(['treatment', 'history_segment']).size().unstack()
    counts.T.plot(kind='bar')
    plt.xlabel("History Segment")
    plt.ylabel("Count")
    plt.title("Treatment vs Control Distribution by History Segment")
    plt.legend(["Control (0)", "Treatment (1)"])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_eda()