import numpy as np
import matplotlib.pyplot as plt

def torus_geodesic_length(R, r, theta1, theta2):
    phi1 = theta1 * 2 * np.pi
    phi2 = theta2 * 2 * np.pi
    cos_phi_diff = np.cos(phi1 - phi2)
    length = np.sqrt((R + r * cos_phi_diff)**2 + (r * np.sin(phi1 - phi2))**2)
    return length

# トーラスの主半径
R = 5

# トーラスの管の半径
r = 2

# 2点間を結ぶ角度パラメータ
theta1 = 0.25
theta2 = 0.75

# 測地線の長さを計算
length = torus_geodesic_length(R, r, theta1, theta2)

# トーラスのパラメータ
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# トーラスを描画
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 結果を出力
print("Geodesic length between theta1 and theta2:", length)

# トーラスの描画を表示
plt.show()
