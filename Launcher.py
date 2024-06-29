import json


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from magazine import start_magaz
from main import start_game

app = QApplication([])
window = QWidget()
window.setWindowTitle("Супер лаунчер")
window.resize(300, 300)
window.show()


settings = {}
#def read_data():
#    global settings
#    try:
#        with open("settings.json", "r", encoding="utf-8") as file:
#            settings = json.load(file)
#    except:
#        settings ={
#                "skin": "optimys_prime/img.png",
#                "money": 100
#            }
#def write_data():
#    global settings
#    with open("settings.json", "w", encoding="utf-8") as file:
#        json.dump(settings, file, indent=4, ensure_ascii=False)
#
#def buy_skin_1():
#    read_data()
#    if settings["money"] >=7:
#        settings["money"] -= 7
#        settings["skin"] = "optimys_prime/автомобіль2.png"
#        write_data()
#    else:
#        print("Грочей не хватає")





knopka1 = QPushButton("Грати")
leave = QPushButton("Вийти з гри")
buy_skin = QPushButton("Купити скін")

h1 = QVBoxLayout()
h1.addWidget(knopka1)
h1.addWidget(leave)
h1.addWidget(buy_skin)

window.setLayout(h1)
knopka1.clicked.connect(start_game)
buy_skin.clicked.connect(start_magaz)
leave.clicked.connect(quit)






window.show()

app.exec()
