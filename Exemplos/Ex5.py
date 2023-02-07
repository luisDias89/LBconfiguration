# Neste programa conjuga todos os programas, anteriores, caixa de texto label, botao para mostrar e apagar a o texto da label

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit()
        self.show_button = QPushButton("Mostrar")
        self.show_button.clicked.connect(self.show_text)
        self.clear_button = QPushButton("Limpar")
        self.clear_button.clicked.connect(self.clear_text)
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.show_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_text(self):
        self.label.setText(self.line_edit.text())

    def clear_text(self):
        self.label.setText("")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())