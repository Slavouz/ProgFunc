import math

def translasi(tx, ty):
    def transform(p):
        x, y = p
        return x + tx, y + ty
    return transform

def dilatasi(sx, sy):
    def transform(p):
        x, y = p
        return x * sx, y * sy
    return transform

def rotasi(sudut):    
    def transform(p):
        x, y = p
        new_x = x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut))
        new_y = x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
        return new_x, new_y
    return transform

point_P = (3, 5)

# Translasi
count_translasi = translasi(2, -1)
final_translasi = count_translasi(point_P)
print(f"Koordinat setelah translasi: " + str(final_translasi))

# Dilatasi
count_dilatasi = dilatasi(2, -1)
final_dilatasi = count_dilatasi(point_P)
print(f"Koordinat setelah dilatasi: " + str(final_dilatasi))

# Rotasi
count_rotasi = rotasi(30)
final_rotasi = count_rotasi(point_P)
print(f"Koordinat setelah rotasi: " + str(final_rotasi))