from conexao import cursor
from PyQt5 import QtCore, QtWidgets


class Ui_Pesquisa(object):
    def setupUi(self, Pesquisa):
        Pesquisa.setObjectName("Pesquisa")
        Pesquisa.resize(539, 409)
        self.centralwidget = QtWidgets.QWidget(Pesquisa)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.horizontalLayout.addWidget(self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.horizontalLayout.addWidget(self.lineEdit_nome)
        self.pushButton_pesquisa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pesquisa.setObjectName("pushButton_pesquisa")
        self.horizontalLayout.addWidget(self.pushButton_pesquisa)

        self.pushButton_pesquisa.clicked.connect(self.pesquisar)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_tabela = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_tabela.setObjectName("tableWidget_tabela")
        self.tableWidget_tabela.setColumnCount(4)
        self.tableWidget_tabela.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tabela.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget_tabela)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        Pesquisa.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pesquisa)
        QtCore.QMetaObject.connectSlotsByName(Pesquisa)

    def retranslateUi(self, Pesquisa):
        _translate = QtCore.QCoreApplication.translate
        Pesquisa.setWindowTitle(_translate("Pesquisa", "Pesquisa Alunos"))
        self.label_nome.setText(_translate("Pesquisa", "Nome:"))
        self.pushButton_pesquisa.setText(_translate("Pesquisa", "Pesquisar"))
        item = self.tableWidget_tabela.horizontalHeaderItem(0)
        item.setText(_translate("Pesquisa", "Código"))
        item = self.tableWidget_tabela.horizontalHeaderItem(1)
        item.setText(_translate("Pesquisa", "Nome"))
        item = self.tableWidget_tabela.horizontalHeaderItem(2)
        item.setText(_translate("Pesquisa", "Curso"))
        item = self.tableWidget_tabela.horizontalHeaderItem(3)
        item.setText(_translate("Pesquisa", "Série"))

    def pesquisar(self):
        nome = self.lineEdit_nome.text()
        sql = f"""
                SELECT * FROM alunos
                WHERE nome LIKE '%{nome}%'
                OR curso LIKE '%{nome}%';
                """

        cursor.execute(sql)
        dados = (
            cursor.fetchall()
        )  # transfere os dados do cursor para uma variavel (dados)

        self.tableWidget_tabela.setRowCount(
            cursor.rowcount
        )  # Define a quantidade de linhas

        for lin, linha in enumerate(dados):
            for col, valor in enumerate(linha):
                item = QtWidgets.QTableWidgetItem(str(valor))   # Passando como string para nao ter problemas ao exibir os dados (contar também)
                self.tableWidget_tabela.setItem(lin, col, item)

        self.tableWidget_tabela.resizeColumnsToContents()   # Organiza a formatação da exibição da tabela
        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Pesquisa = QtWidgets.QMainWindow()
    ui = Ui_Pesquisa()
    ui.setupUi(Pesquisa)
    Pesquisa.show()
    sys.exit(app.exec_())
