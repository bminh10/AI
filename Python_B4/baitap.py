import numpy as np, pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
penguins = sns.load_dataset("penguins").dropna()

x = np.linspace(-5, 5, 100)
y1 = x**2
y2 = x**3

fig, ax = plt.subplots(figsize=(5,5))
ax.plot(x,y1, label="y = x^2")
ax.plot(x,y2, label="y = x^3")
ax.set_title("ve do thi bang huong doi tuong")
ax.set_xlabel("goc (rad)")
ax.set_ylabel("sin(x)")
ax.grid(True)
ax.legend()
plt.show()


fig, axes = plt.subplots(2, 3, figsize=(15, 8))
rng = np.random.default_rng(42)
xs, ys = rng.random(80), rng.random(80)
sc = axes[0,1].scatter(xs,ys, c=xs+ys, s=ys*200, cmap="viridis", alpha=0.7)
axes[0,1].set_title("Scatter")
fig.colorbar(sc, ax=axes[0,1])

""" plt.plot(x, y, label='$y = x^2$', color='blue', linewidth=2)

# 4. Add titles, labels, and styling
plt.title('Quadratic Function Chart ($x^2$)')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.legend() """