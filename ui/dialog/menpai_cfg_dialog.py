import os
from configparser import ConfigParser

from PyQt6.QtWidgets import QDialog

from ..win.menpai_config import Ui_dialog


class MenpaiCfgDialog(QDialog, Ui_dialog):
    def __init__(self):
        super(MenpaiCfgDialog, self).__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.save)
        self.file_path = os.path.join(os.path.abspath('.'), r'resources\menpai\menpai.ini')
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("文件不存在")
        self.conn = ConfigParser()
        self.conn.read(self.file_path)

        self.chasepos = float(self.conn.get('main', 'chasepos'))

        self.lineEdit.setText(str(self.chasepos))

    def save(self):
        self.conn.set('main', 'chasepos', self.lineEdit.text())
        self.conn.write(open(self.file_path, 'w'))
        self.close()
