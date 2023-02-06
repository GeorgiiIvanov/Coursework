from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import json
import os.path
from Game import *
from encryption import *

Form, Window = uic.loadUiType("authorization.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def click_ButtonwithBot():
    window2.close()
    newGame(True)
    game()


def click_Button2Player():
    window2.close()
    newGame(False)
    game()


def click_ButtonRegistr():
    global window1
    Form1, Window1 = uic.loadUiType("registration.ui")
    window1 = Window1()
    form1 = Form1()
    form1.setupUi(window1)

    window1.show()
    window.close()


    def click_ButtonSignUp():
        global window2
        Form2, Window2 = uic.loadUiType("gameMode.ui")
        window2 = Window2()
        form2 = Form2()
        form2.setupUi(window2)

        user = {"login": encrypt(form1.loginREG.displayText(), key, alfavit), "password": encrypt(form1.passwordREG.displayText(), key, alfavit)}
        if len(form1.passwordREG.displayText()) >= 8 and len(form1.loginREG.displayText()) > 0:
            if os.path.isfile("data.json"):
                with open("data.json", "r", encoding='utf-8') as file:
                    users = json.loads(file.read())
            else:
                users = []
            if user not in users:
                with open("data.json", "w", encoding='utf-8') as file:
                    users.append(user)
                    file.write(json.dumps(users))
                window2.show()
                window1.close()
        form2.ButtonwithBot.clicked.connect(click_ButtonwithBot)
        form2.Button2Player.clicked.connect(click_Button2Player)
    form1.ButtonSignUp.clicked.connect(click_ButtonSignUp)


def click_ButtonLogIN():
    global window2
    Form2, Window2 = uic.loadUiType("gameMode.ui")
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)

    user = {"login": encrypt(form.loginAFT.displayText(), key, alfavit), "password": encrypt(form.passwordAFT.displayText(), key, alfavit)}
    if os.path.isfile("data.json"):
        with open("data.json", "r", encoding='utf-8') as file:
            users = json.loads(file.read())
    else:
        users = []
    if user in users:
        window2.show()
        window.close()
    form2.ButtonwithBot.clicked.connect(click_ButtonwithBot)
    form2.Button2Player.clicked.connect(click_Button2Player)


form.ButtonLogIN.clicked.connect(click_ButtonLogIN)
form.ButtonRegistr.clicked.connect(click_ButtonRegistr)
app.exec_()



