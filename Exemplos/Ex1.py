#Exemplo 1: Uma simples Janela

import sys                                                                  # importa a biblioteca de sistema
from PySide2.QtWidgets import QApplication, QWidget                             



app = QApplication(sys.argv)                                                
mainwindow = QWidget()
mainwindow.resize(550, 400)
mainwindow.setWindowTitle("Olá Mundo Pyside2")
mainwindow.show()
app.exec_()