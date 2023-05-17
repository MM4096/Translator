from platformdirs import *
from os import path
from os import makedirs
from cryptography.fernet import Fernet


def Encrypt(data):
    if not path.exists(path.join(user_data_dir("Translator", "mm4096"), "key.key")):
        key = Fernet.generate_key()
        with open(path.join(user_data_dir("Translator", "mm4096"), "key.key"), "w") as key_file:
            key_file.write(key.decode("utf-8"))

        with open(path.join(user_data_dir("Translator", "mm4096"), "IMPORTANT.md"), "w") as file:
            file.write("Do not modify any of the files in this folder. If you do, your data may be corrupted")

    with open(path.join(user_data_dir("Translator", "mm4096"), "key.key"), "r") as key_file:
        key = key_file.read()

    f = Fernet(key)

    return f.encrypt(data.encode("utf-8")).decode("utf-8")


def Decrypt(data):
    with open(path.join(user_data_dir("Translator", "mm4096"), "key.key"), "r") as key_file:
        key = key_file.read()

    f = Fernet(key)

    return f.decrypt(data)


def WriteData(relPath, data):
    if not path.exists(user_data_dir("Translator", "mm4096")):
        makedirs(user_data_dir("Translator", "mm4096"))

    location = user_data_dir("Translator", "mm4096")
    with open(path.join(location, relPath), "w") as f:
        f.write(Encrypt(data))


def ReadData(relPath):
    location = user_data_dir("Translator", "mm4096")
    if path.exists(location):
        try:
            with open(path.join(location, relPath), "r") as f:
                return Decrypt(f.read()).decode("utf-8")
        except FileNotFoundError:
            return None
    else:
        return None


def GetDataPath():
    return user_data_dir("Translator", "mm4096")
