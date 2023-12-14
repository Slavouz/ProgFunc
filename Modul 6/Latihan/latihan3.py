from PIL import Image, ImageEnhance

# TODO 1: Buka gambar menggunakan Pillow.
image = Image.open('C:/Users/davinky/Pictures/lighthouse.jpg')

# TODO 2: Ubah tingkat kecerahan menjadi 1.5 kali lipat dan tingkat kontras menjadi 1.2 kali lipat.
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit dengan nama "brightness_contrast_image.jpg".
final_image.save('C:/Users/davinky/Pictures/brightness_contrast_image.jpg')

# TODO 4: Tampilkan hasilnya
final_image.show()