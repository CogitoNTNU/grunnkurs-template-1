from util import load_data, alphabet
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier

x_train, x_val, x_test, y_train, y_val, y_test = load_data('dataset.h5')
