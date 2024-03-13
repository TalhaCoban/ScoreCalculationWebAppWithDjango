import pandas as pd
import matplotlib.pyplot as plt
import os


data = pd.read_csv("ham2018.txt")
df = data.copy()

fig = plt.figure(figsize=(9,4))

plt.subplot(2,2,1)
plt.scatter(df["500"], df["1"])

plt.subplot(2,2,2)
plt.scatter(df["500"], df["5"])
plt.tight_layout()

plt.savefig("image.png")






