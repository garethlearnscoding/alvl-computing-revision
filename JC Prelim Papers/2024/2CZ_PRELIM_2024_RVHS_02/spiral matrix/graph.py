import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x / 5)

fig, ax1 = plt.subplots(figsize=(8, 5))

# First y-axis
ax1.plot(x, y1, color="tab:blue", label="sin(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Second y-axis
ax2 = ax1.twinx()
ax2.plot(x, y2, color="tab:red", label="cos(x)")
ax2.set_ylabel("cos(x)", color="tab:red")
ax2.tick_params(axis="y", labelcolor="tab:red")

# Third y-axis
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("outward", 60))  # Move third axis outward
ax3.plot(x, y3, color="tab:green", label="exp(x/5)")
ax3.set_ylabel("exp(x/5)", color="tab:green")
ax3.tick_params(axis="y", labelcolor="tab:green")

plt.tight_layout()
plt.show()