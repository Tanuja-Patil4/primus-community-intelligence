import sqlite3
import pandas as pd
from pathlib import Path


# ------------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DB_PATH = BASE_DIR / "data" / "primus.db"


# ------------------------------------------------------------
# CONNECT TO SQLITE DATABASE
# ------------------------------------------------------------

connection = sqlite3.connect(DB_PATH)


# ------------------------------------------------------------
# LOAD CSV FILES
# ------------------------------------------------------------

communities = pd.read_csv(
    DATA_DIR / "communities.csv"
)

residents = pd.read_csv(
    DATA_DIR / "residents.csv"
)

resident_engagement = pd.read_csv(
    DATA_DIR / "resident_engagement.csv"
)

community_experience = pd.read_csv(
    DATA_DIR / "community_experience_summary.csv"
)


# ------------------------------------------------------------
# WRITE DATA INTO SQLITE
# ------------------------------------------------------------

communities.to_sql(
    "communities",
    connection,
    if_exists="replace",
    index=False
)

residents.to_sql(
    "residents",
    connection,
    if_exists="replace",
    index=False
)

resident_engagement.to_sql(
    "resident_engagement",
    connection,
    if_exists="replace",
    index=False
)

community_experience.to_sql(
    "community_experience",
    connection,
    if_exists="replace",
    index=False
)


# ------------------------------------------------------------
# VERIFY DATABASE
# ------------------------------------------------------------

tables = pd.read_sql(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """,
    connection
)

print("\n==============================")
print("PRIMUS DATABASE CREATED")
print("==============================")

print("\nTables:")
print(tables)


# ------------------------------------------------------------
# CHECK ROW COUNTS
# ------------------------------------------------------------

for table in [
    "communities",
    "residents",
    "resident_engagement",
    "community_experience"
]:

    result = pd.read_sql(
        f"SELECT COUNT(*) AS row_count FROM {table}",
        connection
    )

    print(
        f"{table}: "
        f"{result.iloc[0]['row_count']} rows"
    )


# ------------------------------------------------------------
# CLOSE CONNECTION
# ------------------------------------------------------------

connection.close()

print("\nDatabase saved to:")
print(DB_PATH)

print("\nDatabase setup completed successfully.")
