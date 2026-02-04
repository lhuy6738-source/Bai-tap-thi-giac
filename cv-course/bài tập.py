import numpy as np
import matplotlib.pyplot as plt

roman_numbers = [
    "XII", "I", "II", "III", "IV", "V",
    "VI", "VII", "VIII", "IX", "X", "XI"
]

fig, ax = plt.subplots()

# Vẽ vòng tròn
circle = plt.Circle((0, 0), 1, fill=False)
ax.add_artist(circle)

# Vẽ số La Mã
for i, roman in enumerate(roman_numbers):
    angle = np.pi/2 - i * (2 * np.pi / 12)
    x = 0.85 * np.cos(angle)
    y = 0.85 * np.sin(angle)
    ax.text(
        x, y, roman,
        ha='center', va='center',
        fontsize=14, fontweight='bold'
    )

# Kim phút
minute_angle = np.pi / 6
ax.plot([0, 0.7*np.cos(minute_angle)],
        [0, 0.7*np.sin(minute_angle)], linewidth=2)

# Kim giờ
hour_angle = np.pi / 3
ax.plot([0, 0.5*np.cos(hour_angle)],
        [0, 0.5*np.sin(hour_angle)], linewidth=4)

# 🔴 QUAN TRỌNG: set khung nhìn
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

ax.set_aspect('equal')
ax.axis('off')

plt.title("Dong ho so La Ma")
plt.show()