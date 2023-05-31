import numpy as np

# Matriks transformasi pemindahan
def translate(dx, dy):
    return np.array([[1, 0, dx],
                    [0, 1, dy],
                    [0, 0, 1]])

# Matriks transformasi rotasi
def rotate(angle):
    cos_theta = np.cos(np.radians(angle))
    sin_theta = np.sin(np.radians(angle))
    return np.array([[cos_theta, -sin_theta, 0],
                    [sin_theta, cos_theta, 0],
                    [0, 0, 1]])

# Matriks transformasi skalasi
def scale(sx, sy):
    return np.array([[sx, 0, 0],
                    [0, sy, 0],
                    [0, 0, 1]])

# Titik awal
point = np.array([1, 1, 1])

# Transformasi pemindahan
translation_matrix = translate(2, 3)
translated_point = np.dot(translation_matrix, point)
print("Hasil pemindahan:", translated_point)

# Transformasi rotasi
rotation_matrix = rotate(45)
rotated_point = np.dot(rotation_matrix, point)
print("Hasil rotasi:", rotated_point)

# Transformasi skalasi
scale_matrix = scale(2, 2)
scaled_point = np.dot(scale_matrix, point)
print("Hasil skalasi:", scaled_point)