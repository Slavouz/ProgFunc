import matplotlib.pyplot as plt

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualiasi pertama
nama_produk = [produk[0] for produk in data_transaksi]
harga_produk = [produk[1] for produk in data_transaksi]
jumlah_terjual = [produk[2] for produk in data_transaksi]

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.subplot(1, 2, 1)
plt.scatter(harga_produk, jumlah_terjual)
plt.xlabel("Harga Produk")
plt.ylabel("Jumlah Terjual")
plt.title("Hubungan Harga Produk dan Jumlah Produk Terjual")

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan = [harga_produk[i] * jumlah_terjual[i] for i in range(len(harga_produk))]

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
plt.subplot(1, 2, 2)
plt.bar(nama_produk, pendapatan)
plt.xlabel("Produk")
plt.ylabel("Pendapatan")
plt.title("Pendapatan Produk")

plt.tight_layout()
plt.show()
