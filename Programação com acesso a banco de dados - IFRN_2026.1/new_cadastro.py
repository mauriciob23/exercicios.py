from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from new_cadastro_db import conexao, cursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout_2.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout_2.addWidget(self.lineEdit_nome, 1, 0, 1, 1)
        self.verticalLayout_nome = QtWidgets.QVBoxLayout()
        self.verticalLayout_nome.setObjectName("verticalLayout_nome")
        self.gridLayout_2.addLayout(self.verticalLayout_nome, 2, 0, 1, 1)
        self.label_pessoa = QtWidgets.QLabel(self.centralwidget)
        self.label_pessoa.setObjectName("label_pessoa")
        self.gridLayout_2.addWidget(self.label_pessoa, 3, 0, 1, 1)
        self.radioButton_juridica = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_juridica.setObjectName("radioButton_juridica")
        self.gridLayout_2.addWidget(self.radioButton_juridica, 4, 0, 1, 1)
        self.radioButton_fisica = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_fisica.setObjectName("radioButton_fisica")
        self.gridLayout_2.addWidget(self.radioButton_fisica, 5, 0, 1, 1)
        self.verticalLayout_pessoa = QtWidgets.QVBoxLayout()
        self.verticalLayout_pessoa.setObjectName("verticalLayout_pessoa")
        self.gridLayout_2.addLayout(self.verticalLayout_pessoa, 6, 0, 1, 1)
        self.label_observacao = QtWidgets.QLabel(self.centralwidget)
        self.label_observacao.setObjectName("label_observacao")
        self.gridLayout_2.addWidget(self.label_observacao, 7, 0, 1, 1)
        self.plainTextEdit_observacao = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_observacao.setObjectName("plainTextEdit_observacao")
        self.gridLayout_2.addWidget(self.plainTextEdit_observacao, 8, 0, 1, 1)
        self.verticalLayout_observacao = QtWidgets.QVBoxLayout()
        self.verticalLayout_observacao.setObjectName("verticalLayout_observacao")
        self.gridLayout_2.addLayout(self.verticalLayout_observacao, 9, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 10, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 11, 0, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        ##
        self.pushButton_salvar.clicked.connect(self.salvar)
        ##
        self.gridLayout_2.addWidget(self.pushButton_salvar, 12, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Clientes"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_pessoa.setText(_translate("MainWindow", "Pessoa:"))
        self.radioButton_juridica.setText(_translate("MainWindow", "Juridica"))
        self.radioButton_fisica.setText(_translate("MainWindow", "Física"))
        self.label_observacao.setText(_translate("MainWindow", "Observação:"))
        self.label_4.setText(_translate("MainWindow", "Ativo:"))
        self.checkBox.setText(_translate("MainWindow", "Sim"))
        self.pushButton_salvar.setText(_translate("MainWindow", "SALVAR"))

    def salvar(self):
        nome = self.lineEdit_nome.text()
        pessoa = ""
        if self.radioButton_fisica.isChecked():
            pessoa = "Física"

        elif self.radioButton_juridica.isChecked():
            pessoa = "Jurídica"

        observacao = self.plainTextEdit_observacao.toPlainText()

        ativo = "Não"
        if self.checkBox.isChecked():
            ativo = "Sim"

        sql = f'''INSERT INTO cliente VALUES(
                    null, '{nome}', '{pessoa}', '{observacao}', '{ativo}' )'''
        
        cursor.execute(sql)
        conexao.commit()
        print("INSERIDO COM SUCESSO!!!")

        msg = QMessageBox()           # msg confirmação
        msg.setWindowTitle("Aviso")
        msg.setText("INSERIDO COM SICESSO!!")
        msg.exec()

        ## LIMPA FORMULARIO ##
        self.lineEdit_nome.setText("")
        self.plainTextEdit_observacao.setPlainText("")
        self.checkBox.setChecked(False)

        self.radioButton_fisica.setAutoExclusive(False)
        self.radioButton_juridica.setAutoExclusive(False)

        self.radioButton_fisica.setChecked(False)
        self.radioButton_juridica.setChecked(False)

        self.radioButton_fisica.setAutoExclusive(True)
        self.radioButton_juridica.setAutoExclusive(True)

        self.lineEdit_nome.setFocus()       # MArca o campo do nome para iniciar

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())