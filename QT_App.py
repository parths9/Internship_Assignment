from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QComboBox, QLabel
from PyQt5.QtCore import QTimer
import sys

class CustomComboBox(QComboBox):
    def showPopup(self):
        super().showPopup()
        self.view().setMinimumHeight(self.view().sizeHintForRow(0) * 4)
        self.view().setMaximumHeight(self.view().sizeHintForRow(0) * 4)

class Counter_Window(QWidget):
    def __init__(self, color, counter):
        super().__init__()

        self.resize(40, 60)
        self.move(600, 500)

        self.counter = counter
        self.label = QLabel(str(self.counter), self)
        self.label.setStyleSheet(f"color: {color}; font-size: 40px; qproperty-alignment: 'AlignRight';")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        self.counter -= 1
        self.label.setText(str(self.counter))
        if self.counter == 0:
            self.timer.stop()

class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(0, 100)
        self.layout.addWidget(self.spinBox)

        self.comboBox = CustomComboBox(self)
        self.comboBox.addItems(["Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Magenta", "Black"])
        self.layout.addWidget(self.comboBox)

        self.button = QPushButton("Start Countdown", self)
        self.button.clicked.connect(self.start_counter)
        self.layout.addWidget(self.button)


    def start_counter(self):
        color = self.comboBox.currentText()
        counter = self.spinBox.value()
        self.counter_window = Counter_Window(color, counter)
        self.counter_window.show()


app = QApplication(sys.argv)
window = Main_Window()
window.resize(300,300)
#window.move(500,500)
window.setWindowTitle('Task App')

window.show()
sys.exit(app.exec_())
