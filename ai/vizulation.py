import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label="sin(x)", linewidth=4)
plt.plot(x, np.cos(x), label="cos(x)", linestyle="dashed")
plt.title("Trigonometric Functions")
plt.xlabel("X")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()