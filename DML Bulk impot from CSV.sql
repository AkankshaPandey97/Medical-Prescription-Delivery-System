/* ****Note:-All the table ingestion is through bulk insert . The zip file "DMDD csv DATA Files" has all the required Zip files.
			 The queries have file path as per the system. Please update the filepath before running the bulk insert code */


USE PharmacyDBDemo1;
GO

-- Import data into Address table
BULK INSERT Address
FROM 'C:\Users\anjal\Downloads\DATA\Address.csv'
WITH (
    FIELDTERMINATOR = ',',  -- CSV field delimiter
    ROWTERMINATOR = '\n',   -- CSV row delimiter
    FIRSTROW = 2            -- If the first row is column headers
);
GO
Select * from Address
go

-- Import data into Patient table
BULK INSERT Patient
FROM 'C:\Users\anjal\Downloads\DATA\Patient.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from Patient-- some rows have  issues for dob

-- Import data into Physician table
BULK INSERT Physician
FROM 'C:\Users\anjal\Downloads\DATA\Physician.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
	--FORMATFILE = 'C:\Users\anjal\Downloads\PatientFormat.fmt'
    FIRSTROW = 2
	
);
GO
Select * from Physician
go
-- Import data into Prescription table
BULK INSERT Prescription
FROM 'C:\Users\anjal\Downloads\DATA\Prescription.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from Prescription
go
-- Import data into MedicationItem table
BULK INSERT MedicationItem
FROM 'C:\Users\anjal\Downloads\DATA\MedicationItem.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
select* from MedicationItem
-- Import data into Pharmacy table
BULK INSERT Pharmacy
FROM 'C:\Users\anjal\Downloads\DATA\Pharmacy.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
select* from pharmacy

-- Import data into Inventory table
BULK INSERT Inventory
FROM 'C:\Users\anjal\Downloads\DATA\Inventory.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from Inventory
go
-- Import data into Order table
BULK INSERT [Order]
FROM 'C:\Users\anjal\Downloads\DATA\Order.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from [Order]
go


-- Import data into OrderItem table
BULK INSERT OrderItem
FROM 'C:\Users\anjal\Downloads\DATA\OrderItem.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from OrderItem
go
-- Import data into DeliveryPerson table
BULK INSERT DeliveryPerson
FROM 'C:\Users\anjal\Downloads\DATA\DeliveryPerson.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from DeliveryPerson
go
-- Import data into Delivery table
BULK INSERT Delivery
FROM 'C:\Users\anjal\Downloads\DATA\Delivery.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from Delivery
go

-- Import data into Supplier table
BULK INSERT Supplier
FROM 'C:\Users\anjal\Downloads\DATA\Supplier.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
select * from Supplier
-- Import data into SupplyRecord table
BULK INSERT SupplyRecord
FROM 'C:\Users\anjal\Downloads\DATA\SupplyRecord.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
select * from SupplyRecord

-- Import data into Transactions table
BULK INSERT Transactions
FROM 'C:\Users\anjal\Downloads\DATA\Transactions.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO
Select * from Transactions
go