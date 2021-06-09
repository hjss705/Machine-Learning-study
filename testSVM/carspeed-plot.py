import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv('speed.csv', index_col=2)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["BMW"],b['KIA'], c=color, label=lbl)

scatter('느림', 'red')
scatter('보통', 'yellow')
scatter('빠름', 'black')

ax.legend()
plt.savefig('speed-test.png')