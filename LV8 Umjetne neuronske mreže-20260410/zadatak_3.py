import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2

# učitavanje modela
model = tf.keras.models.load_model("LV8 Umjetne neuronske mreže-20260410/NNmodel.keras")

# učitavanje slike
img = cv2.imread("test.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_resized = cv2.resize(img_gray, (28,28))

plt.imshow(img_resized, cmap="gray")
plt.show()

img_resized = img_resized.astype("float32") / 255.0
img_resized = np.expand_dims(img_resized, axis=-1)  # (28,28,1)
img_resized = np.expand_dims(img_resized, axis=0)   # (1,28,28,1)

# predikcija modela
prediction = model.predict(img_resized)
print("Predikcija modela:", np.argmax(prediction))