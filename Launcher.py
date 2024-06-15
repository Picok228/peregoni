import json


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from main import start_game

app = QApplication([])
window = QWidget()
window.setWindowTitle("Супер лаунчер")
window.resize(300, 300)
window.show()


settings = {}
def read_data():
    global settings

    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)

Golovna_linia = QHBoxLayout()
grati = QPushButton("Грати")
Golovna_linia.addWidget(grati)

main_line = QVBoxLayout()

knopka_start = QPushButton("Старт")

main_line.addWidget(knopka_start)



knopka_start.clicked.connect(start_game)
def change_data():
    settings["skin"] = line_edit.text()
    write_data()

window.show()

app.exec()
