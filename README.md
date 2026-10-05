# Primus Community Intelligence 📊

An end-to-end analytics project for a **synthetic senior-living business case**, combining Python, SQL, SQLite and Power BI to analyze community performance, resident engagement, satisfaction and operational metrics.

> **Note:** This project uses completely synthetic data created for academic and portfolio purposes. It does not use or represent confidential data from any real senior-living organization.

---

## 📌 Project Overview

**Primus Community Intelligence** is designed as a business analytics solution for a senior-living organization operating multiple residential communities.

The project answers questions such as:

- How are communities performing in terms of occupancy?
- How many residents are represented across communities?
- What is the overall occupancy rate?
- How does resident engagement vary?
- How does satisfaction differ across communities?
- Which communities may require management attention?
- What operational metrics can management monitor through a dashboard?

---

## 🎯 Business Objective

The objective is to build a centralized analytics workflow that transforms raw resident and community data into actionable business insights.

The solution follows:

**Data Generation → Data Validation → Database → SQL Analysis → Power BI Dashboard**

---

## 🏗️ Project Architecture

```text
                    Synthetic Business Data
                              │
                              ▼
                     Python Data Generation
                              │
                              ▼
                           CSV Files
                              │
                              ▼
                         SQLite Database
                              │
                              ▼
                        SQL Analysis
                              │
                              ▼
                       Power BI Data Model
                              │
                              ▼
                    Executive Dashboard
                              │
                              ▼
                     Business Insights
```

---

## 📊 Power BI Dashboard

### Executive Overview

The dashboard provides an executive-level view of:

- Total Communities
- Total Residents
- Overall Occupancy
- Total Capacity
- Average Satisfaction
- Service Requests
- Community-level performance
- Resident residence type
- City-level filtering

![Primus Community Intelligence Executive Dashboard](powerbi/screenshots/executive_overview.png)

---

## 📈 Dashboard Highlights

The current dashboard contains:

### KPI Cards
- **8 Communities**
- **1,602 Residents**
- **2,050 Total Capacity**
- **78% Overall Occupancy**
- Satisfaction metrics
- Service request metrics

### Interactive Filters
- Residence Type
- City

### Visual Analysis
- Community comparison
- Satisfaction distribution
- Geographic/state-level analysis
- Resident and operational KPIs

---

## 🗂️ Dataset

The project uses synthetic datasets representing:

### Communities

Contains:

- Community ID
- Community Name
- City
- State
- Capacity
- Occupied Units
- Occupancy Rate
- Opening Year

### Residents

Contains:

- Resident ID
- Community ID
- Age
- Gender
- Residence Type
- Move-in Date

### Resident Engagement

Contains:

- Resident ID
- Community ID
- Month
- Activities Attended
- Unique Activity Types
- Service Requests
- Satisfaction Score
- Engagement Level

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data generation, validation and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical calculations |
| Faker | Synthetic data generation |
| SQLite | Relational database |
| SQL | Business analysis and aggregation |
| Power BI | Dashboard and visualization |
| DAX | KPI calculations |
| Git/GitHub | Version control and portfolio |

---

## 📁 Project Structure

```text
primus-community-intelligence/
│
├── data/
│   ├── communities.csv
│   ├── residents.csv
│   ├── resident_engagement.csv
│   └── community_experience_summary.csv
│
├── models/
│
├── notebooks/
│
├── outputs/
│
├── powerbi/
│   ├── primus_community_intelligence.pbix
│   └── screenshots/
│       └── executive_overview.png
│
├── sql/
│
├── src/
│   ├── generate_data.py
│   ├── generate_engagement.py
│   ├── load_database.py
│   ├── run_sql.py
│   └── analysis_queries.sql
│
├── .gitignore
└── README.md
```

---

## 🔄 Analytical Workflow

### 1. Data Generation

Python was used to create realistic synthetic community and resident datasets.

### 2. Data Validation

The generated data was checked for:

- Missing values
- Duplicate IDs
- Valid age ranges
- Occupancy consistency
- Resident-to-community reconciliation

### 3. Database Creation

The CSV datasets were loaded into SQLite to create a relational analytical database.

### 4. SQL Analysis

SQL was used for:

- Aggregations
- Joins
- Grouping
- Occupancy analysis
- Satisfaction analysis
- Engagement analysis
- Community segmentation
- Monthly trends

### 5. Power BI

Power BI was used to create an interactive executive dashboard with KPIs, filters and visual analysis.

---

## 💡 Skills Demonstrated

This project demonstrates practical skills in:

- Data Analytics
- Data Cleaning
- Synthetic Data Generation
- Python
- SQL
- SQLite
- Data Modeling
- Power BI
- DAX
- Business Intelligence
- KPI Development
- Data Visualization
- Business Problem Solving
- Git & GitHub

---

## 🚀 Future Development

Planned extensions include:

- Exploratory Data Analysis using Python
- Statistical analysis
- Correlation analysis
- Predictive analytics
- Service demand forecasting
- Machine learning models
- Additional Power BI dashboard pages
- Automated data pipelines

---

## ⚠️ Disclaimer

This is an **academic portfolio project** using synthetic data.

The community names, resident records, operational metrics and business figures are artificially generated and should not be interpreted as actual data from any real organization.

---

## 👩‍💻 Author

**Tanuja Patil**

MBA – Artificial Intelligence & Data Science

RV University, Bengaluru

GitHub: [Tanuja-Patil4](https://github.com/Tanuja-Patil4)

---

⭐ If you find this project useful, consider starring the repository.
