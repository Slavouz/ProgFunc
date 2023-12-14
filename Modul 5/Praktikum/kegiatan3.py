import matplotlib.pyplot as plt
import numpy as np

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10 # Misalnya interval ukuran per 10 sentimmeter

# TODO 1: buat Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompok_tb(tb, interval):
    hasil = []
    
    for i in range(int(min(tb)), int(max(tb)) + 1, interval):
        frekuensi = 0
        for tinggi in tinggi_badan:
            if i <= tinggi < i + interval:
                frekuensi += 1
        hasil.append((i, frekuensi))
    return hasil

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
hasil = kelompok_tb(tinggi_badan, interval_size)

# TODO 3: Visualiasi data dalam bentuk histogram
plt.hist(hasil, bins=len(hasil))
plt.title("Historgram Frekuensi Tinggi Badan")
plt.xlabel("Interval Tinggi Badan (cm)")
plt.ylabel("Frekuensi")
plt.show()

# TODO 4: Menambahkan kurva pdf pada hasil visualiasi data
avg = sum(tinggi_badan) / len(tinggi_badan)
std = np.std(tinggi_badan)

def pdf(x, avg, std):
    return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-(x - avg)**2 / (2 * std**2))

x = np.linspace(min(tinggi_badan), max(tinggi_badan), 1000)

plt.plot(x, pdf(x, avg, std))
plt.show()