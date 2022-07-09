import numpy as np

a, b, d = map(int, input().split())
d = d * (np.pi / 180)

new = np.dot(
    np.array([[np.cos(d), -np.sin(d)], [np.sin(d), np.cos(d)]]), np.array([a, b])
)
print(new[0], new[1])
