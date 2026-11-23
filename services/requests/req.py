import requests
import time
import random

URL = "http://price-predict:8000/api/prediction"

for i in range(50):
    params = {"item_id": i}

    data ={
        "Car_Name": "swift",
        "Year": 2018,
        "Selling_type": "Dealer",
        "Present_Price": round(random.uniform(5.5, 8.0), 2),
        "Driven_kms": random.randint(38000, 68000),
        "Fuel_Type": "Petrol",
        "Transmission": "Manual",
        "Owner": 0,
        "Car_Age": 8
    }

    if random.random()<0.1:
        data.pop("Fuel_Type")
        print("Отправляем некорректный запрос")

    response = requests.post(URL, params=params, json=data, timeout=10)

    print(response.status_code)
    print(response.json())

    time.sleep(random.uniform(1, 5))