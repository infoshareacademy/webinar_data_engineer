import csv
import random
from datetime import datetime, timedelta
from faker import Faker

# Inicjalizacja generatora Faker
fake = Faker()

# Lista metod płatności
payment_methods = ['Visa', 'Mastercard', 'American Express', 'PayPal', 'Cash']

# Generowanie danych
def generate_sales_data(num_rows):
    data = []
    for i in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        payment_method = random.choice(payment_methods)
        payment_date = (datetime.now() - timedelta(days=random.randint(1, 90))).strftime('%Y-%m-%d')
        amount = round(random.uniform(10.0, 1000.0), 2)
        data.append([i+1, first_name, last_name, payment_method, payment_date, amount])
    return data

# Zapis do pliku CSV
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'first_name', 'last_name', 'payment_method', 'payment_date', 'amount'])
        writer.writerows(data)

# Przykładowe użycie
filename = 'sales_data.csv'
num_rows = 1000
sales_data = generate_sales_data(num_rows)
write_to_csv(filename, sales_data)
print(f'Zapisano {num_rows} wierszy danych do pliku {filename}')