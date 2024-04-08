#install faker to generate random data 
pip install Faker

import csv
from faker import Faker
import os

fake = Faker()

# Define the number of entries for each table
num_entries = 20

# Ensure the output directory exists
output_dir = 'c:\\Users\\anjal\\Downloads'
os.makedirs(output_dir, exist_ok=True)

def write_csv(filename, headers, data):
    with open(os.path.join(output_dir, filename), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

# Generate data for Address table
address_data = [[i, fake.street_address(), fake.city(), fake.state_abbr(), fake.zipcode()] for i in range(1, num_entries + 1)]
write_csv('Address.csv', ['AddressID', 'Street', 'City', 'State', 'ZipCode'], address_data)

# Generate data for Patient table
patient_data = [[i, i, fake.first_name(), fake.last_name(), fake.email(), fake.phone_number(), fake.random_element(elements=[0, 1]), fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d")] for i in range(1, num_entries + 1)]
write_csv('Patient.csv', ['PatientID', 'AddressID', 'FirstName', 'LastName', 'Email', 'ContactNumber', 'PreviousPurchase', 'BirthDate'], patient_data)

# Generate data for Physician table
physician_data = [[i, fake.name(), fake.job(), fake.phone_number(), fake.company()] for i in range(1, num_entries + 1)]
write_csv('Physician.csv', ['PhysicianID', 'Name', 'Specialty', 'PhoneNumber', 'VisitingHospital'], physician_data)

# Generate data for Prescription table
prescription_data = [[i, fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.date(), fake.sentence(),fake.random_int(min=1, max=num_entries)] for i in range(1, num_entries + 1)]
write_csv('Prescription.csv', ['PrescriptionID', 'PatientID', 'PhysicianID', 'DateIssued', 'Dosage','MedicationItemID'], prescription_data)

# Generate data for MedicationItem table
medication_item_data = [[i, fake.catch_phrase(), fake.text(max_nb_chars=100), fake.text(max_nb_chars=50)] for i in range(1, num_entries + 1)]
write_csv('MedicationItem.csv', ['MedicationItemID', 'Name', 'Description', 'SideEffects'], medication_item_data)

# Generate data for Pharmacy table
pharmacy_data = [[i, fake.company(), fake.street_address(), fake.city(), fake.state_abbr(), fake.zipcode(), fake.phone_number()] for i in range(1, num_entries + 1)]
write_csv('Pharmacy.csv', ['PharmacyID', 'ShopName', 'ShopStreet', 'ShopCity', 'ShopState', 'ShopZipCode', 'PhoneNumber'], pharmacy_data)

# Generate data for Inventory table
inventory_data = [[i, fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.random_int(min=0, max=100)] for i in range(1, num_entries + 1)]
write_csv('Inventory.csv', ['InventoryID', 'PharmacyID', 'MedicationItemID', 'Quantity'], inventory_data)

# Generate data for Order table
order_data = [[i, fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.date_this_decade(), fake.date_this_decade(), fake.random_number(digits=5)] for i in range(1, num_entries + 1)]
write_csv('Order.csv', ['OrderID', 'PharmacyID', 'PrescriptionID', 'OrderDate', 'DeliveryDate', 'TotalPrice'], order_data)

# Additional tables such as OrderItem, DeliveryPerson, Delivery, Supplier, SupplyRecord, and Transactions
# should be generated following the same pattern, adjusting the fields and data types as necessary.

# Example for DeliveryPerson table
delivery_person_data = [[i, fake.first_name(), fake.last_name(), fake.email(), fake.phone_number()] for i in range(1, num_entries + 1)]
write_csv('DeliveryPerson.csv', ['DeliveryPersonID', 'FirstName', 'LastName', 'Email', 'ContactNumber'], delivery_person_data)

# Generate data for Delivery table
delivery_data = [[i, fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.date_this_decade(), fake.date_this_decade()] for i in range(1, num_entries + 1)]
write_csv('Delivery.csv', ['DeliveryID', 'OrderID', 'DeliveryPersonID', 'DeliveryDate', 'EstimatedDeliveryDate'], delivery_data)

# Generate data for Supplier table
supplier_data = [[i, fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(), fake.street_address(), fake.city(), fake.state_abbr(), fake.zipcode()] for i in range(1, num_entries + 1)]
write_csv('Supplier.csv', ['SupplierID', 'SupplierFirstName', 'SupplierLastName', 'ContactNumber', 'SupplierEmail', 'SupplierStreet', 'SupplierCity', 'SupplierState', 'SupplierZipCode'], supplier_data)

# Generate data for SupplyRecord table
supply_record_data = [[i, fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.date_this_decade(), fake.random_int(min=1, max=100)] for i in range(1, num_entries + 1)]
write_csv('SupplyRecord.csv', ['SupplyRecordID', 'SupplierID', 'PharmacyID', 'MedicationItemID', 'SupplyDate', 'QuantitySupplied'], supply_record_data)

# Generate data for Transactions table
transactions_data = [
    [
        i,
        i,
        #fake.random_int(min=1, max=num_entries),
        fake.pydecimal(left_digits=5, right_digits=2, positive=True),  # Adjusted to use pydecimal
        fake.date_this_decade(),
        fake.random_element(elements=['Credit Card', 'Debit Card', 'Cash'])
    ] for i in range(1, num_entries + 1)
]
write_csv('Transactions.csv', ['TransactionID', 'OrderID', 'Amount', 'TransactionDate', 'PaymentMethod'], transactions_data)
