import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6), facecolor="lightyellow")

# верхняя дуга зонта: y = -1/18 x² + 12, x ∈ [-12, 12]
x1 = np.linspace(-12, 12, 400)
y1 = -1/18 * x1**2 + 12
plt.plot(x1, y1, 'b-', label='Купол')

# левая часть: y = -1/8 x² + 6, x ∈ [-4, 4]
x2 = np.linspace(-4, 4, 400)
y2 = -1/8 * x2**2 + 6
plt.plot(x2, y2, 'g--')

# левая внутренняя дуга: y = 1/8 (x + 8)² + 6, x ∈ [-12, -4]
x3 = np.linspace(-12, -4, 400)
y3 = 1/8 * (x3 + 8)**2 + 6
plt.plot(x3, y3, 'm:')

# правая внутренняя дуга: y = 1/8 (x - 8)² + 6, x ∈ [4, 12]
x4 = np.linspace(4, 12, 400)
y4 = 1/8 * (x4 - 8)**2 + 6
plt.plot(x4, y4, 'm:')

# левая ручка: y = 2(x + 3) - 9, x ∈ [-4, -0.3]
x5 = np.linspace(-4, -0.3, 400)
y5 = 2 * (x5 + 3) - 9
plt.plot(x5, y5, 'r-.', marker='x', markersize=4)

# правая ручка: y = 1.5(x + 3)³ - 10, x ∈ [-4, 0.2]
x6 = np.linspace(-4, 0.2, 400)
y6 = 1.5 * (x6 + 3)**3 - 10
plt.plot(x6, y6, 'k-', marker='*', markersize=4)

plt.title("Vihmavari (Зонтик)", fontsize=14)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

