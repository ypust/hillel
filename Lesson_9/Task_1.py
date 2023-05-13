import json
with open('group_people.json', 'r') as file:
    data = json.load(file)

    max_group_id = None
    max_female_count = 0

    for group in data:
        group_id = group["id_group"]
        female_count = 0

        for record in group["people"]:
            if record["gender"] == "Female" and record["year"] > 1977:
                female_count += 1

        if female_count > max_female_count:
            max_group_id = group_id
            max_female_count = female_count

    print(f'{max_group_id} {max_female_count}')
