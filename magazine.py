import json


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


def start_magaz():
    window = QDialog()
    window.setWindowTitle("Магазин")
    window.resize(400, 400)
    window.show()


    knopka1 = QPushButton("Грати")
    kartinka_px = QPixmap("optimys_prime/бус-removebg-preview.png")
    kartinka = QLabel("optimys_prime/бус-removebg-preview.png")
    kartinka2_px = QPixmap("optimys_prime/автомобіль3.png")
    kartinka2_px=kartinka2_px.scaledToWidth(125)
    kartinka2 = QLabel("optimys_prime/автомобіль3.png")
    kartinka3_px = QPixmap("optimys_prime/автомобіль4.png")
    kartinka3_px = kartinka3_px.scaledToWidth(135)
    kartinka3 = QLabel("optimys_prime/автомобіль4.png")
    buy_skin_1_btn = QPushButton("Купити скін")
    h1 = QVBoxLayout()
    h2 = QHBoxLayout()

    h1.addWidget(knopka1)
    h2.addWidget(kartinka)
    h2.addWidget(kartinka2)
    h2.addWidget(kartinka3)
    h1.addLayout(h2)
    h1.addWidget(buy_skin_1_btn)

    window.setLayout(h1)

    settings = {}

    def read_data():
        global settings
        try:
            with open("settings.json", "r", encoding="utf-8") as file:
                settings = json.load(file)
        except:
            settings = {
                "skin": "optimys_prime/img.png",
                "money": 100
            }

    def write_data():
        global settings
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4, ensure_ascii=False)

    def buy_skin_1():
        read_data()
        if settings["money"] >= 7:
            settings["money"] -= 7
            settings["skin"] = "optimys_prime/автомобіль2.png"
            write_data()
        else:
            print("Грочей не хватає")


    kartinka.setPixmap(kartinka_px)
    kartinka2.setPixmap(kartinka2_px)
    kartinka3.setPixmap(kartinka3_px)
    window.show()

    window.exec()