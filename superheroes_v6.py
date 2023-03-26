hero_0 = {
    "name": "Materdon",
    "power": "flight",
    "strength": 5,
    "speed": 12
}

hero_1 = {
    "name": "Orasy",
    "power": "x-ray vision",
    "strength": 2,
    "speed": 8
}

hero_list = [hero_1, hero_0]

for i in hero_list:
    print(f"{i['name']}'s superpower is {i['power']} and their strength value "
          f"is {i['strength']}")
