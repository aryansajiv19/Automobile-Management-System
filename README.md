# Automobile Management System

A command-line records system for a car dealership that manages vehicle inventory and customer data in MySQL or CSV, with pandas-based querying, charts and export.

```text
Enter column name to filter by: FuelType
Enter value to filter FuelType by: Electric
+-------------+--------+---------+--------+---------+-----------+-----------+------------+----------------+
|   VehicleID | Make   | Model   |   Year |   Price | Status    |   Mileage | FuelType   | Transmission   |
+=============+========+=========+========+=========+===========+===========+============+================+
|          11 | Tesla  | Model 3 |   2022 |   45000 | Available |      3000 | Electric   | Automatic      |
+-------------+--------+---------+--------+---------+-----------+-----------+------------+----------------+
```

## Overview

The application covers the day-to-day record keeping of a small dealership: which vehicles are in stock, what they cost, and who the customers are. Data is loaded into a pandas DataFrame, edited and queried through an interactive menu, and written back when the user chooses to export.

It was developed as a Grade 12 Informatics Practices project.

## Highlights

- **Two storage back ends.** The same operations work on a MySQL table (SQLAlchemy with PyMySQL) or a CSV file.
- **Expression queries.** Filters accept pandas expressions such as `Price < 25000 and Status == "Available"`.
- **Safe editing.** All changes apply to an in-memory copy; nothing is written until an explicit export.

## How it works

1. Choose a module (vehicle inventory or customer details) and a source (MySQL or CSV).
2. The data is loaded into a DataFrame and displayed as a formatted table.
3. Edit rows and columns, filter, look up exact values, inspect the schema, or chart a column with matplotlib.
4. Export the result to MySQL or to a new CSV file.

## Engineering decisions

**A DataFrame as the working copy.** Loading everything into pandas gives filtering, type inspection and plotting for free, and lets the user experiment without touching the source. The trade-off is that the whole dataset must fit in memory, which is appropriate for a single dealership's records.

**Credentials from the environment.** The database connection string is read from `MYSQL_URL` rather than stored in the source, so no credentials live in the repository.

## Tech stack

**Language:** Python 3.9+  
**Data:** pandas, SQLAlchemy, PyMySQL, MySQL 8  
**Output:** matplotlib, tabulate

## Getting started

```bash
pip install -r requirements.txt
python pyboardproject.py
```

Choose **Vehicle inventory**, then **CSV file**, to run with the included sample data. For MySQL, load `ipboardprojectsql_code.sql` and set `MYSQL_URL`, for example `mysql+pymysql://user:password@localhost:3306/NEW_AUTOMOBILE_MANAGEMENT`.

## Future work

- **Preserve the schema on export.** `to_sql(if_exists="replace")` recreates the table and drops its primary key, auto-increment and unique email constraint; upserting changed rows would keep them.
- **One generic module.** The vehicle and customer modules are near-duplicates and could share a single table editor.
- **Align the customer CSV.** `customers.csv` is empty and its expected headers differ from the SQL schema, so customers currently require MySQL.
- **Tests** for the filter and export paths.
