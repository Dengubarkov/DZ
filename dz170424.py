import requests
import json
import csv
response = requests.get("https://jsonplaceholder.typicode.com/todos").json()

with open("dz170424.csv", 'w') as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=response[0].keys())
    writer.writeheader()
    for i in response:
        writer.writerow(i)