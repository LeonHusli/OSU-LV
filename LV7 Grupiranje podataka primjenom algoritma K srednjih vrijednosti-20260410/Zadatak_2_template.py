import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("LV7 Grupiranje podataka primjenom algoritma K srednjih vrijednosti-20260410/imgs/test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

#2.1
unique_colors = np.unique(img_array_aprox, axis=0)
print("Broj različitih boja:", len(unique_colors))

#2.2
km = KMeans(n_clusters=3, init="random", n_init=5, random_state=0)
km.fit(img_array)
labels = km.predict(img_array)
centroids = km.cluster_centers_

#2.3
img_array_aprox = centroids[labels]
img_aprox = img_array_aprox.reshape(w, h, d)

plt.imshow(img_aprox)
plt.show()

#2.4
for K in range(1,10):
    km = KMeans(n_clusters=K, init="random", n_init=5, random_state=0)
    km.fit(img_array)
    labels = km.predict(img_array)
    centroids = km.cluster_centers_

    img_array_aprox = centroids[labels]
    img_aprox = img_array_aprox.reshape(w, h, d)

    plt.subplot(3,3,K)
    plt.imshow(img_aprox)

plt.show()

#2.5
#isto sve samo mjenjamo datoteku

#2.6
inertia = []
K_range = range(1,10)

for K in K_range:
    km = KMeans(n_clusters=K, init="random", n_init=5, random_state=0)
    km.fit(img_array)
    inertia.append(km.inertia_)

plt.plot(K_range, inertia, marker=".")
plt.show()

#2.7
for k in range(1,10):
    cluster_img = (labels == k).reshape(w, h)

    plt.subplot(3,3, k)
    plt.imshow(cluster_img, cmap="gray")

plt.show()