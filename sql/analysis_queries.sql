/* ============================================================
   PRIMUS COMMUNITY INTELLIGENCE
   SQL ANALYSIS LAYER

   Business Case:
   Analyze occupancy, resident engagement, satisfaction,
   service interactions and community-level performance.

   IMPORTANT:
   All data is synthetic and created for an academic
   portfolio case study inspired by the senior-living sector.
   ============================================================ */


/* ============================================================
   QUERY 1
   COMMUNITY OCCUPANCY
   ============================================================

   Business Question:
   What is the occupancy situation across communities?
*/

SELECT
    community_id,
    community_name,
    city,
    state,
    capacity,
    occupied_units,
    ROUND(occupancy_rate * 100, 2) AS occupancy_percentage,
    opening_year

FROM communities

ORDER BY occupancy_rate DESC;


/* ============================================================
   QUERY 2
   OVERALL OCCUPANCY
   ============================================================

   Business Question:
   What is the overall capacity utilization?
*/

SELECT
    SUM(capacity) AS total_capacity,

    SUM(occupied_units) AS total_occupied_units,

    ROUND(
        SUM(occupied_units) * 100.0
        / SUM(capacity),
        2
    ) AS overall_occupancy_percentage

FROM communities;


/* ============================================================
   QUERY 3
   LOW-OCCUPANCY COMMUNITIES
   ============================================================

   Business Question:
   Which communities have relatively lower occupancy?
*/

SELECT
    community_id,
    community_name,
    city,
    capacity,
    occupied_units,

    ROUND(
        occupancy_rate * 100,
        2
    ) AS occupancy_percentage

FROM communities

WHERE occupancy_rate < 0.75

ORDER BY occupancy_rate ASC;


/* ============================================================
   QUERY 4
   RESIDENT ENGAGEMENT OVERVIEW
   ============================================================

   Business Question:
   What does overall resident engagement look like?
*/

SELECT

    COUNT(*) AS total_monthly_records,

    COUNT(DISTINCT resident_id)
        AS unique_residents,

    ROUND(
        AVG(activities_attended),
        2
    ) AS avg_activities_attended,

    ROUND(
        AVG(unique_activity_types),
        2
    ) AS avg_activity_types,

    ROUND(
        AVG(service_requests),
        2
    ) AS avg_service_requests,

    ROUND(
        AVG(satisfaction_score),
        2
    ) AS avg_satisfaction

FROM resident_engagement;


/* ============================================================
   QUERY 5
   ENGAGEMENT LEVEL DISTRIBUTION
   ============================================================

   Business Question:
   How are residents distributed across engagement levels?
*/

SELECT

    engagement_level,

    COUNT(*) AS monthly_records,

    COUNT(DISTINCT resident_id)
        AS unique_residents

FROM resident_engagement

GROUP BY engagement_level

ORDER BY monthly_records DESC;


/* ============================================================
   QUERY 6
   COMMUNITY EXPERIENCE
   ============================================================

   Business Question:
   How does engagement and satisfaction vary by community?
*/

SELECT

    c.community_id,

    c.community_name,

    c.city,

    ROUND(
        AVG(e.activities_attended),
        2
    ) AS avg_activities_attended,

    ROUND(
        AVG(e.unique_activity_types),
        2
    ) AS avg_activity_types,

    ROUND(
        AVG(e.service_requests),
        2
    ) AS avg_service_requests,

    ROUND(
        AVG(e.satisfaction_score),
        2
    ) AS avg_satisfaction

FROM communities c

LEFT JOIN resident_engagement e

    ON c.community_id = e.community_id

GROUP BY

    c.community_id,
    c.community_name,
    c.city

ORDER BY avg_satisfaction DESC;


/* ============================================================
   QUERY 7
   OCCUPANCY + EXPERIENCE
   ============================================================

   Business Question:
   How do occupancy and resident experience compare
   across communities?
*/

SELECT

    c.community_id,

    c.community_name,

    c.city,

    ROUND(
        c.occupancy_rate * 100,
        2
    ) AS occupancy_percentage,

    ROUND(
        AVG(e.activities_attended),
        2
    ) AS avg_activities_attended,

    ROUND(
        AVG(e.satisfaction_score),
        2
    ) AS avg_satisfaction

FROM communities c

LEFT JOIN resident_engagement e

    ON c.community_id = e.community_id

GROUP BY

    c.community_id,
    c.community_name,
    c.city,
    c.occupancy_rate

ORDER BY occupancy_percentage DESC;


/* ============================================================
   QUERY 8
   COMMUNITY PERFORMANCE SEGMENTATION
   ============================================================

   Business Question:
   Which communities fall into different performance
   categories based on occupancy and satisfaction?

   NOTE:
   Thresholds are analytical assumptions for this
   synthetic case study.
*/

SELECT

    c.community_id,

    c.community_name,

    c.city,

    ROUND(
        c.occupancy_rate * 100,
        2
    ) AS occupancy_percentage,

    ROUND(
        AVG(e.satisfaction_score),
        2
    ) AS avg_satisfaction,

    CASE

        WHEN
            c.occupancy_rate >= 0.85
            AND AVG(e.satisfaction_score) >= 4.0

        THEN 'High Performing'


        WHEN
            c.occupancy_rate >= 0.75
            AND AVG(e.satisfaction_score) >= 3.5

        THEN 'Stable'


        WHEN
            c.occupancy_rate < 0.75
            OR AVG(e.satisfaction_score) < 3.5

        THEN 'Needs Attention'


        ELSE 'Monitor'

    END AS performance_category

FROM communities c

LEFT JOIN resident_engagement e

    ON c.community_id = e.community_id

GROUP BY

    c.community_id,
    c.community_name,
    c.city,
    c.occupancy_rate

ORDER BY occupancy_percentage DESC;


/* ============================================================
   QUERY 9
   SERVICE REQUESTS VS SATISFACTION
   ============================================================

   Business Question:
   Do communities with more service interactions also
   show different satisfaction levels?

   This is an association analysis, NOT a causal claim.
*/

SELECT

    c.community_id,

    c.community_name,

    ROUND(
        AVG(e.service_requests),
        2
    ) AS avg_service_requests,

    ROUND(
        AVG(e.satisfaction_score),
        2
    ) AS avg_satisfaction

FROM communities c

LEFT JOIN resident_engagement e

    ON c.community_id = e.community_id

GROUP BY

    c.community_id,
    c.community_name

ORDER BY avg_service_requests DESC;


/* ============================================================
   QUERY 10
   LOW-SATISFACTION RECORDS
   ============================================================

   Business Question:
   Where are lower satisfaction observations occurring?
*/

SELECT

    resident_id,

    community_id,

    month,

    activities_attended,

    service_requests,

    satisfaction_score,

    engagement_level

FROM resident_engagement

WHERE satisfaction_score < 3.0

ORDER BY satisfaction_score ASC;


/* ============================================================
   QUERY 11
   HIGH-ENGAGEMENT RECORDS
   ============================================================

   Business Question:
   What does highly engaged resident activity look like?
*/

SELECT

    resident_id,

    community_id,

    month,

    activities_attended,

    unique_activity_types,

    satisfaction_score,

    engagement_level

FROM resident_engagement

WHERE engagement_level = 'High'

ORDER BY activities_attended DESC;


/* ============================================================
   QUERY 12
   MONTHLY EXPERIENCE TREND
   ============================================================

   Business Question:
   Is resident engagement or satisfaction changing over time?
*/

SELECT

    month,

    ROUND(
        AVG(activities_attended),
        2
    ) AS avg_activities_attended,

    ROUND(
        AVG(service_requests),
        2
    ) AS avg_service_requests,

    ROUND(
        AVG(satisfaction_score),
        2
    ) AS avg_satisfaction

FROM resident_engagement

GROUP BY month

ORDER BY month;


/* ============================================================
   QUERY 13
   COMMUNITY MONTHLY TREND
   ============================================================

   Business Question:
   How does resident experience change over time
   within each community?
*/

SELECT

    community_id,

    month,

    ROUND(
        AVG(activities_attended),
        2
    ) AS avg_activities,

    ROUND(
        AVG(service_requests),
        2
    ) AS avg_service_requests,

    ROUND(
        AVG(satisfaction_score),
        2
    ) AS avg_satisfaction

FROM resident_engagement

GROUP BY

    community_id,
    month

ORDER BY

    community_id,
    month;


/* ============================================================
   QUERY 14
   RESIDENT ENGAGEMENT SEGMENTS
   ============================================================

   Business Question:
   How does satisfaction differ across engagement levels?
*/

SELECT

    engagement_level,

    COUNT(*) AS records,

    ROUND(
        AVG(activities_attended),
        2
    ) AS avg_activities,

    ROUND(
        AVG(service_requests),
        2
    ) AS avg_service_requests,

    ROUND(
        AVG(satisfaction_score),
        2
    ) AS avg_satisfaction

FROM resident_engagement

GROUP BY engagement_level

ORDER BY avg_satisfaction DESC;


/* ============================================================
   QUERY 15
   COMMUNITY MANAGEMENT VIEW
   ============================================================

   This is the main analytical output we can eventually
   feed into Power BI.
*/

SELECT

    c.community_id,

    c.community_name,

    c.city,

    c.state,

    c.capacity,

    c.occupied_units,

    ROUND(
        c.occupancy_rate * 100,
        2
    ) AS occupancy_percentage,

    ROUND(
        AVG(e.activities_attended),
        2
    ) AS avg_activity_participation,

    ROUND(
        AVG(e.unique_activity_types),
        2
    ) AS avg_activity_types,

    ROUND(
        AVG(e.service_requests),
        2
    ) AS avg_service_requests,

    ROUND(
        AVG(e.satisfaction_score),
        2
    ) AS avg_satisfaction,

    CASE

        WHEN
            c.occupancy_rate >= 0.85
            AND AVG(e.satisfaction_score) >= 4.0

        THEN 'High Performing'


        WHEN
            c.occupancy_rate >= 0.75
            AND AVG(e.satisfaction_score) >= 3.5

        THEN 'Stable'


        WHEN
            c.occupancy_rate < 0.75
            OR AVG(e.satisfaction_score) < 3.5

        THEN 'Needs Attention'


        ELSE 'Monitor'

    END AS performance_category

FROM communities c

LEFT JOIN resident_engagement e

    ON c.community_id = e.community_id

GROUP BY

    c.community_id,
    c.community_name,
    c.city,
    c.state,
    c.capacity,
    c.occupied_units,
    c.occupancy_rate

ORDER BY
    avg_satisfaction DESC;