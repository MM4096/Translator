from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout, QGridLayout, \
    QLineEdit, QStackedWidget, QHBoxLayout, QFrame, QDialog, QDialogButtonBox

from enum import Enum

import sys
import pyrebase
import asyncio
from auth import Login, Register, ReturnEnum
from writeFiles import WriteData, ReadData

firebaseConfig = {
    "apiKey": "AIzaSyD9xGtjutq5jqbNJaCbLUmiv-FS0l2lJ8c",
    "authDomain": "translator-35a8b.firebaseapp.com",
    "projectId": "translator-35a8b",
    "storageBucket": "translator-35a8b.appspot.com",
    "messagingSenderId": "662457562337",
    "appId": "1:662457562337:web:1982e7fd646e56d447b3a0",
    "databaseURL": "https://translator-35a8b-default-rtdb.asia-southeast1.firebasedatabase.app",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

user = None


class MainWindow(QGridLayout):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Translator")
        self.translateButton = QPushButton("Translate")
        self.translateButton.clicked.connect(self.TranslatePage)
        self.transcribeButton = QPushButton("Transcribe")
        self.transcribeButton.clicked.connect(self.TranscribePage)
        self.pricingButton = QPushButton("Pricing")
        self.pricingButton.clicked.connect(self.PricingPage)
        self.logoutButton = QPushButton("Log out")
        self.logoutButton.clicked.connect(self.Logout)

        self.addWidget(self.label, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.translateButton, 1, 1, 1, 1)
        self.addWidget(self.transcribeButton, 2, 1, 1, 1)
        self.addWidget(self.pricingButton, 3, 1, 1, 1)
        self.addWidget(self.logoutButton, 4, 1, 1, 1)

    def PricingPage(self):
        window.SetActiveWindow(window.PricingWindow)

    def TranslatePage(self):
        pass

    def TranscribePage(self):
        pass

    def Logout(self):
        global user
        user = None
        WriteData("user.data", "")
        window.SetActiveWindow(window.MenuWindow)


class LoginWindow(QGridLayout):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Log in")

        self.usernameInput = QLineEdit()
        self.usernameInput.setPlaceholderText("Enter your email")

        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Enter your password")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirmPasswordInput = QLineEdit()
        self.confirmPasswordInput.setPlaceholderText("Confirm your password")
        self.confirmPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.submitButton = QPushButton("Log in")
        self.submitButton.clicked.connect(self.Login)

        self.switchButton = QPushButton("Don't have an account? Sign up")
        self.switchButton.clicked.connect(self.Switch)

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(self.Back)

        self.usernameError = QLabel()
        self.usernameError.setStyleSheet("color: red")
        self.passwordError = QLabel()
        self.passwordError.setStyleSheet("color: red")

        self.addWidget(self.label, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.usernameInput, 1, 1, 1, 2)
        self.addWidget(self.usernameError, 1, 3, 1, 1)
        self.addWidget(self.passwordInput, 2, 1, 1, 2)
        self.addWidget(self.passwordError, 2, 3, 1, 1)
        self.addWidget(self.switchButton, 4, 1, 1, 2)
        self.addWidget(self.submitButton, 5, 1, 1, 2)
        self.addWidget(self.backButton, 6, 1, 1, 2)

    def Login(self):
        self.usernameError.setText("")
        self.passwordError.setText("")
        email = self.usernameInput.text()
        password = self.passwordInput.text()
        result = Login(auth, email, password)
        global user
        user = result[0]

        returnMessage = result[1]

        if user is not None:
            self.usernameInput.setText("")
            self.passwordInput.setText("")
            WriteData("user.data", email + "," + password)
            window.SetActiveWindow(window.MainWindow)
        else:
            if returnMessage == ReturnEnum.USER_DISABLED:
                self.usernameError.setText("User is disabled")
            elif returnMessage == ReturnEnum.INVALID_EMAIL:
                self.usernameError.setText("Invalid email")
            elif returnMessage == ReturnEnum.INVALID_PASSWORD:
                self.passwordError.setText("Incorrect password")
            elif returnMessage == ReturnEnum.EMAIL_NOT_FOUND:
                self.usernameError.setText("Account not found")
            elif returnMessage == ReturnEnum.TOO_MANY_ATTEMPTS_TRY_LATER:
                self.usernameError.setText("Too many attempts, try again later")

    def Switch(self):
        window.SetActiveWindow(window.RegisterWindow)

    def Back(self):
        window.SetActiveWindow(window.MenuWindow)


class PricingWindow(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Pricing")

        self.basicCredit = QVBoxLayout()

        self.premiumCredit = QVBoxLayout()

        self.bundleCredit = QVBoxLayout()

        self.bcHeader = QLabel("Basic")
        self.bcContent = QLabel("+ 10 minutes")
        self.bcPrice = QLabel("$2")
        self.bcButton = QPushButton("Buy")

        self.basicCredit.addWidget(self.bcHeader)
        self.basicCredit.addWidget(self.bcContent)
        self.basicCredit.addWidget(self.bcPrice)
        self.basicCredit.addWidget(self.bcButton)

        self.pcHeader = QLabel("Premium")
        self.pcContent = QLabel("+30 minutes")
        self.pcPrice = QLabel("$5.50")
        self.pcButton = QPushButton("Buy")

        self.premiumCredit.addWidget(self.pcHeader)
        self.premiumCredit.addWidget(self.pcContent)
        self.premiumCredit.addWidget(self.pcPrice)
        self.premiumCredit.addWidget(self.pcButton)

        self.bundleHeader = QLabel("Bundle")
        self.bundleContent = QLabel("+ 60 minutes")
        self.bundlePrice = QLabel("$10")
        self.bundleButton = QPushButton("Buy")

        self.bundleCredit.addWidget(self.bundleHeader)
        self.bundleCredit.addWidget(self.bundleContent)
        self.bundleCredit.addWidget(self.bundlePrice)
        self.bundleCredit.addWidget(self.bundleButton)

        self.pricingLayouts = QHBoxLayout()

        self.pricingLayouts.addLayout(self.basicCredit)
        self.pricingLayouts.addLayout(self.premiumCredit)
        self.pricingLayouts.addLayout(self.bundleCredit)

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(self.Back)

        self.addWidget(self.label, Qt.AlignmentFlag.AlignCenter)
        self.addLayout(self.pricingLayouts, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.backButton, Qt.AlignmentFlag.AlignCenter)

    def Back(self):
        if user is None:
            window.SetActiveWindow(window.MenuWindow)
        else:
            window.SetActiveWindow(window.MainWindow)


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

        self.usernameError = QLabel()
        self.usernameError.setStyleSheet("color: red")
        self.passwordError = QLabel()
        self.passwordError.setStyleSheet("color: red")
        self.confirmPasswordError = QLabel()
        self.confirmPasswordError.setStyleSheet("color: red")

        self.addWidget(self.label, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self.usernameInput, 1, 1, 1, 2)
        self.addWidget(self.usernameError, 1, 3, 1, 1)
        self.addWidget(self.passwordInput, 2, 1, 1, 2)
        self.addWidget(self.passwordError, 2, 3, 1, 1)
        self.addWidget(self.confirmPasswordInput, 3, 1, 1, 2)
        self.addWidget(self.confirmPasswordError, 3, 3, 1, 1)
        self.addWidget(self.switchButton, 4, 1, 1, 2)
        self.addWidget(self.submitButton, 5, 1, 1, 2)
        self.addWidget(self.backButton, 6, 1, 1, 2)

    def Register(self):
        self.usernameError.setText("")
        self.passwordError.setText("")
        self.confirmPasswordError.setText("")
        if self.passwordInput.text() != self.confirmPasswordInput.text():
            self.confirmPasswordError.setText("Passwords do not match")
            return
        result = Register(auth, self.usernameInput.text(), self.passwordInput.text())
        global user
        user = result[0]

        returnMessage = result[1]

        if user is not None:
            user = None
            self.usernameInput.hide()
            self.passwordInput.hide()
            self.confirmPasswordInput.hide()
            self.switchButton.hide()
            self.label.setText("A verification email has been sent to your email address. Please verify your account.")
            self.submitButton.hide()
            self.usernameInput.setText("")
            self.passwordInput.setText("")
            self.confirmPasswordInput.setText("")
        else:
            if returnMessage == ReturnEnum.EMAIL_EXISTS:
                self.usernameError.setText("Email already exists")
            elif returnMessage == ReturnEnum.INVALID_EMAIL:
                self.usernameError.setText("Invalid email")
            elif returnMessage == ReturnEnum.WEAK_PASSWORD:
                self.passwordError.setText("Password too weak!")

    def Switch(self):
        window.SetActiveWindow(window.LoginWindow)

    def Back(self):
        window.SetActiveWindow(window.MenuWindow)

    def Reset(self):
        self.usernameInput.show()
        self.passwordInput.show()
        self.confirmPasswordInput.show()
        self.switchButton.show()
        self.label.setText("Sign up")
        self.submitButton.show()
        self.usernameInput.setText("")
        self.passwordInput.setText("")
        self.confirmPasswordInput.setText("")


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
        self.addWidget(loginButton, 1, 1, 1, 1)
        self.addWidget(registerButton, 2, 1, 1, 1)
        self.addWidget(pricingButton, 3, 1, 1, 1)

    def Login(self):
        window.SetActiveWindow(window.LoginWindow)

    def Register(self):
        window.SetActiveWindow(window.RegisterWindow)

    def Pricing(self):
        window.SetActiveWindow(window.PricingWindow)


class WindowManager(QWidget):

    def __init__(self):
        super().__init__()
        self.Box = QVBoxLayout()
        self.FLoginWindow = LoginWindow()
        self.FMenuWindow = MenuWindow()
        self.FRegisterWindow = RegisterWindow()
        self.FMainWindow = MainWindow()
        self.FPricingWindow = PricingWindow()

        self.LoginWindow = QFrame()
        self.LoginWindow.setLayout(self.FLoginWindow)

        self.MenuWindow = QFrame()
        self.MenuWindow.setLayout(self.FMenuWindow)

        self.RegisterWindow = QFrame()
        self.RegisterWindow.setLayout(self.FRegisterWindow)

        self.MainWindow = QFrame()
        self.MainWindow.setLayout(self.FMainWindow)

        self.PricingWindow = QFrame()
        self.PricingWindow.setLayout(self.FPricingWindow)

        self.Box.addWidget(self.LoginWindow)
        self.Box.addWidget(self.MenuWindow)
        self.Box.addWidget(self.RegisterWindow)
        self.Box.addWidget(self.MainWindow)
        self.Box.addWidget(self.PricingWindow)

        self.setLayout(self.Box)
        self.show()

        self.setWindowTitle("Translator")

    def SetActiveWindow(self, showWindow):
        # hide all items currently in boxlayout
        self.LoginWindow.hide()
        self.MenuWindow.hide()
        self.RegisterWindow.hide()
        self.MainWindow.hide()
        self.FRegisterWindow.Reset()
        self.PricingWindow.hide()

        showWindow.show()


async def LoginSavedUser():
    savedUser = ReadData("user.data")
    if savedUser != "":
        global user
        user = Login(auth, savedUser[0], savedUser[1])
        if user is not None:
            window.SetActiveWindow(window.MainWindow)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WindowManager()
    window.setFixedSize(600, 600)
    window.show()
    window.SetActiveWindow(window.MenuWindow)

    asyncio.run(LoginSavedUser())

    app.exec()
