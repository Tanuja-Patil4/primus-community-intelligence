# ============================================================
# PRIMUS COMMUNITY INTELLIGENCE
# Data Generation & Quality Validation
# ============================================================

import pandas as pd
import numpy as np
from faker import Faker


# ------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------

np.random.seed(42)
fake = Faker()
Faker.seed(42)


# ------------------------------------------------------------
# 2. COMMUNITY MASTER DATA
# ------------------------------------------------------------

communities = [
    {
        "community_id": "C001",
        "community_name": "Primus Harmony",
        "city": "Bengaluru",
        "state": "Karnataka",
        "capacity": 300,
        "opening_year": 2023
    },
    {
        "community_id": "C002",
        "community_name": "Primus Serenity",
        "city": "Hyderabad",
        "state": "Telangana",
        "capacity": 250,
        "opening_year": 2024
    },
    {
        "community_id": "C003",
        "community_name": "Primus Haven",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "capacity": 275,
        "opening_year": 2022
    },
    {
        "community_id": "C004",
        "community_name": "Primus Vista",
        "city": "Pune",
        "state": "Maharashtra",
        "capacity": 225,
        "opening_year": 2024
    },
    {
        "community_id": "C005",
        "community_name": "Primus Gardens",
        "city": "Mumbai",
        "state": "Maharashtra",
        "capacity": 325,
        "opening_year": 2023
    },
    {
        "community_id": "C006",
        "community_name": "Primus Harmony North",
        "city": "Delhi",
        "state": "Delhi",
        "capacity": 250,
        "opening_year": 2025
    },
    {
        "community_id": "C007",
        "community_name": "Primus Meadows",
        "city": "Kochi",
        "state": "Kerala",
        "capacity": 200,
        "opening_year": 2023
    },
    {
        "community_id": "C008",
        "community_name": "Primus Courtyard",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "capacity": 225,
        "opening_year": 2024
    }
]


# ------------------------------------------------------------
# 3. CREATE COMMUNITY DATAFRAME
# ------------------------------------------------------------

communities_df = pd.DataFrame(communities)


# ------------------------------------------------------------
# 4. SYNTHETIC OCCUPANCY DATA
# ------------------------------------------------------------

# These figures are synthetic assumptions for the case study.
occupancy_rates = [
    0.82, 0.76, 0.91, 0.68,
    0.87, 0.63, 0.79, 0.73
]

communities_df["occupancy_rate"] = occupancy_rates

communities_df["occupied_units"] = (
    communities_df["capacity"]
    * communities_df["occupancy_rate"]
).round().astype(int)


# ------------------------------------------------------------
# 5. DISPLAY COMMUNITY DATA
# ------------------------------------------------------------

print("\n========================================")
print("COMMUNITY DATA")
print("========================================")
print(communities_df)
print("\nDataset shape:", communities_df.shape)


# ------------------------------------------------------------
# 6. GENERATE RESIDENT DATA
# ------------------------------------------------------------

residents = []
resident_counter = 1

for community in communities:

    occupied = int(
        communities_df.loc[
            communities_df["community_id"] == community["community_id"],
            "occupied_units"
        ].iloc[0]
    )

    for _ in range(occupied):

        resident = {
            "resident_id": f"R{resident_counter:05d}",
            "community_id": community["community_id"],
            "age": int(
                np.clip(
                    np.random.normal(70, 7),
                    55,
                    90
                )
            ),
            "gender": np.random.choice(
                ["Male", "Female"],
                p=[0.48, 0.52]
            ),
            "residence_type": np.random.choice(
                ["1BHK", "2BHK", "3BHK"],
                p=[0.25, 0.55, 0.20]
            ),
            "move_in_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            )
        }

        residents.append(resident)
        resident_counter += 1


# ------------------------------------------------------------
# 7. CREATE RESIDENT DATAFRAME
# ------------------------------------------------------------

residents_df = pd.DataFrame(residents)


# ------------------------------------------------------------
# 8. DISPLAY RESIDENT DATA
# ------------------------------------------------------------

print("\n========================================")
print("RESIDENT DATA SAMPLE")
print("========================================")
print(residents_df.head(10))
print("\nResident dataset shape:", residents_df.shape)


# ------------------------------------------------------------
# 9. DATA QUALITY CHECKS
# ------------------------------------------------------------

print("\n========================================")
print("DATA QUALITY CHECKS")
print("========================================")

print("\nTotal residents:", len(residents_df))

print("\nMissing values:")
print(residents_df.isnull().sum())

duplicate_ids = residents_df["resident_id"].duplicated().sum()

print("\nDuplicate resident IDs:", duplicate_ids)

print(
    "\nAge range:",
    residents_df["age"].min(),
    "to",
    residents_df["age"].max()
)


# ------------------------------------------------------------
# 10. RESIDENTS BY COMMUNITY
# ------------------------------------------------------------

community_resident_counts = (
    residents_df
    .groupby("community_id")
    .size()
    .reset_index(name="resident_count")
)

print("\n========================================")
print("RESIDENTS BY COMMUNITY")
print("========================================")
print(community_resident_counts)


# ------------------------------------------------------------
# 11. OCCUPANCY VS RESIDENT VALIDATION
# ------------------------------------------------------------

validation = (
    communities_df[
        ["community_id", "capacity", "occupied_units"]
    ]
    .merge(
        community_resident_counts,
        on="community_id",
        how="left"
    )
)

validation["difference"] = (
    validation["occupied_units"]
    - validation["resident_count"]
)

print("\n========================================")
print("OCCUPANCY VS RESIDENT VALIDATION")
print("========================================")
print(validation)


# ------------------------------------------------------------
# 12. FINAL VALIDATION
# ------------------------------------------------------------

validation_passed = (
    (validation["difference"] == 0).all()
    and residents_df["resident_id"].is_unique
    and residents_df.isnull().sum().sum() == 0
    and residents_df["age"].between(55, 90).all()
)

print("\n========================================")
print("FINAL VALIDATION")
print("========================================")

print("Validation passed:", validation_passed)


# ------------------------------------------------------------
# 13. PROJECT SUMMARY
# ------------------------------------------------------------

print("\n========================================")
print("PROJECT DATA SUMMARY")
print("========================================")

print("Communities:", len(communities_df))
print("Total capacity:", communities_df["capacity"].sum())
print("Total occupied units:", communities_df["occupied_units"].sum())
print("Total residents:", len(residents_df))

overall_occupancy = (
    communities_df["occupied_units"].sum()
    / communities_df["capacity"].sum()
    * 100
)

print(
    "Overall occupancy rate:",
    round(overall_occupancy, 2),
    "%"
)


# ------------------------------------------------------------
# 14. EXPORT DATASETS
# ------------------------------------------------------------

communities_df.to_csv(
    "data/communities.csv",
    index=False
)

residents_df.to_csv(
    "data/residents.csv",
    index=False
)

print("\n========================================")
print("DATA EXPORT")
print("========================================")

print("Communities saved to: data/communities.csv")
print("Residents saved to: data/residents.csv")

print("\nData generation completed successfully.")
