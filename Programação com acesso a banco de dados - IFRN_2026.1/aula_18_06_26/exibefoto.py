from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

##################################
import mariadb
conexao = mariadb.connect(
    host="localhost", user="root", password="", database="imagens"
)
cursor = conexao.cursor()
##################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.carregar)

        self.verticalLayout.addWidget(self.pushButton)
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(12)
        self.label_nome.setFont(font)
        self.label_nome.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.label_nome.setObjectName("label_nome")
        self.verticalLayout.addWidget(self.label_nome)
        self.label_foto = QtWidgets.QLabel(self.centralwidget)
        self.label_foto.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Vineta BT")
        font.setPointSize(12)
        self.label_foto.setFont(font)
        self.label_foto.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_foto.setObjectName("label_foto")
        self.verticalLayout.addWidget(self.label_foto)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "Código"))
        self.pushButton.setText(_translate("MainWindow", "Comprar"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_foto.setText(_translate("MainWindow", "Foto: "))

    def carregar(self):
        codigo = self.lineEdit.text()
        sql = "SELECT nome, foto FROM cliente WHERE codigo = " + codigo
        cursor.execute(sql)
        # dados = cursor.fetchone()
        # nome, foto = dados      # separa os itens em variáveis
        nome, foto = (
            cursor.fetchone()
        )  # pode ser assim tambem, sem usar a variavel dados

        self.label_nome.setText("Nome: " + nome)

        pixmap = QPixmap()  # Cria o objeto
        pixmap.loadFromData(foto)  # Carrega a foto no objeto
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation) # Redimenciona imagem

        self.label_foto.setPixmap(pixmap)  # aplica o objeto da foto no label

        # self.label_foto.setText("Foto: " + foto) # <=== isso aqui NÃO existe pra exibição de foto


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
