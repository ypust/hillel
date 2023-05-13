import json

with open('manager_sales.json', 'r') as file:
    data = json.load(file)

    max_sale_number = 0
    max_sale_manager_name = None

    for manager in data:
        manager_name = manager["manager"]["first_name"] + " " + manager["manager"]["last_name"]
        sale_number = 0
        for car in manager["cars"]:
            sale_number += car["price"]

        if sale_number > max_sale_number:
            max_sale_number = sale_number
            max_sale_manager_name = manager_name

    print(f"{max_sale_manager_name} {max_sale_number}")