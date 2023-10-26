data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

item_data = map(lambda items: [int(item) for item in items.split() if item.isdigit()], data)

for item in item_data:
    print(item)