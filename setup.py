import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from master import *
from edit import Mythread


class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.thread = Mythread()
        self.thread.sigout.connect(self.process)

    def get_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, "浏览", "../")
        if dir_path:
            self.lineEdit_1.setText(dir_path)

    def process(self, i, _list):
        self.pushBtn_3.setEnabled(False)
        self.pushBtn_3.setText("生成中...")
        value = ((i + 1) / len(_list)) * 100
        self.progressBar.setValue(value)
        if i == len(_list)-1:
            QMessageBox.information(self, "信息", "生成报告成功")
            self.pushBtn_3.setText("开      始")
            self.pushBtn_3.setEnabled(True)

    def get_xlsx(self):
        xlsx_path, _type = QFileDialog.getOpenFileName(self, "打开", "../", "Excel文件(*.xlsx)")
        if xlsx_path:
            self.lineEdit_2.setText(xlsx_path)

    def run(self):
        self.thread.file_path = self.lineEdit_1.text()
        self.thread.xlsx_path = self.lineEdit_2.text()
        self.thread.sn = self.lineEdit_3.text()

        if self.thread.file_path == "" or self.thread.xlsx_path == "" or self.thread.sn == "":
            QMessageBox.warning(self, "警告", "请填入完整信息")
        elif int(self.thread.sn) > 20 or int(self.thread.sn) <= 0:
            QMessageBox.warning(self, "警告", "样车数量异常（范围1~20）")
        else:
            try:
                self.thread.start()
            except Exception as e:
                QMessageBox.critical(self, "错误", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
