import pandas as pd
import matplotlib.pyplot as plt
import pymysql as py
import numpy as np
from sqlalchemy import create_engine
from tabulate import tabulate

pd.set_option('display.max_rows',50)
pd.set_option('display.max_columns',50)

print("AUTOMOBILE MANAGEMENT SYSTEM")
print("By Aryan Sajiv")
print("Grade 12")

x = 1
while x == 1:
    print('''Choose Module To Use: 
1. Vehicle Inventory.
2. Customer Details.
3. Exit.''')
    mod1 = int(input("Please enter your choice(1,2,3): "))
    print()

    if mod1 == 1:
        print("Vehicle Inventory.")
        print()        
        print('''Create a DataFrame using: 
1. An existing Database.
2. An existing CSV file.''')
        ch1 = int(input("Enter your choice from the menu(1,2):  "))
        print()  
        if ch1 == 1: 
            print("Importing from an existing Database")
            engine = create_engine("mysql+pymysql://root:Tbnrfrags2@localhost:3306/NEW_AUTOMOBILE_MANAGEMENT")
            df = pd.read_sql_query("SELECT * FROM VEHICLES", engine)
            vehicles = df.copy()
            print("Importing...")
            print()
            print("DataFrame created is:")
            print(tabulate(vehicles, headers='keys', tablefmt='grid'))
            print()

        elif ch1 == 2: 
            print("Importing from an existing CSV File.")
            df = pd.read_csv("vehicles.csv", header=0, names=["VehicleID", "Make", "Model", "Year", "Price", "Status", "Mileage", "FuelType", "Transmission"])
            vehicles = df.set_index('VehicleID')
            print("Importing...")
            print("DataFrame created is:")
            print(tabulate(vehicles, headers='keys', tablefmt='grid'))
            print()

        while True:
            print('''MENU: 
            1. Alter rows/tuples (Add, Update, Delete).
            2. Alter Columns/Fields (Add, Update, Delete, Rename).
            3. Filter/Retrieving data (Boolean Indexing, Retrieval).
            4. Plot a graph (Bar, Histogram, Line).
            5. Perform Attributes on DataFrame.
            6. Export to Database (SQL).
            7. Export to CSV.
            8. View DataFrame/Table.
            9. Retrieve Specific Data.
            10. Exit.''')
            ch2 = int(input("Enter your choice from the above menu(1-10): "))
            print()

            if ch2 == 1:
                print("""1. Alter rows/tuples : MENU
                1.Add a row
                2.Update a row
                3.Update a Particular Value
                4.Delete row""")
                ch3 = int(input("Enter Choice(1-4):"))

                if ch3 == 1:
                    print("1. Add a row")
                    new_row = {}
                    for col in vehicles.columns:
                        value = input(f"Enter value for {col}: ")
                        # Cast values based on expected column types
                        if vehicles[col].dtype == 'int64':
                            new_row[col] = int(value)
                        elif vehicles[col].dtype == 'float64':
                            new_row[col] = float(value)
                        else:
                            new_row[col] = str(value)  # Default to string if unsure
                    vehicles.loc[len(vehicles)] = new_row
                    print("Row added.")

                elif ch3 == 2:
                    print("2. Update a row")
                    row_id = int(input("Enter row index to update: "))
                    for col in vehicles.columns:
                        new_val = input(f"Enter new value for {col} (leave blank to skip): ")
                        if new_val:
                            vehicles.at[row_id, col] = new_val
                    print("Row updated.")

                elif ch3 == 3:
                    print("3. Update a Particular Value")
                    row_id = int(input("Enter row index: "))
                    col_name = input("Enter column name: ")
                    new_val = input("Enter new value: ")
                    vehicles.at[row_id, col_name] = new_val
                    print("Value updated.")

                elif ch3 == 4:
                    print("4. Delete row")
                    row_id = int(input("Enter row index to delete: "))
                    vehicles.drop(index=row_id, inplace=True)
                    vehicles.reset_index(drop=True, inplace=True)
                    print("Row deleted.")

            elif ch2 == 2:
                print("""1. Alter Columns/Fields : MENU
                1.Add a column.
                2.Update a column.
                3.Delete column.
                4.Rename a column.""")
                ch5 = int(input("Enter your choice(1-4):"))

                if ch5 == 1:
                    print("1. Add a column.")
                    col_name = input("Enter new column name: ")
                    default_val = input("Enter default value for new column: ")
                    vehicles[col_name] = default_val
                    print("Column added.")

                elif ch5 == 2:
                    print("2. Update a column.")
                    col_name = input("Enter column name to update: ")
                    new_val = input("Enter new value for entire column: ")
                    vehicles[col_name] = new_val
                    print("Column updated.")

                elif ch5 == 3:
                    print("3. Delete column.")
                    col_name = input("Enter column name to delete: ")
                    vehicles.drop(columns=[col_name], inplace=True)
                    print("Column deleted.")

                elif ch5 == 4:
                    print("4. Rename a column.")
                    old_name = input("Enter old column name: ")
                    new_name = input("Enter new column name: ")
                    vehicles.rename(columns={old_name: new_name}, inplace=True)
                    print("Column renamed.")

            elif ch2 == 3:
                print("3. Filter/Retrieving data")
                condition = input("Enter filter condition (e.g., Price > 20000): ")
                filtered_data = vehicles.loc[vehicles.eval(condition)]
                with pd.option_context("Expand_frame_repr", False):
                  print(filtered_data)

            elif ch2 == 4:
                print("4. Plot a graph")
                col_name = input("Enter column name to plot: ")
                plot_type = input("Enter plot type (bar/hist/line): ")
                if plot_type == "bar":
                    vehicles[col_name].value_counts().plot(kind="bar")
                elif plot_type == "hist":
                    vehicles[col_name].plot(kind="hist")
                elif plot_type == "line":
                    vehicles[col_name].plot(kind="line")
                plt.show()

            elif ch2 == 5:
                print("5. Perform Attributes on DataFrame.")
                print("DataFrame Attributes:")
                print(f"Number of Rows: {len(vehicles)}")
                print(f"Number of Columns: {len(vehicles.columns)}")
                print(f"Shape: {vehicles.shape}")
                print(f"Data Types:\n{vehicles.dtypes}")
                print(f"First 5 Rows:\n{vehicles.head()}")

            elif ch2 == 6:
                print("6. Export to Database (SQL)")
                if engine is None:
                    engine = create_engine("mysql+pymysql://root:Tbnrfrags2@localhost:3306/NEW_AUTOMOBILE_MANAGEMENT")
                vehicles.to_sql(name="vehicles", con=engine, if_exists="replace", index=False)
                print("Exported to Database.")

            elif ch2 == 7:
                print("7. Export to CSV")
                vehicles.to_csv("vehicles_updated.csv", index=False)
                print("Exported to CSV.")

            elif ch2 == 8:
                print("8. View DataFrame/Table")
                print("Current DataFrame:")
                print(tabulate(vehicles, headers='keys', tablefmt='grid'))

            elif ch2 == 9:
                print("9. Retrieve Specific Data")
                col_name = input("Enter column name to filter by: ")
                value = input(f"Enter value to filter {col_name} by: ")
                filtered_data = vehicles[vehicles[col_name] == value]
                print("Filtered Data:")
                print(tabulate(filtered_data, headers='keys', tablefmt='grid'))

            elif ch2 == 10:
                print("Exiting...")
                break

            else:
                print("Invalid option. Please try again.")

    elif mod1 == 2:  # Customer Details
        print("Customer Details.")
        # Importing customer data from CSV or Database
        print('''Create a DataFrame using: 
1. An existing Database.
2. An existing CSV file.''')
        ch1 = int(input("Enter your choice from the menu(1,2):  "))
        print()  
        if ch1 == 1: 
            print("Importing from an existing Database")
            engine = create_engine("mysql+pymysql://root:Lakshya2007@localhost:3306/NEW_AUTOMOBILE_MANAGEMENT")
            df = pd.read_sql_query("SELECT * FROM CUSTOMERS", engine)
            customers = df.set_index('CustomerID')
            print("Importing...")
            print("DataFrame created is:")
            print(tabulate(customers, headers='keys', tablefmt='grid'))
            print()

        elif ch1 == 2: 
            print("Importing from an existing CSV File.")
            df = pd.read_csv("customers.csv", header=0, names=["CustomerID", "Name", "Address", "Phone", "Email"])
            customers = df.set_index('CustomerID')
            print("Importing...")
            print("DataFrame created is:")
            print(tabulate(customers, headers='keys', tablefmt='grid'))
            print()

        while True:
            print('''MENU: 
            1. Alter rows/tuples (Add, Update, Delete).
            2. Alter Columns/Fields (Add, Update, Delete, Rename).
            3. Filter/Retrieving data (Boolean Indexing, Retrieval).
            4. Plot a graph (Bar, Histogram, Line).
            5. Perform Attributes on DataFrame.
            6. Export to Database (SQL).
            7. Export to CSV.
            8. View DataFrame/Table.
            9. Retrieve Specific Data.
            10. Exit.''')
            ch2 = int(input("Enter your choice from the above menu(1-10): "))
            print()

            if ch2 == 1:
                print("""1. Alter rows/tuples : MENU
                1.Add a row
                2.Update a row
                3.Update a Particular Value
                4.Delete row""")
                ch3 = int(input("Enter Choice(1-4):"))

                if ch3 == 1:
                    print("1. Add a row")
                    new_row = {}
                    for col in customers.columns:
                        value = input(f"Enter value for {col}: ")
                        new_row[col] = str(value)  # Assume all customer columns are strings
                    customers.loc[len(customers)] = new_row
                    print("Row added.")

                elif ch3 == 2:
                    print("2. Update a row")
                    row_id = int(input("Enter row index to update: "))
                    for col in customers.columns:
                        new_val = input(f"Enter new value for {col} (leave blank to skip): ")
                        if new_val:
                            customers.at[row_id, col] = new_val
                    print("Row updated.")

                elif ch3 == 3:
                    print("3. Update a Particular Value")
                    row_id = int(input("Enter row index: "))
                    col_name = input("Enter column name: ")
                    new_val = input("Enter new value: ")
                    customers.at[row_id, col_name] = new_val
                    print("Value updated.")

                elif ch3 == 4:
                    print("4. Delete row")
                    row_id = int(input("Enter row index to delete: "))
                    customers.drop(index=row_id, inplace=True)
                    customers.reset_index(drop=True, inplace=True)
                    print("Row deleted.")

            elif ch2 == 2:
                print("""1. Alter Columns/Fields : MENU
                1.Add a column.
                2.Update a column.
                3.Delete column.
                4.Rename a column.""")
                ch5 = int(input("Enter your choice(1-4):"))

                if ch5 == 1:
                    print("1. Add a column.")
                    col_name = input("Enter new column name: ")
                    default_val = input("Enter default value for new column: ")
                    customers[col_name] = default_val
                    print("Column added.")

                elif ch5 == 2:
                    print("2. Update a column.")
                    col_name = input("Enter column name to update: ")
                    new_val = input("Enter new value for entire column: ")
                    customers[col_name] = new_val
                    print("Column updated.")

                elif ch5 == 3:
                    print("3. Delete column.")
                    col_name = input("Enter column name to delete: ")
                    customers.drop(columns=[col_name], inplace=True)
                    print("Column deleted.")

                elif ch5 == 4:
                    print("4. Rename a column.")
                    old_name = input("Enter old column name: ")
                    new_name = input("Enter new column name: ")
                    customers.rename(columns={old_name: new_name}, inplace=True)
                    print("Column renamed.")
            
            elif ch2 == 3:
                print("3. Filter/Retrieving data")
                condition = input("Enter filter condition (e.g., Name == 'John'): ")
                filtered_data = customers.loc[customers.eval(condition)]
                print(filtered_data)
            
            elif ch2 == 4:
                print("4. Plot a graph")
                col_name = input("Enter column name to plot: ")
                plot_type = input("Enter plot type (bar/hist/line): ")
                if plot_type == "bar":
                    customers[col_name].value_counts().plot(kind="bar")
                elif plot_type == "hist":
                    customers[col_name].plot(kind="hist")
                elif plot_type == "line":
                    customers[col_name].plot(kind="line")
                plt.show()

            elif ch2 == 5:
                print("5. Perform Attributes on DataFrame.")
                print(f"Number of Rows: {len(customers)}")
                print(f"Number of Columns: {len(customers.columns)}")
                print(f"Shape: {customers.shape}")
                print(f"Data Types:\n{customers.dtypes}")
                print(f"First 5 Rows:\n{customers.head()}")

            elif ch2 == 6:
                print("6. Export to Database (SQL)")
                customers.to_sql(name="customers", con=engine, if_exists="replace", index=False)
                print("Exported to Database.")

            elif ch2 == 7:
                print("7. Export to CSV")
                customers.to_csv("customers_updated.csv", index=False)
                print("Exported to CSV.")

            elif ch2 == 8:
                print("8. View DataFrame/Table")
                print("Current DataFrame:")
                print(tabulate(customers, headers='keys', tablefmt='grid'))

            elif ch2 == 9:
                print("9. Retrieve Specific Data")
                col_name = input("Enter column name to filter by: ")
                value = input(f"Enter value to filter {col_name} by: ")
                filtered_data = customers[customers[col_name] == value]
                print("Filtered Data:")
                print(tabulate(filtered_data, headers='keys', tablefmt='grid'))

            elif ch2 == 10:
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
    
    elif mod1 == 3:  # Exit
        print("Exiting...")
        break
    else:
        print("Invalid module choice. Please try again.")
