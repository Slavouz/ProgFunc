random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
float_tupple = ()
str_list = []
int_dict = {}

for x in range(len(random_list)):
    if type(random_list[x]) is float:
        float_tupple += (random_list[x],)
    elif type(random_list[x]) is str:
        str_list.append(random_list[x])
    elif type(random_list[x]) is int:
        satuan = random_list[x] % 10
        puluhan = (random_list[x] // 10) % 10
        ratusan = random_list[x] // 100
        int_dict[x] = {"Ratusan": ratusan, "Puluhan": puluhan, "Satuan": satuan}

print("Float: ")

print(float_tupple)

print("String: ")

for y in range(len(str_list)):
    print(str_list[y])

print("Integer: ")

for k, v in int_dict.items():
    print(k, v)
