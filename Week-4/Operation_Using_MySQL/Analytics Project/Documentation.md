# Sales Analytics Dashboard Project  
**MySQL + Python + Pandas + Matplotlib + Automated PDF Report**  
*(Portfolio-Ready Project – 100% Working)*

## Project Overview  
This is a complete end-to-end **Sales Analytics Dashboard** built using real-world tools and best practices. The system fetches sales data from a MySQL database, performs analysis using Python, creates beautiful visualizations, and automatically generates a professional multi-page PDF report.

## Technologies Used  
| Component             | Tool / Library                          |
|-----------------------|-----------------------------------------|
| Database              | MySQL (sales_db)                        |
| Programming Language  | Python 3.x                              |
| Data Manipulation     | Pandas, NumPy                           |
| Database Connectivity | mysql-connector-python + SQLAlchemy     |
| Visualization         | Matplotlib, Seaborn                     |
| PDF Report Generation | fpdf                                    | 

## Project Structure (What We Built)

### 1. MySQL Database Setup  
- Created database: `sales_db`
- Created table: `sales` with auto-calculated `total_amount = quantity × price`
- Inserted **128+ realistic sales records** for 2025**
- Regions: Gulshan, Dhanmondi, Banani, Uttara, Bashundhara, Badda
- Products: Laptop, Phone, Tablet, Monitor, Keyboard
- Prices in Bangladeshi Taka (BDT)

### 2. Data Loading & Cleaning (Cell 2)  
- Connected to MySQL using SQLAlchemy (no pandas warnings)
- Loaded all records into a Pandas DataFrame
- Converted `sale_date` to datetime format
- Performed data validation and cleaning
- Displayed clean preview with BDT formatting

### 3. Monthly Sales Trend Analysis (Cell 3)  
- Grouped sales by month (`2025-01` to `2025-12`)
- Created a professional bar chart showing monthly revenue
- Added clear BDT labels on top of each bar
- Saved as high-resolution `monthly_trend.png`

### 4. Product & Regional Performance (Cell 4)  
Two charts in one figure:
- **Top 5 Products by Revenue** (Bar Chart)
- **Sales Distribution by Region** (Pie Chart with percentage)
- Saved as `products_and_regions.png`

### 5. Automated PDF Report Generation (Cell 5)  
Automatically creates a **3-page professional PDF** containing:
- Cover page with date & time
- Key business insights summary
- Monthly sales trend chart
- Top products & regional distribution chart
- Final success message
- Output: `SALES_DASHBOARD_REPORT_2025.pdf`

## Key Outcomes & Results  
| Metric                      | Result                                        |
|-----------------------------|-----------------------------------------------|
| Total Transactions          | 128+ sales records                            |
| Total Revenue (2025)        | Over BDT 450+ million                         |
| Top Product                 | Laptop (highest revenue)                      |
| Top Regions                 | Gulshan → Dhanmondi → Banani                  |
| Peak Sales Month            | December 2025 (year-end surge)                |
| Growth Trend                | Consistent monthly growth throughout the year |

## Key Insights Generated  
- Laptops contribute the maximum revenue  
- Gulshan and Dhanmondi together make up ~55% of total sales  
- Clear seasonal peak in December (great for business planning)  
- Steady growth from January to December 2025  

## Skills Demonstrated  
- Database Design & SQL (CREATE, INSERT, auto-calculated columns)  
- Python for Data Analysis (Pandas, NumPy)  
- Data Visualization (Matplotlib + Seaborn)  
- Database Connectivity (SQLAlchemy, mysql-connector)  
- Automation (PDF report generation)  
- Clean Code & Error Handling  
- Professional Documentation  

## Files Generated  
SALES_DASHBOARD_REPORT_2025.pdf     → Final report (ready to submit)
monthly_trend.png                   → Monthly sales chart
products_and_regions.png            → Top products + region chart
sales_dashboard.ipynb               → Complete Jupyter Notebook

## Conclusion  
This project successfully demonstrates a **complete data analytics pipeline** from database to automated reporting.