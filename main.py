import sys
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtQuickWidgets import QQuickWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    quick_widget = QQuickWidget()
    url = QUrl("Qml\quickProgram.qml")
    quick_widget.setSource(url)
    sys.exit(app.exec_())