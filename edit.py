import os

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal

from funs import *


class MyLindEdit(QLineEdit):
    def __init__(self, title, parent):
        super(MyLindEdit, self).__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        try:
            file_paths = e.mimeData().text()
            file_path = file_paths.split('\n')[0]
            path = file_path.replace('file:///', '', 1)
            self.setText(path)
        except Exception as f:
            print(str(f))


class Mythread(QThread):
    sigout = pyqtSignal(int, list)

    def __init__(self):
        super(Mythread, self).__init__()
        self.file_path = None
        self.xlsx_path = None
        self.sn = None

    def run(self):
        base_dir = os.path.dirname(self.file_path)
        save_path = os.path.join(base_dir, 'report')
        vehicle_info, tol_list = read_xls(self.xlsx_path, int(self.sn))
        _context = make_context(vehicle_info, tol_list)
        files = os.listdir(self.file_path)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        for file in files:
            template_file = os.path.join(self.file_path, file)
            dst_path = os.path.join(save_path, file)
            merge(template_file, _context, dst_path)
            i = files.index(file)
            self.sigout.emit(i, files)
