import sys
from Model.AuthManager import AuthManager
from ui_register import Ui_MainWindow
from PySide2.QtWidgets import *
import login


class Register(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.register_btn.clicked.connect(lambda: self.handle_register(
            self.ui.username_entry.text(), self.ui.name_entry.text(),
            self.ui.email_entry.text(), self.ui.pass_entry.text()
        ))
        self.ui.loginTransfer.clicked.connect(self.push_login)

    def handle_register(self, username: str, name: str, email: str, password: str):
        authmanager = AuthManager()
        authmanager.register(username, name, email, password)

    def push_login(self):
        login_instance = login.Login()
        login_instance.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window1 = Register()
    window1.show()
    sys.exit(app.exec_())
