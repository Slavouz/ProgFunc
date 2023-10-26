data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def toMinute(w=0):
    def hari(d=0):
        def jam(h=0):
            def menit(m=0):                
                return (((w * 7)+d)*24+h)*60+m
            return menit
        return jam
    return hari

item_data = map(lambda items: [int(item) for item in items.split() if item.isdigit()], data)
converted_data = map(lambda item: toMinute(item[0])(item[1])(item[2])(item[3]), item_data)

print("OutputData =",  list(converted_data))