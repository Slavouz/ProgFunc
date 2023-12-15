import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm

tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10

# TODO 1: buat Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompok_tb(data, interval_size):
    hasil = {}
    for tb in data:
        interval_lower = (tb // interval_size) * interval_size
        interval = (interval_lower, interval_lower + interval_size)
        hasil[interval] = hasil.get(interval, 0) + 1
    return hasil

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
frekuensi_tb = kelompok_tb(tinggi_badan, interval_size)
intervals = list(frekuensi_tb.keys())

flat_intval = np.array(intervals).ravel()
sorted_intval = sorted(flat_intval)

# TODO 3: Visualiasi data dalam bentuk histogram
plt.hist(tinggi_badan, bins=sorted_intval, label='Data', color='blue')
plt.xlabel('Interval Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Frekuensi Tinggi Badan')

# TODO 4: Menambahkan kurva pdf pada hasil visualiasi data
tb_mean = np.mean(tinggi_badan)
tb_std = np.std(tinggi_badan)

xmin = np.min(tinggi_badan)
xmax = np.max(tinggi_badan)

x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, tb_mean, tb_std)

scale_factor = 0.5 / max(p)
p_scaled = p * scale_factor

plt.plot(x, p_scaled * len(tinggi_badan), label='PDF', color='red')
plt.legend()
plt.show()