import sys
from Model.AuthManager import AuthManager
from ui_login import Ui_MainWindow
from PySide2.QtWidgets import *
from register import Register


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submit_btn.clicked.connect(lambda: self.handle_login(
            self.ui.email_entry.text(), self.ui.pass_entry.text()))
        self.ui.registerTransfer.clicked.connect(lambda: self.push_register())

    def handle_login(self, email: str, password: str):
        authmanager = AuthManager()
        authmanager.login(email, password)

    def push_register(self):
        self.registerWindow = Register()
        self.registerWindow.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window1 = Login()
    window1.show()
    sys.exit(app.exec_())
