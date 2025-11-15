-- Create a new database
CREATE DATABASE IF NOT EXISTS NEW_AUTOMOBILE_MANAGEMENT;
USE NEW_AUTOMOBILE_MANAGEMENT;

-- Create the VEHICLES Table
CREATE TABLE IF NOT EXISTS VEHICLES (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    Make VARCHAR(50) NOT NULL,
    Model VARCHAR(50) NOT NULL,
    Year INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(20) NOT NULL,
    Mileage INT NOT NULL,
    FuelType VARCHAR(30) NOT NULL,
    Transmission VARCHAR(30) NOT NULL
);

-- Create the CUSTOMERS Table without the PhoneNumber column
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Address TEXT NOT NULL
);

-- Insert sample data into VEHICLES table
INSERT INTO VEHICLES (Make, Model, Year, Price, Status, Mileage, FuelType, Transmission) VALUES
('Toyota', 'Corolla', 2020, 20000.00, 'Available', 15000, 'Petrol', 'Automatic'),
('Honda', 'Civic', 2019, 18000.00, 'Sold', 20000, 'Diesel', 'Manual'),
('Ford', 'Focus', 2021, 22000.00, 'Available', 10000, 'Petrol', 'Automatic'),
('Chevrolet', 'Malibu', 2018, 16000.00, 'Sold', 30000, 'Petrol', 'Manual'),
('Hyundai', 'Elantra', 2022, 25000.00, 'Available', 5000, 'Hybrid', 'Automatic'),
('BMW', '3 Series', 2020, 35000.00, 'Available', 20000, 'Diesel', 'Automatic'),
('Audi', 'A4', 2019, 34000.00, 'Sold', 22000, 'Petrol', 'Automatic'),
('Mercedes', 'C-Class', 2021, 40000.00, 'Available', 8000, 'Diesel', 'Automatic'),
('Nissan', 'Altima', 2020, 23000.00, 'Sold', 18000, 'Petrol', 'Manual'),
('Kia', 'Optima', 2018, 17000.00, 'Available', 25000, 'Hybrid', 'Automatic'),
('Tesla', 'Model 3', 2022, 45000.00, 'Available', 3000, 'Electric', 'Automatic'),
('Volkswagen', 'Passat', 2019, 19000.00, 'Sold', 22000, 'Petrol', 'Manual'),
('Mazda', '6', 2021, 24000.00, 'Available', 12000, 'Petrol', 'Automatic'),
('Subaru', 'Impreza', 2020, 21000.00, 'Available', 15000, 'Diesel', 'Manual'),
('Jeep', 'Cherokee', 2021, 32000.00, 'Available', 10000, 'Petrol', 'Automatic'),
('Ford', 'Explorer', 2020, 30000.00, 'Sold', 20000, 'Diesel', 'Automatic'),
('Chevrolet', 'Tahoe', 2019, 45000.00, 'Available', 25000, 'Petrol', 'Automatic'),
('Honda', 'Accord', 2022, 28000.00, 'Available', 5000, 'Hybrid', 'Automatic'),
('Hyundai', 'Santa Fe', 2020, 27000.00, 'Available', 15000, 'Diesel', 'Automatic'),
('Kia', 'Sorento', 2021, 29000.00, 'Available', 10000, 'Petrol', 'Manual');

-- Insert sample data into CUSTOMERS table
INSERT INTO CUSTOMERS (FirstName, LastName, Email, Address) VALUES
('John', 'Doe', 'john.doe@example.com', '123 Elm Street'),
('Jane', 'Smith', 'jane.smith@example.com', '456 Oak Avenue'),
('Alice', 'Brown', 'alice.brown@example.com', '789 Maple Lane'),
('Bob', 'Johnson', 'bob.johnson@example.com', '321 Pine Drive'),
('Charlie', 'Davis', 'charlie.davis@example.com', '654 Birch Blvd'),
('Diana', 'Evans', 'diana.evans@example.com', '987 Cedar Crescent'),
('Eve', 'Foster', 'eve.foster@example.com', '741 Spruce Terrace'),
('Frank', 'Green', 'frank.green@example.com', '852 Willow Street'),
('Grace', 'Harris', 'grace.harris@example.com', '963 Aspen Avenue'),
('Hank', 'Iverson', 'hank.iverson@example.com', '159 Oakwood Court'),
('Ivy', 'Jones', 'ivy.jones@example.com', '753 Pinehurst Circle'),
('Jack', 'King', 'jack.king@example.com', '864 Cypress Road'),
('Karen', 'Lewis', 'karen.lewis@example.com', '975 Redwood Way'),
('Liam', 'Miller', 'liam.miller@example.com', '147 Magnolia Place'),
('Mia', 'Nelson', 'mia.nelson@example.com', '258 Alder Park'),
('Noah', 'Owen', 'noah.owen@example.com', '369 Juniper Circle'),
('Olivia', 'Parker', 'olivia.parker@example.com', '741 Birchwood Drive'),
('Paul', 'Quincy', 'paul.quincy@example.com', '852 Aspen Hill'),
('Quinn', 'Roberts', 'quinn.roberts@example.com', '963 Willow Pond'),
('Rachel', 'Smith', 'rachel.smith@example.com', '159 Cedar Path');

select * from vehicles;
select * from customers;

