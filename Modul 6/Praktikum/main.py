from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont

# TODO 1: Buka kedua gambar menggunakan Pillow.

bg = Image.open('C:/Users/davinky/Documents/codeshit/ProgFunc/Modul 6/Praktikum/images/bg.jpeg')
fg = Image.open('C:/Users/davinky/Documents/codeshit/ProgFunc/Modul 6/Praktikum/images/fg.jpeg')

# TODO 2: Ubah gambar background menjadi hitam-putih (grayscale), berotasi sebesar 30 derajat, dan blur
bgNew = bg.convert('L').rotate(30).filter(ImageFilter.BLUR)

# TODO 3: Ubah tingkat kecerahan gambar overlay menjadi 1.x kali lipat dan tingkat kontras menjadi 1.y kali lipat. Dimana nilai x dan y mengacu pada 2 digit NIM akhir kalian dan resize sesuai kebutuhan.
enhancer = ImageEnhance.Brightness(fg)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
fgNew = enhancer.enhance(1.6)

# TODO 4: Sisipkan gambar overlay ke dalam gambar background sehingga terlihat seperti stiker pada gambar latar belakang.
fgNew_hw = int(fgNew.width / 2)
fgNew_hh = int(fgNew.height / 2)
fgNew_new_size = (fgNew_hw, fgNew_hh)
fgNew = fgNew.resize(fgNew_new_size)

x_center = (bg.width - fgNew.width) // 2
y_center = (bg.height - fgNew.height) // 2

bgNew.paste(fgNew, (x_center, y_center))

# TODO 5: Tambahkan teks "Informatika JOSSS!" pada gambar overlay dengan font Arial dan ukuran 24.
draw = ImageDraw.Draw(bgNew)
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 24)
txt = "Informatika JOSSS!"

tbox = draw.textbbox((0, 0), txt, font)

t_width = tbox[2] - tbox[0]
t_height = tbox[3] - tbox[1]
txt_x = (bgNew.width - t_width) // 2
txt_y = (bgNew.height - t_height) // 2

draw.text((txt_x, txt_y), txt, font=font, fill=255)

# TODO 6: Simpan gambar hasil edit dengan nama "tugas_praktikum_enam.jpg".
bgNew.save('C:/Users/davinky/Documents/codeshit/ProgFunc/Modul 6/Praktikum/images/tugas_praktikum_enam.jpg')
bgNew.show()