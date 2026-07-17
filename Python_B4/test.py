import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi,200)
y = np.sin(x)

""" fig, ax = plt.subplots(figsize=(6,3))
ax.plot(x,y)
ax.set_title("ve do thi bang huong doi tuong")
ax.set_xlabel("goc (rad)")
ax.set_ylabel("sin(x)")
plt.show() """

fig, axes = plt.subplots(2,3,figsize=(15,8))

#(1) line
axes[0,0].plot(x, np.sin(x), label="sin")
axes[0,0].plot(x, np.cos(x), label="cos")
axes[0,0].set_title("Line")

#(2) Scatter
rng = np.random.default_rng(42)
xs, ys = rng.random(80), rng.random(80)
sc = axes[0,1].scatter(xs,ys, c=xs+ys, s=ys*200, cmap="viridis", alpha=0.7)
axes[0,1].set_title("Scatter")
fig.colorbar(sc, ax=axes[0,1])

#(3) Bar
prod = ["A", "B", "C", "D"]
axes[0,2].bar(prod, [23,45,31,28], color="steelblue")
axes[0,2].set_title("Bar")

#(4) Histogram
axes[1,0].hist(rng.nomal(70,15,1000))



fig.suptitle("5 bieu do co ban", fontsize=15)
fig.tight_layout()
plt.show()
