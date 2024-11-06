import json
import random
from datetime import datetime, timedelta
from faker import Faker

# Inicjalizacja generatora Faker
fake = Faker()

# Lista metod płatności
payment_methods = ['Visa', 'MasterCard', 'Wallet', 'Apple Pay', 'Google Pay']

# Generowanie danych
def generate_sales_data(num_rows):
    data = []
    for i in range(num_rows):
        user_name = fake.user_name()
        payment_method = random.choice(payment_methods)
        payment_date = (datetime.now() - timedelta(days=random.randint(1, 90))).strftime('%Y-%m-%d')
        amount = round(random.uniform(10.0, 1000.0), 2)
        data.append({
            "id": i+1,
            "user_name": user_name,
            "payment_method": payment_method,
            "payment_date": payment_date,
            "amount": amount
        })
    return data

# Zapis do pliku JSON
def write_to_json(filename, data):
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Przykładowe użycie
filename = 'sales_data.json'
num_rows = 1000
sales_data = generate_sales_data(num_rows)
write_to_json(filename, sales_data)
print(f'Zapisano {num_rows} wierszy danych do pliku {filename}')