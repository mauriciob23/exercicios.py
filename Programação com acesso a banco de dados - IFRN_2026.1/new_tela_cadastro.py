from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tela_cadastro_db import conexao, cursor

lista_cursos = []


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(317, 164)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")

        # Nome:
        self.label_nome = QtWidgets.QLabel(Dialog)
        self.label_nome.setObjectName("label_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nome
        )

        # Cursos:
        self.label_cursos = QtWidgets.QLabel(Dialog)
        self.label_cursos.setObjectName("label_cursos")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_cursos)
        self.label_serie = QtWidgets.QLabel(Dialog)

        # Serie:
        self.label_serie.setObjectName("label_serie")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_serie)
        self.pushButton_salvar = QtWidgets.QPushButton(Dialog)

        # Botão salvar:
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.pushButton_salvar
        )

        # ComboBox de cursos:
        self.comboBox_cursos = QtWidgets.QComboBox(Dialog)
        self.comboBox_cursos.setObjectName("comboBox_cursos")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.comboBox_cursos
        )

        # Linha de edição da serie:
        self.lineEdit_serie = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_serie.setObjectName("lineEdit_serie")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_serie
        )

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadastro de Alunos"))
        self.label_nome.setText(_translate("Dialog", "Nome:"))
        self.label_cursos.setText(_translate("Dialog", "Cursos:"))
        self.label_serie.setText(_translate("Dialog", "Serie:"))
        self.pushButton_salvar.setText(_translate("Dialog", "SALVAR"))

    # Carregando cursos em ordem alfabetica no comboBox
    def carregar_cursos(self):
        cursor.execute("SELECT * FROM cursos ORDER BY nome")
        for linha in cursor:
            self.comboBox_cursos.addItem(linha[1])  # Nome do curso
            lista_cursos.append(linha[0])

    # Salvando:
    def salvar(self):
        nome = self.lineEdit_nome.text()
        # curso = self.comboBox_cursos.currentText() # texto do item sendo selecionado
        posicao = self.comboBox_cursos.currentIndex()
        curso = lista_cursos[posicao]
        serie = self.lineEdit_serie.text()

        sql = f"""
            INSERT INTO alunos VALUES
            (null, '{nome}', '{curso}', '{serie}');
            """

        cursor.execute(sql)
        conexao.commit()

        msg = QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText("Cadastrado com sucesso!")
        msg.exec()

        # self.lineEdit_nome.setText


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
