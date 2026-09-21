# ============================================================
# PRIMUS COMMUNITY INTELLIGENCE
# Resident Experience & Engagement Data
# ============================================================

import pandas as pd
import numpy as np


# ------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------

np.random.seed(42)


# ------------------------------------------------------------
# 2. LOAD RESIDENT DATA
# ------------------------------------------------------------

residents_df = pd.read_csv(
    "data/residents.csv"
)


# ------------------------------------------------------------
# 3. DEFINE ANALYSIS PERIOD
# ------------------------------------------------------------

months = pd.date_range(
    start="2026-01-01",
    end="2026-06-01",
    freq="MS"
)


# ------------------------------------------------------------
# 4. ACTIVITY TYPES
# ------------------------------------------------------------

activity_types = [
    "Social",
    "Learning",
    "Cultural",
    "Recreation",
    "Community"
]


# ------------------------------------------------------------
# 5. GENERATE MONTHLY ENGAGEMENT
# ------------------------------------------------------------

engagement_records = []


for _, resident in residents_df.iterrows():

    # Resident-specific baseline engagement
    base_engagement = np.random.poisson(
        lam=4
    )

    for month in months:

        # Small month-to-month variation
        monthly_variation = np.random.normal(
            loc=0,
            scale=1
        )

        activities_attended = max(
            0,
            int(
                base_engagement
                + monthly_variation
            )
        )

        # Number of different activity categories
        unique_activity_types = min(
            len(activity_types),
            max(
                0,
                int(
                    np.random.normal(
                        loc=min(activities_attended, 4),
                        scale=1
                    )
                )
            )
        )

        # Service interactions
        service_requests = max(
            0,
            int(
                np.random.poisson(
                    lam=1.2
                )
            )
        )

        # Synthetic satisfaction signal
        # Higher engagement generally contributes
        # to somewhat higher satisfaction, but with noise.

        satisfaction = (
            3.2
            + 0.18 * activities_attended
            - 0.10 * service_requests
            + np.random.normal(0, 0.55)
        )

        satisfaction = np.clip(
            satisfaction,
            1,
            5
        )

        engagement_records.append({

            "resident_id":
                resident["resident_id"],

            "community_id":
                resident["community_id"],

            "month":
                month,

            "activities_attended":
                activities_attended,

            "unique_activity_types":
                unique_activity_types,

            "service_requests":
                service_requests,

            "satisfaction_score":
                round(
                    satisfaction,
                    1
                )
        })


# ------------------------------------------------------------
# 6. CREATE DATAFRAME
# ------------------------------------------------------------

engagement_df = pd.DataFrame(
    engagement_records
)


# ------------------------------------------------------------
# 7. ADD ENGAGEMENT LEVEL
# ------------------------------------------------------------

def classify_engagement(value):

    if value >= 7:
        return "High"

    elif value >= 4:
        return "Medium"

    else:
        return "Low"


engagement_df["engagement_level"] = (
    engagement_df["activities_attended"]
    .apply(classify_engagement)
)


# ------------------------------------------------------------
# 8. DISPLAY SAMPLE
# ------------------------------------------------------------

print("\n========================================")
print("RESIDENT ENGAGEMENT SAMPLE")
print("========================================")

print(
    engagement_df.head(10)
)


# ------------------------------------------------------------
# 9. DATASET SIZE
# ------------------------------------------------------------

print("\nDataset shape:")

print(
    engagement_df.shape
)


# ------------------------------------------------------------
# 10. BASIC DATA QUALITY CHECKS
# ------------------------------------------------------------

print("\n========================================")
print("DATA QUALITY CHECKS")
print("========================================")


print(
    "\nMissing values:"
)

print(
    engagement_df.isnull().sum()
)


print(
    "\nDuplicate rows:"
)

print(
    engagement_df.duplicated().sum()
)


print(
    "\nSatisfaction range:"
)

print(
    engagement_df["satisfaction_score"].min(),
    "to",
    engagement_df["satisfaction_score"].max()
)


# ------------------------------------------------------------
# 11. ENGAGEMENT LEVEL DISTRIBUTION
# ------------------------------------------------------------

print("\n========================================")
print("ENGAGEMENT LEVEL DISTRIBUTION")
print("========================================")

print(
    engagement_df["engagement_level"]
    .value_counts()
)


# ------------------------------------------------------------
# 12. COMMUNITY-LEVEL SUMMARY
# ------------------------------------------------------------

community_summary = (

    engagement_df
    .groupby("community_id")
    .agg(
        average_activities=(
            "activities_attended",
            "mean"
        ),

        average_satisfaction=(
            "satisfaction_score",
            "mean"
        ),

        average_service_requests=(
            "service_requests",
            "mean"
        )
    )

    .reset_index()
)


print("\n========================================")
print("COMMUNITY EXPERIENCE SUMMARY")
print("========================================")

print(
    community_summary
)


# ------------------------------------------------------------
# 13. EXPORT DATA
# ------------------------------------------------------------

engagement_df.to_csv(
    "data/resident_engagement.csv",
    index=False
)


community_summary.to_csv(
    "data/community_experience_summary.csv",
    index=False
)


print("\n========================================")
print("DATA EXPORT")
print("========================================")

print(
    "Saved: data/resident_engagement.csv"
)

print(
    "Saved: data/community_experience_summary.csv"
)

print(
    "\nEngagement data generation completed successfully."
)