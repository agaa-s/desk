"""
2020-12-29現在
PiSide6 は、GLIBC_2.28 を必要とするため、本コードの実行はできない。
  ImportError: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.28' not found …

Ubuntu 18.04 glibc（GNU Cライブラリ）は、2.27。
  [確認]
  % /lib/x86_64-linux-gnu/libc.so.6

※下記コードは、PySide6 → Pyside2 で実行で可能となる。

------------------------------------------------------------
atom の python-debugger のファイルの切り替え方法。
Enter debugger commands here に 『e=test6.py』 を入力する。
------------------------------------------------------------
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec_())
