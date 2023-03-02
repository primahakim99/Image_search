import cv2

# Meminta nama file gambar dari pengguna
# img1_path = input("Masukkan nama file gambar: ")

# Load gambar yang ingin dibandingkan
img1 = cv2.imread('images.jpg')
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Memasukkan daftar pembanding
daftar_pembanding = ['alphard.jpg', 'alphardhitam.jpg', 'duapalhard.jpg']

# Membuat list untuk menyimpan nilai similarity dari setiap pembanding
list_similarity = []

# Loop melalui daftar pembanding dan mencari similarity
for pembanding in daftar_pembanding:
    img2 = cv2.imread(pembanding)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_img1, gray_img2, cv2.TM_CCOEFF_NORMED)
    similarity = cv2.minMaxLoc(result)[1]
    list_similarity.append(similarity)
    print(f"Similarity dengan {pembanding}: {similarity}")

# Mencari nilai tertinggi dalam list similarity
max_similarity = max(list_similarity)
index_max_similarity = list_similarity.index(max_similarity)

# Menampilkan nilai similarity tertinggi dan nama pembanding
print(f"Most similar image is {daftar_pembanding[index_max_similarity]} : {max_similarity}")
