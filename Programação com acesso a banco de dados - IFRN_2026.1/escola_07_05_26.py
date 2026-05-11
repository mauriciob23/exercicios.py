from PyQt5 import QtCore, QtWidgets

import mariadb

conexao = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")

        self.pushButton_pesquisar.clicked.connect(self.pesquisar)

        self.gridLayout.addWidget(self.pushButton_pesquisar, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pesquisa"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.pushButton_pesquisar.setText(_translate("MainWindow", "Pesquisar"))

    def pesquisar(self):
        nome = self.lineEdit.text()
        sql = f'''SELECT * FROM alunos
                WHERE nome LIKE '%{nome}%' 
                OR curso LIKE '%{nome}%'; '''
        
        cursor.execute(sql)

        texto = ""

        texto += str(cursor.rowcount) + " resultado(s) encontrado(s):\n\n"      # Conta os resultados encontrados


        for linha in cursor:
            texto += "Código: " + str(linha[0]) + "\n"
            texto += "Nome: " + linha[1] + "\n"
            texto += "Curso: " + linha[2] + "\n" 
            texto += "Serie: " + str(linha[3]) + "\n\n"


        self.plainTextEdit.setPlainText(texto)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())