import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# task A
plt.figure()
plt.scatter(X_train[:,0], X_train[:,1], c=y_train, cmap="bwr", marker=".", label="train")
plt.scatter(X_test[:,0], X_test[:,1], c=y_test, cmap="bwr", marker="x", label="test")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

# task B
model = LogisticRegression()
model.fit(X_train, y_train)

# task C
theta0 = model.intercept_
theta1 = model.coef_[0][0]
theta2 = model.coef_[0][1]

plt.scatter(X_train[:,0], X_train[:,1], c=y_train, cmap="bwr", marker=".", label="train")
x1 = np.linspace(X_train[:, 0].min(), X_train[:, 0].max(), 100)
x2 = -(theta0 + theta1 * x1) / theta2
plt.plot(x1, x2, color="black", label="decision boundary")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

# task D
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm)
disp.plot(cmap="Blues")
plt.show()

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Točnost (accuracy):", accuracy)
print("Preciznost (precision):", precision)
print("Odziv (recall):", recall)

# task E
correct = y_test == y_pred
incorrect = y_test != y_pred

plt.figure()
plt.scatter(X_test[correct, 0], X_test[correct, 1], color='green', marker='.', label='correct')
plt.scatter(X_test[incorrect, 0], X_test[incorrect, 1], color='black', marker='x', label='incorrect')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show()