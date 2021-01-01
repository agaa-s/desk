import sys
from PySide2.QtWidgets import (QApplication, QDialog
                             , QVBoxLayout, QHBoxLayout, QLabel, QWidget
                             , QLineEdit, QPushButton
                             , QListWidget, QListWidgetItem)
from PySide2.QtCore import Slot, Qt

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
    def __init__(self, parent=None):
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
        content_layout.addWidget(text_widget)
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

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    # Run the main Qt loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        main()
    elif sys.argv[1] == "1":
        main1()
    else:
        main2()
