from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout, QGridLayout, \
    QLineEdit, QStackedWidget, QHBoxLayout, QFrame

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


class LoginWindow(QGridLayout):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Sign in")

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

        self.switchButton = QPushButton("Don't have an account? Sign up")
        self.switchButton.clicked.connect(self.Switch)

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(self.Back)

        self.addWidget(self.label, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.usernameInput, 1, 1, 1, 2)
        self.addWidget(self.passwordInput, 2, 1, 1, 2)
        self.addWidget(self.switchButton, 4, 1, 1, 2)
        self.addWidget(self.submitButton, 5, 1, 1, 2)
        self.addWidget(self.backButton, 6, 1, 1, 2)

    def Login(self):
        print("Hello world!")

    def Switch(self):
        window.SetActiveWindow(window.RegisterWindow)

    def Back(self):
        window.SetActiveWindow(window.MenuWindow)


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
        self.submitButton.clicked.connect(self.Register)

        self.switchButton = QPushButton("Already have an account? Sign in")
        self.switchButton.clicked.connect(self.Switch)

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(self.Back)

        self.addWidget(self.label, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.usernameInput, 1, 1, 1, 2)
        self.addWidget(self.passwordInput, 2, 1, 1, 2)
        self.addWidget(self.confirmPasswordInput, 3, 1, 1, 2)
        self.addWidget(self.switchButton, 4, 1, 1, 2)
        self.addWidget(self.submitButton, 5, 1, 1, 2)
        self.addWidget(self.backButton, 6, 1, 1, 2)

    def Register(self):
        pass

    def Switch(self):
        window.SetActiveWindow(window.LoginWindow)

    def Back(self):
        window.SetActiveWindow(window.MenuWindow)


class MenuWindow(QGridLayout):
    def __init__(self):
        super().__init__()

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
        window.SetActiveWindow(window.LoginWindow)

    def Register(self):
        window.SetActiveWindow(window.RegisterWindow)

    def Pricing(self):
        print("Hello world!")


class WindowManager(QWidget):

    def __init__(self):
        super().__init__()
        self.Box = QVBoxLayout()
        self.FLoginWindow = LoginWindow()
        self.FMenuWindow = MenuWindow()
        self.FRegisterWindow = RegisterWindow()

        self.LoginWindow = QFrame()
        self.LoginWindow.setLayout(self.FLoginWindow)

        self.MenuWindow = QFrame()
        self.MenuWindow.setLayout(self.FMenuWindow)

        self.RegisterWindow = QFrame()
        self.RegisterWindow.setLayout(self.FRegisterWindow)

        self.Box.addWidget(self.LoginWindow)
        self.Box.addWidget(self.MenuWindow)
        self.Box.addWidget(self.RegisterWindow)

        self.setLayout(self.Box)
        self.show()

    def SetActiveWindow(self, showWindow):
        # hide all items currently in boxlayout
        self.LoginWindow.hide()
        self.MenuWindow.hide()
        self.RegisterWindow.hide()

        showWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WindowManager()
    window.setGeometry(300, 300, 800, 600)
    window.show()
    window.SetActiveWindow(window.MenuWindow)

    app.exec()
