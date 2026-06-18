user = input("Nome do usuário: ")

import sys

from aula_28_05_26.menu import Ui_Menu
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

tela = QtWidgets.QMainWindow()
tmenu = Ui_Menu(user)  ## CONSTRUTOR MODIFICADO
tmenu.setupUi(tela)
tela.show()
