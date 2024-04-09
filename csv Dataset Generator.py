#Esure you have instaled the "Faker" python library to generate random data . Command --pip install Faker
#python code starts here
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
patient_data = [[i, i, fake.first_name(), fake.last_name(), fake.email(), fake.numerify(text="##########"), fake.random_element(elements=[0, 1]), fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d")] for i in range(1, num_entries + 1)]
write_csv('Patient.csv', ['PatientID', 'AddressID', 'FirstName', 'LastName', 'Email', 'ContactNumber', 'PreviousPurchase', 'BirthDate'], patient_data)

# Generate data for Physician table
physician_data = [[i, fake.name(), fake.job(), fake.numerify(text="##########"), fake.company()] for i in range(1, num_entries + 1)]
write_csv('Physician.csv', ['PhysicianID', 'Name', 'Specialty', 'PhoneNumber', 'VisitingHospital'], physician_data)

# Generate data for Prescription table
prescription_data = [
    [
        i, 
        fake.random_int(min=1, max=num_entries), 
        fake.random_int(min=1, max=num_entries), 
        fake.date_object().strftime("%Y-%m-%d"),  # Ensure date is in YYYY-MM-DD format
        fake.sentence(), 
        fake.random_int(min=1, max=num_entries)
    ] for i in range(1, num_entries + 1)
]
write_csv('Prescription.csv', ['PrescriptionID', 'PatientID', 'PhysicianID', 'DateIssued', 'Dosage', 'MedicationItemID'], prescription_data)

# Generate data for MedicationItem table
medication_item_data = [[i, fake.catch_phrase(), fake.text(max_nb_chars=100), fake.text(max_nb_chars=50)] for i in range(1, num_entries + 1)]
write_csv('MedicationItem.csv', ['MedicationItemID', 'Name', 'Description', 'SideEffects'], medication_item_data)

# Generate data for Pharmacy table
pharmacy_data = [[i, fake.company(), fake.street_address(), fake.city(), fake.state_abbr(), fake.zipcode(), fake.numerify(text="##########")] for i in range(1, num_entries + 1)]
write_csv('Pharmacy.csv', ['PharmacyID', 'ShopName', 'ShopStreet', 'ShopCity', 'ShopState', 'ShopZipCode', 'PhoneNumber'], pharmacy_data)

# Generate data for Inventory table
inventory_data = [[i, fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.random_int(min=0, max=100)] for i in range(1, num_entries + 1)]
write_csv('Inventory.csv', ['InventoryID', 'PharmacyID', 'MedicationItemID', 'Quantity'], inventory_data)

# Generate data for Order table
order_data = [[i, fake.random_int(min=1, max=num_entries), fake.random_int(min=1, max=num_entries), fake.date_this_decade().strftime("%Y-%m-%d"), fake.date_this_decade().strftime("%Y-%m-%d"), fake.random_number(digits=5)] for i in range(1, num_entries + 1)]
write_csv('Order.csv', ['OrderID', 'PharmacyID', 'PrescriptionID', 'OrderDate', 'DeliveryDate', 'TotalPrice'], order_data)

order_item_data = [
    [
        i,  # OrderItemID
        fake.random_int(min=1, max=num_entries),  # OrderID
        fake.random_int(min=1, max=num_entries),  # MedicationItemID
        fake.random_int(min=1, max=num_entries),  # DeliveryID
        fake.random_int(min=1, max=20), 
                fake.random_int(min=1, max=20),  # OrderQuantity
        fake.sentence(nb_words=6)  # Dosage, a random sentence as a placeholder for dosage instructions
    ] for i in range(1, num_entries + 1)
]

write_csv('OrderItem.csv', ['OrderItemID', 'OrderID', 'MedicationItemID', 'DeliveryID', 'OrderQuantity', 'Dosage'], order_item_data)

# Example for DeliveryPerson table
delivery_person_data = [[i, fake.first_name(), fake.last_name(), fake.email(), fake.numerify(text="##########")] for i in range(1, num_entries + 1)]
write_csv('DeliveryPerson.csv', ['DeliveryPersonID', 'FirstName', 'LastName', 'Email', 'ContactNumber'], delivery_person_data)

# Generate data for Delivery table
delivery_data = [
    [
        i, 
        fake.random_int(min=1, max=num_entries), 
        fake.random_int(min=1, max=num_entries), 
        fake.date_this_decade().strftime("%Y-%m-%d"), 
        fake.date_this_decade().strftime("%Y-%m-%d")
    ] for i in range(1, num_entries + 1)
]
write_csv('Delivery.csv', ['DeliveryID', 'OrderID', 'DeliveryPersonID', 'DeliveryDate', 'EstimatedDeliveryDate'], delivery_data)

# Generate data for Supplier table
supplier_data = [
    [
        i, 
        fake.first_name(), 
        fake.last_name(), 
        fake.numerify(text="##########"), 
        fake.email(), 
        fake.street_address(), 
        fake.city(), 
        fake.state_abbr(), 
        fake.zipcode()
    ] for i in range(1, num_entries + 1)
]
write_csv('Supplier.csv', ['SupplierID', 'SupplierFirstName', 'SupplierLastName', 'ContactNumber', 'SupplierEmail', 'SupplierStreet', 'SupplierCity', 'SupplierState', 'SupplierZipCode'], supplier_data)

# Generate data for SupplyRecord table
supply_record_data = [
    [
        i, 
        fake.random_int(min=1, max=num_entries), 
        fake.random_int(min=1, max=num_entries), 
        fake.random_int(min=1, max=num_entries), 
        fake.date_this_decade().strftime("%Y-%m-%d"), 
        fake.random_int(min=1, max=100)
    ] for i in range(1, num_entries + 1)
]
write_csv('SupplyRecord.csv', ['SupplyRecordID', 'SupplierID', 'PharmacyID', 'MedicationItemID', 'SupplyDate', 'QuantitySupplied'], supply_record_data)

# Generate data for Transactions table
transactions_data = [
    [
        i,
        i,  # Assuming TransactionID and OrderID are the same for simplicity
        fake.pydecimal(left_digits=5, right_digits=2, positive=True),  # Adjusted to use pydecimal
        fake.date_this_decade().strftime("%Y-%m-%d"),
        fake.random_element(elements=['Credit Card', 'Debit Card', 'Cash'])
    ] for i in range(1, num_entries + 1)
]
write_csv('Transactions.csv', ['TransactionID', 'OrderID', 'Amount', 'TransactionDate', 'PaymentMethod'], transactions_data)
