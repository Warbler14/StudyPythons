#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

plt.show()