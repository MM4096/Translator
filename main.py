from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout, QGridLayout, \
    QLineEdit, QStackedWidget, QHBoxLayout

from enum import Enum

import sys
import pyrebase
from auth import Login, Register

firebaseConfig = {
    "apiKey": "AIzaSyDE6yjJa9JfNSasdkZ6qIGq62dEvDMTVSI",
    "authDomain": "test-4fad1.firebaseapp.com",
    "databaseURL": "https://test-4fad1-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "test-4fad1.appspot.com",
    "messagingSenderId": "579594052865",
    "appId": "1:579594052865:web:a9389d58d5fc5b5352a700"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

user = None

class LoginWindow(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Translator - Sign up")

        self.label = QLabel("Sign up")

        self.usernameInput = QLineEdit()
        self.usernameInput.setPlaceholderText("Enter your email")

        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Enter your password")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirmPasswordInput = QLineEdit()
        self.confirmPasswordInput.setPlaceholderText("Confirm your password")
        self.confirmPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.submitButton = QPushButton("Sign up")
        self.submitButton.clicked.connect(self.Login)

        self.switchButton = QPushButton("Already have an account? Sign in")
        self.switchButton.clicked.connect(self.Switch)

        layout = QGridLayout()

        layout.addWidget(self.label, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.usernameInput, 1, 1, 1, 2)
        layout.addWidget(self.passwordInput, 2, 1, 1, 2)
        layout.addWidget(self.confirmPasswordInput, 3, 1, 1, 2)
        layout.addWidget(self.switchButton, 4, 1, 1, 2)
        layout.addWidget(self.submitButton, 5, 1, 1, 2)

        self.confirmPasswordInput.hide()

        self.setLayout(layout)
        self.show()

    def Register(self):
        print("Hello world!")

    def Switch(self):
        pass


class RegisterWindow(QGridLayout):
    def __init__(self):

        super().__init__()

        self.label = QLabel("Sign up")

        self.usernameInput = QLineEdit()
        self.usernameInput.setPlaceholderText("Enter your email")

        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Enter your password")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirmPasswordInput = QLineEdit()
        self.confirmPasswordInput.setPlaceholderText("Confirm your password")
        self.confirmPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.submitButton = QPushButton("Sign up")
        self.submitButton.clicked.connect(self.Register())

        self.switchButton = QPushButton("Already have an account? Sign in")
        self.switchButton.clicked.connect(self.Switch)

        self.addWidget(self.label, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.usernameInput, 1, 1, 1, 2)
        self.addWidget(self.passwordInput, 2, 1, 1, 2)
        self.addWidget(self.confirmPasswordInput, 3, 1, 1, 2)
        self.addWidget(self.switchButton, 4, 1, 1, 2)
        self.addWidget(self.submitButton, 5, 1, 1, 2)

    def Register(self):
        print("Hello world!")

    def Switch(self):
        pass


class MainWindow(QGridLayout):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translator")

        label = QLabel("Translator")
        loginButton = QPushButton("Login")
        loginButton.clicked.connect(self.Login)
        registerButton = QPushButton("Register")
        registerButton.clicked.connect(self.Register)
        pricingButton = QPushButton("Pricing")
        pricingButton.clicked.connect(self.Pricing)

        self.addWidget(label, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(loginButton, 2, 1, 1, 1)
        self.addWidget(registerButton, 3, 1, 1, 1)
        self.addWidget(pricingButton, 4, 1, 1, 1)

    def Login(self):
        window.SetActiveWindow(WindowManager.Windows.LoginRegisterPage)

    def Register(self):
        print("Hello world!")

    def Pricing(self):
        print("Hello world!")


class WindowManager(QWidget):
    class Windows(Enum):
        MainPage = 0
        LoginRegisterPage = 1

    def __init__(self):
        super().__init__()
        self.LoginWindow = LoginWindow()
        self.MenuWindow = MainWindow()
        self.SetActiveWindow(self.Windows.MainPage)

    def SetActiveWindow(self, showWindow):
        if showWindow == self.Windows.MainPage:
            self.setLayout(self.MenuWindow)
        elif showWindow == self.Windows.LoginRegisterPage:
            self.setLayout(self.LoginRegisterWindow)


if __name__ == "__main__":
    # username = input("Enter your email: ")
    # password = input("Enter your password: ")
    #
    # user = Register(auth, username, password)
    app = QApplication(sys.argv)

    window = QWidget()
    window.setLayout(WindowManager())
    window.setGeometry(300, 300, 800, 600)
    window.show()

    app.exec()
