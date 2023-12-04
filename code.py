import numpy as np
from pyquaternion import Quaternion
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建一个三维向量
v = np.array([1, 0, 0])

# 创建一个旋转轴
axis = np.array([0, 0.71, 0.71])

# 设定一个旋转角度（弧度）
angle = np.pi / 9

# 创建一个四元数
q = Quaternion(axis=axis, angle=angle)

# 创建一个3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制原始向量
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='b')

# 创建一个角度序列
angles = np.linspace(0, 2*np.pi, 100)

# 对每个角度进行旋转
for angle in angles:
    q = Quaternion(axis=axis, angle=angle)
    v_rot = q.rotate(v)
    ax.quiver(0, 0, 0, v_rot[0], v_rot[1], v_rot[2], color='r', alpha=0.1)

# 设置图形的比例
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# 显示图形
plt.show()
