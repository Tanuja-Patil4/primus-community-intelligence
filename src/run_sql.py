import sqlite3
from pathlib import Path

# ============================================================
# PRIMUS COMMUNITY INTELLIGENCE
# SQL QUERY RUNNER
# ============================================================

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database location
DB_PATH = BASE_DIR / "data" / "primus.db"

# SQL file location
SQL_PATH = BASE_DIR / "sql" / "analysis_queries.sql"


# ------------------------------------------------------------
# CONNECT TO DATABASE
# ------------------------------------------------------------

connection = sqlite3.connect(DB_PATH)

print("\n========================================")
print("PRIMUS SQL ANALYSIS")
print("========================================")

print(f"\nDatabase: {DB_PATH}")


# ------------------------------------------------------------
# READ SQL FILE
# ------------------------------------------------------------

with open(SQL_PATH, "r", encoding="utf-8") as file:
    sql_script = file.read()


# ------------------------------------------------------------
# SPLIT QUERIES
# ------------------------------------------------------------

queries = [
    query.strip()
    for query in sql_script.split(";")
    if query.strip()
]


# ------------------------------------------------------------
# EXECUTE QUERIES
# ------------------------------------------------------------

for number, query in enumerate(queries, start=1):

    # Ignore SQL comments when checking whether query is empty
    cleaned_query = "\n".join(
        line for line in query.splitlines()
        if not line.strip().startswith("--")
    ).strip()

    if not cleaned_query:
        continue

    print("\n----------------------------------------")
    print(f"QUERY {number}")
    print("----------------------------------------")

    try:
        cursor = connection.execute(query)

        # Check whether query returned data
        if cursor.description:

            columns = [column[0] for column in cursor.description]

            rows = cursor.fetchall()

            print(" | ".join(columns))
            print("-" * 80)

            for row in rows:
                print(" | ".join(str(value) for value in row))

            print(f"\nRows returned: {len(rows)}")

        else:
            print("Query executed successfully.")

    except Exception as error:
        print(f"ERROR: {error}")


# ------------------------------------------------------------
# CLOSE CONNECTION
# ------------------------------------------------------------

connection.close()

print("\n========================================")
print("SQL ANALYSIS COMPLETED")
print("========================================")