import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas


from PySide2.QtWidgets import (QApplication, QDialog
                             , QVBoxLayout, QHBoxLayout, QLabel, QWidget
                             , QLineEdit, QPushButton
                             , QListWidget, QListWidgetItem)
from PySide2.QtCore import Slot, Qt


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

class MyForm(QDialog):

    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setWindowTitle("My Form")

        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")

        # Create layout and add widgets
        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    @Slot()
    def greetings(self):
        print ("Hello %s" % self.edit.text())

class MyWidget(QWidget):
    def __init__(self, parent=None, canvas=None):
        super(MyWidget, self).__init__(parent)

        ## 左
        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem("Item {}".format(i))
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        ## 右
        # 右上
        _placeholder = "This is a placeholder text"
        text_widget = QLabel(_placeholder)
        text_widget.setObjectName("title")

        # 右下
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        if canvas == None:
            content_layout.addWidget(text_widget)
        else :
            content_layout.addWidget(canvas)

        content_layout.addWidget(button)

        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        ## 全体を構成
        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)



def main():

    # Create the Qt Application
    app = QApplication(sys.argv)

    form = MyForm()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec_())

def setStyle(app):
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

def main1():

    # Create the Qt Application
    app = QApplication(sys.argv)

    w = QLabel("This is a placeholder text")
    w.resize(800, 600)
    w.setAlignment(Qt.AlignCenter)
    w.setStyleSheet("""
        background-color: #262626;
        background-color: red;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
        """)
    w.show()

    # Run the main Qt loop
    sys.exit(app.exec_())

def main2():
    # Create the Qt Application
    app = QApplication()

    w = MyWidget()
    w.resize(800, 600)
    w.show()

    # styleシートを適用
    setStyle(app)

    # Run the main Qt loop
    sys.exit(app.exec_())

def main3():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    fig = plt.figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    rects = ax.bar(range(10), 20 * np.random.rand(10))
    drs = []
    for rect in rects:
        dr = DraggableRectangle(rect)
        dr.connect()
        drs.append(dr)

    w = MyWidget(None, canvas)
    w.resize(800, 600)
    w.show()

    canvas.setFocusPolicy(Qt.StrongFocus)
    canvas.setFocus()

    # styleシートを適用
    setStyle(app)

    # Run the main Qt loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        main()
    elif sys.argv[1] == "1":
        main1()
    elif sys.argv[1] == "2":
        main2()
    else :
        main3()
