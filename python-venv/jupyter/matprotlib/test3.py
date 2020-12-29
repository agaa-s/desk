import matplotlib.pyplot as plt
fig = plt.figure(figsize=(6, 4), dpi=72, facecolor='skyblue', linewidth=10, edgecolor='green')
ax = fig.add_subplot(111)

###plt.show()
fig.savefig('1-1_a.png', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())
### atomでdebugする場合は、atomの起動ディレクトリに作成される。
