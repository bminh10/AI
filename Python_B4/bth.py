import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["savefig.dpi"] = 300
Path("figures").mkdir(exist_ok=True)
# Datasets tai offline qua seaborn
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
penguins = sns.load_dataset("penguins").dropna()
print("San sang:", [d.shape for d in (tips, iris, titanic, penguins)])

x = np.linspace(0, 2*np.pi, 200)
""" # Cach 1 - pyplot
plt.figure(figsize=(6, 3))
plt.plot(x, np.sin(x))
plt.title("pyplot")
plt.show()
# Cach 2 - huong doi tuong (OO): dung tu day ve sau
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, np.sin(x))
ax.set_title("object-oriented")
# TODO: dat nhan truc x = "goc (rad)", y = "sin(x)" bang ax.set_xlabel / ax.set_ylabel
plt.show() """

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
# (1) Line
axes[0,0].plot(x, np.sin(x), label="sin")
axes[0,0].plot(x, np.cos(x), "--", label="cos") # TODO: them legend
axes[0,0].set_title("Line")
# (2) Scatter (mau + kich thuoc theo gia tri)
rng = np.random.default_rng(42)
xs, ys = rng.random(80), rng.random(80)
sc = axes[0,1].scatter(xs, ys, c=xs+ys, s=ys*200, cmap="viridis", alpha=0.7)
axes[0,1].set_title("Scatter")
fig.colorbar(sc, ax=axes[0,1])
# (3) Bar
prod = ["A", "B", "C", "D"]
axes[0,2].bar(prod, [23, 45, 31, 38], color="steelblue")
axes[0,2].set_title("Bar")

# (4) Histogram
axes[1,0].hist(rng.normal(70, 15, 1000), bins=30, edgecolor="black")
axes[1,0].set_title("Histogram")
# TODO (5): Pie chart tren axes[1,1] cho ty le [40, 35, 25], labels=["X","Y","Z"],
# autopct="%1.0f%%". Dat title "Pie".
# ____
size = [40,35,25]
axes[1,1].pie(size, labels=["X","Y","Z"], startangle=90)
axes[1,1].set_title("Pie")


axes[1,2].axis("off") # o trong
fig.suptitle("Nam bieu do co ban", fontsize=15)
fig.tight_layout()
plt.show()