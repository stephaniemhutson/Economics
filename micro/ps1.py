import matplotlib.pyplot as plt
import numpy as np

plt.subplot(221)
plt.plot([0, 1, 4],[4, 1, 0])
plt.ylabel("x_2 : x_1")
plt.xlabel("x_1 : x_2")
plt.title("Indifference Curve")
plt.grid(True)

plt.subplot(222)
plt.plot([0, 1, 4],[4, 1, 0])
plt.plot([0,2],[2,0])

plt.ylabel("x_2 : x_1")
plt.xlabel("x_1 : x_2")
plt.title("1/3 <p_1/p_2 < 3")
plt.grid(True)

plt.subplot(223)
plt.plot([0, 1, 4],[4, 1, 0])
plt.plot([0,4/3],[4,0])

plt.ylabel("x_2 : x_1")
plt.xlabel("x_1 : x_2")
plt.title("3p_2 = p_1")
plt.grid(True)

plt.subplot(224)
plt.plot([0, 1, 4],[4, 1, 0])
plt.plot([0,5/4],[5,0])

plt.ylabel("x_2 : x_1")
plt.xlabel("x_1 : x_2")
plt.title("3p_2 < p_1")
plt.grid(True)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
