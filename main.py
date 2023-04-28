from PyQt6.QtWidgets import QApplication, QWidget
import sys
import pyrebase
from auth import Login, Register

# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
# app.exec()

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

if __name__ == "__main__":
    username = input("Enter your email: ")
    password = input("Enter your password: ")

    user = Register(auth, username, password)
