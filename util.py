import h5py
import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def load_data(path):
    """
    Load data from h5py directory    :param path: path to h5py directory
    :return: x_train, x_val, x_test, y_train, y_val, y_test
    """
    with h5py.File(path, "r") as f:
        x_train = np.array(f.get('x_train'))
        x_val = np.array(f.get('x_val'))
        x_test = np.array(f.get('x_test'))
        y_train = np.array(f.get('y_train'))
        y_val = np.array(f.get('y_val'))
        y_test = np.array(f.get('y_test'))
    return x_train, x_val, x_test, y_train, y_val, y_test