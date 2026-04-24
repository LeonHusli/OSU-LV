import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# train i test podaci
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

# ucitavanje modela
model = tf.keras.models.load_model("LV8 Umjetne neuronske mreže-20260410/NNmodel.keras")

y_pred_s = model.predict(x_test_s)
y_pred_s_classes = np.argmax(y_pred_s, axis=1)

wrong_idx = np.where(y_pred_s_classes != y_test)[0]

plt.figure(figsize=(8,8))
for i in range(0,9):
    plt.subplot(3,3,i+1)
    plt.imshow(x_test[wrong_idx[i]], cmap="gray")
    plt.title(f"True: {y_test[wrong_idx[i]]} | Predicted: {y_pred_s_classes[wrong_idx[i]]}")
    plt.axis(False)
plt.show()