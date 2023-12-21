import numpy as np


def snake(rows, cols):
    arr = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        a = np.arange(i * cols + 1, (i + 1) * cols + 1)
        arr[i] = a[::(-1) ** i]
    return arr

print(snake(4, 5))
