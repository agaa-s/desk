import sys

from PySide2 import QtWidgets
from PySide2.QtCore import Signal, Slot


class ShowMultiplesOfThree(QtWidgets.QWidget):
    multiplesOfThree = Signal(int)  # カスタムシグナルを定義

    ### この書き方は python2 らしい
    ###  <https://techacademy.jp/magazine/28283>
    # def __init__(self, parent=None):
    #     super(ShowMultiplesOfThree, self).__init__(parent)
    def __init__(self):
        super().__init__()

        # カスタムシグナルとカスタムスロットを結びつけて、3の倍数になったときにテキストを更新させる
        self.multiplesOfThree.connect(self.update_text)

        # レイアウト設定、スピンボックスとテキストを用意する
        layout = QtWidgets.QVBoxLayout()

        self.sp = QtWidgets.QSpinBox()
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.value_changed)  # 値の変化を検知する

        self.text = QtWidgets.QPlainTextEdit()
        layout.addWidget(self.text)

        self.setLayout(layout)

    def value_changed(self):
        self.text.clear()
        if int(self.sp.value()) % 3 == 0:
            self.multiplesOfThree.emit(int(self.sp.value()))  # 3の倍数の場合はカスタムシグナル発火

    @Slot(int)
    def update_text(self, sp_value):
        self.text.appendPlainText(f'value = {sp_value}')    # カスタムシグナルを受け付けたらテキストを更新


def main():
    app = QtWidgets.QApplication(sys.argv)

    widget = ShowMultiplesOfThree()
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
