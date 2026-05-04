from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime

import mariadb
conexao = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="empresa",
    )

cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(284, 107)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.marcar)

        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MATRUCULA:"))
        self.pushButton.setText(_translate("MainWindow", "MARCAR PONTO"))

    def marcar(self):
        matricula = self.lineEdit.text()
        sql = f'''
            INSERT INTO ponto02
            VALUES(
                null,
                {matricula},
                now()
                );'''
        
        cursor.execute(sql)
        conexao.commit()

        datahora = QDateTime.currentDateTime().toString("dd-MM-yyyy HH:mm:ss")

        msg = QMessageBox()
        msg.setText(f"PONTO MARCADO\n{datahora}")
        msg.exec_()

        self.lineEdit.setText("") #Limpando texto escrito


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())