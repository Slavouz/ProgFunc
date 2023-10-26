random_list = [3.1, 105, 'Hello', 2.7, 737, 'Python', 5.5, 412, 'world', 'AI']

float_list = tuple(filter(lambda list: type(list) is float, random_list))

int_list = list(map(lambda list: {
    'ratusan': int(list / 100),
    'puluhan': int((list % 100) / 10),
    'satuan': int(((list % 100) % 10) / 1)
}, filter(lambda list: type(list) is int, random_list)))

str_list = list(filter(lambda list: type(list) is str, random_list))

print("Data Float :", tuple(float_list))
print("Data Int :", list(int_list))
print("Data String :", list(str_list))