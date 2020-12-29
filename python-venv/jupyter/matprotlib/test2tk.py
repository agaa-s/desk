"""
TKにmatpolotlibのグラフを表示する
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# importエラーになる（調査未 2020-12-30・・・とりあえず書き方の控えとして。）
import tkinter as tk

# 終了処理
def Quit():
    root.quit()
    root.destroy()

# Prepare Data
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
x2 = np.linspace(0.0, 3.0)
y2 = np.cos(2 * np.pi * x2) * np.exp(-x1)

# Figure instance
fig = plt.Figure()

# ax1
ax1 = fig.add_subplot(221)
ax1.plot(x1, y1)
ax1.set_title('line plot')
ax1.set_ylabel('Damped oscillation')

# ax2
ax2 = fig.add_subplot(222)
ax2.scatter(x1, y1, marker='o')
ax2.set_title('Scatter plot')

# ax3
ax3 = fig.add_subplot(223)
ax3.plot(x2, y2)
ax3.set_ylabel('Damped oscillation')
ax3.set_xlabel('time (s)')

# ax4
ax4 = fig.add_subplot(224)
ax4.scatter(x2, y2, marker='o')
ax4.set_xlabel('time (s)')


# When windows is closed.

def _destroyWindow():
    root.quit()
    root.destroy()


# Tkinter Class

root = tk.Tk()
root.title(u"テストその１") #GUIのタイトル名の決定
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)  # When you close the tkinter window.

# Canvas
canvas = FigureCanvasTkAgg(fig, master=root)  # Generate canvas instance, Embedding fig in root
canvas.draw()
####canvas._tkcanvas.pack()
###canvas.get_tk_widget().pack()
canvas.get_tk_widget().grid(row = 0, column = 0, rowspan = 10)

##########
# EditBox
FileEditBox = tk.Entry(width = 15)
FileEditBox.grid(row = 1, column = 1)

# QUITボタン
ButtonWidth = 15
QuitButton = tk.Button(text = "QUIT", width = ButtonWidth, command = Quit) #QUITボタンオブジェクト生成
QuitButton.grid(row = 4, column = 1, columnspan = 1) #Quitボタン位置設定
##########

# root
root.update()
root.deiconify()
root.mainloop()
