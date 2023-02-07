# Gera bolas com formato aleatório
import sys
from random import randint
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem)
from PySide2.QtGui import QBrush, QPen, QColor
from PySide2.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bola Aleatória")
        self.resize(800,600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        widgets_layout = QVBoxLayout()
        layout.addLayout(widgets_layout)

        self.label = QLabel("Nenhuma bola gerada")
        widgets_layout.addWidget(self.label)

        self.button = QPushButton("Gerar Bola")
        self.button.clicked.connect(self.gerar_bola)
        widgets_layout.addWidget(self.button)

        self.apagar_button = QPushButton("Apagar")
        self.apagar_button.clicked.connect(self.apagar_bola)
        widgets_layout.addWidget(self.apagar_button)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)

        self.timer = QTimer()
        self.timer.timeout.connect(self.gerar_bola)
        self.timer.start(1000)

        self.show()

    def gerar_bola(self):
        self.scene.clear()
        size = randint(20, 80)
        x = randint(0, 300 - size)
        y = randint(0, 300 - size)
        brush = QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        pen = QPen(Qt.black)
        pen.setWidth(2)
        self.bola = QGraphicsEllipseItem(x, y, size, size)
        self.bola.setBrush(brush)
        self.bola.setPen(pen)
        self.scene.addItem(self.bola)
        self.label.setText(f"Bola gerada com tamanho {size}")

    def apagar_bola(self):
        self.scene.clear()
        self.label.setText("Nenhuma bola gerada")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())