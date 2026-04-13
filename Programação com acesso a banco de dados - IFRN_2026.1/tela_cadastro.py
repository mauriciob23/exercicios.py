from PyQt5 import QtCore, QtWidgets
from tela_cadastro_db import conexao, cursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Janela
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 211)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Nome:
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName("lineEdit_name")

        # Curso:
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_curso = QtWidgets.QLabel(self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 1, 0, 1, 1)
        self.lineEdit_curso = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_curso.setObjectName("lineEdit_curso")

        # Serie:
        self.gridLayout.addWidget(self.lineEdit_curso, 1, 1, 1, 1)
        self.label_serie = QtWidgets.QLabel(self.centralwidget)
        self.label_serie.setObjectName("label_serie")
        self.gridLayout.addWidget(self.label_serie, 2, 0, 1, 1)
        self.lineEdit_serie = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_serie.setObjectName("lineEdit_serie")

        # Botão Salvar:
        self.gridLayout.addWidget(self.lineEdit_serie, 2, 1, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")

        self.pushButton_salvar.clicked.connect(self.salvar)  # Chamando a função

        self.gridLayout.addWidget(self.pushButton_salvar, 3, 1, 1, 1)

        ############
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Aluno"))
        self.label_name.setText(_translate("MainWindow", "Nome"))
        self.label_curso.setText(_translate("MainWindow", "Curso"))
        self.label_serie.setText(_translate("MainWindow", "Serie"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))

    def salvar(self):
        nome = self.lineEdit_name.text()
        curso = self.lineEdit_curso.text()
        serie = self.lineEdit_serie.text()

        sql = f"""
            INSERT INTO alunos VALUES
            (null, '{nome}', '{curso}', '{serie}');
            """

        cursor.execute(sql)
        conexao.commit()
        print("Cadastrado com sucesso!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
