## Vendor-Performance-Analysis
Vendor Performance Analysis is a comprehensive data-driven project that consolidates multiple SQL-based data sources to evaluate and visualize supplier performance. By integrating, cleaning, and analyzing key operational metrics, the project enables organizations to gain actionable insights into their procurement ecosystem using Power BI dashboards.
## Objective
- Identify high-performing and underperforming vendors
- Analyze vendor delivery timelines and delays
- Evaluate quality issues and returns
- Recommend actions for vendor optimization
## Tools & Technologies
- Python 3.x – Data wrangling & transformation
- Pandas – Data manipulation
- SQLite3 – Querying relational data
- Power BI – Interactive data visualization
- Matplotlib / Seaborn – Optional EDA plotting (if used)
- Logging – For debugging and traceability
## Project Workflow Overview
1.  Data Ingestion & Transformation
Raw vendor data was ingested from multiple SQL sources.
A dedicated transformation script (script.ipynb) was used to clean, normalize, and consolidate data.
Key transformations included:
- Standardizing vendor IDs and names
- Aggregating sales, purchases, and inventory metrics
- Joining transactional tables to master datasets for enriched context

2. Exploratory Data Analysis (EDA)
Conducted preliminary analysis using Python (pandas, seaborn, matplotlib) to understand data quality and distribution:
- Handled missing values, identified outliers, and removed duplicates
- Grouped data by vendor and brand categories to compute initial metrics
- Derived summary statistics for key features (sales, purchase cost, quantity, etc.)
- Created optional visualizations:
- Bar charts for sales vs. profit by brand
- Box plots to detect cost anomalies
- Correlation heatmaps for identifying KPI relationships

3.  Vendor Performance Analysis
Used Power BI to develop a comprehensive analytical dashboard that answers critical business questions, such as:

 Key Business Insights
- Promotional/Pricing Optimization:
Identified brands with low sales but high profit margins, indicating potential for targeted promotions or price adjustments.
- Top Performers:
Highlighted vendors and brands with the highest sales volume, helping to prioritize partnerships.
- Spend Analysis:
Assessed which vendors contribute the most to total purchase value, enabling focused negotiations.
- Vendor Dependency:
Measured procurement dependency on top vendors to identify risks and explore diversification strategies.
- Bulk Purchase Optimization:
Analyzed unit price trends vs. purchase volume to uncover the optimal order quantity for cost savings.
- Inventory Capital Lock:
Calculated the amount of capital tied up in unsold inventory per vendor, helping to identify slow-moving suppliers.

4.  Power BI Dashboard
     - dashboard.png
