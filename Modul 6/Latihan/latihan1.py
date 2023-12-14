# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()'
gambarku = Image.open('C:/Users/davinky/Pictures/lighthouse.jpg')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert('L')

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 24)
text = "Bagas Satrya Yogatama - 202110370311256"

tbox = draw.textbbox((0, 0), text, font)

text_width = tbox[2] - tbox[0]
text_height = tbox[3] - tbox[1]
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2

draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('C:/Users/davinky/Pictures/newimage.jpg')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()