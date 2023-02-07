#Exemplo2: Um janela que contem um botao e um texto, sempre que carrego no botão apaga o que está no texto
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Texto a ser apagado")
        self.button = QPushButton("Apagar")
        self.button.clicked.connect(self.clear_text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def clear_text(self):
        self.label.setText("")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())