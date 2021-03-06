#!/usr/bin/env python
# coding: utf-8

# QMainWindow を使ってます。

import matplotlib
# matplotlib.rcParams['backend.qt5'] = 'PySide2'
# matplotlib.use('Qt5Agg')

import numpy as np
import matplotlib.pyplot as plt

## Original
##  <https://qiita.com/mountcedar/items/ccf671a497563b0cd671>
# from matplotlib.backends.backend_qt4agg \
#     import FigureCanvasQTAgg as FigureCanvas
# from PySide.QtGui import QApplication
# from PySide.QtGui import QMainWindow
# from PySide.QtCore import Qt

from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
# from PySide2.QtWidgets import QApplication
# from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Qt


class DraggableRectangle(object):
    def __init__(self, rect):
        self.rect = rect
        self.press = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        '''
        on button press we will see if the mouse is over us and store some data
        '''
        if event.inaxes != self.rect.axes:
            return

        contains, attrd = self.rect.contains(event)
        if not contains:
            return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None:
            return
        if event.inaxes != self.rect.axes:
            return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress

        self.rect.set_x(x0 + dx)
        self.rect.set_y(y0 + dy)

        self.rect.figure.canvas.draw()

    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


if __name__ == '__main__':
    import sys

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    # グラフを作成
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects = ax.bar(range(10), 20 * np.random.rand(10))

    canvas = FigureCanvas(fig)  # canvasはQtのwidgit
    canvas.setFocusPolicy(Qt.StrongFocus)
    canvas.setFocus()

    # # グラフの各バーをドラッガブルにする
    # #   canvas = FigureCanvas(fig) よりあとで実行すること
    # drs = []
    # for rect in rects:
    #     dr = DraggableRectangle(rect)
    #     dr.connect()  # 本来なら終了時に disconnectするのでしょうね
    #     drs.append(dr) # drの上書き防止

###    plt.show()


    # ラベル
    text = QLabel("drg_rect2.py")
    text.setAlignment(Qt.AlignCenter)

    # ボタン
    button = QPushButton("Click me!!!")

    # レイアウトを構成
    layout = QVBoxLayout()
    layout.addWidget(text)
    layout.addWidget(button)
    layout.addWidget(canvas)

    widget = QWidget()
    widget.setLayout(layout)
###    widget.show()

    window = QMainWindow()
###    window.setCentralWidget(canvas)
    window.setCentralWidget(widget)
    window.show()

    app.exec_()
