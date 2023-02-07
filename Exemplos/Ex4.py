# Exemplo de uma caixa de texto com um botao que imprime numa label o que foi escrito
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit()
        self.button = QPushButton("Mostrar")
        self.button.clicked.connect(self.show_text)
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_text(self):
        self.label.setText(self.line_edit.text())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())