import matplotlib.pyplot as plt
from functools import reduce

# Data nilai - nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# TODO 1: Menghitung rata-rata menggunakan fungsi reduce
avg_nilai = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

# TODO 2: Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lambda)
data_mahasiswa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pointX = list(map(lambda i: data_mahasiswa[i], range(len(data_mahasiswa))))

# TODO 3: Visualisasi data dalam bentuk diagram batang
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.bar(pointX, nilai_mahasiswa)
plt.plot([0, len(nilai_mahasiswa) + 1], [avg_nilai, avg_nilai], linestyle='--', color='red', label='Rata-rata = {:.2f}'.format(avg_nilai))
plt.legend()
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.xlim([0, len(nilai_mahasiswa) + 1])
plt.show()