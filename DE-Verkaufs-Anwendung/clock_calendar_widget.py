from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QPainter, QPen
import math

class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        center_x = self.width() / 2
        center_y = self.height() / 2
        painter.translate(center_x, center_y)
        painter.scale(self.width() / 200.0, self.height() / 200.0)
        # Zeichnen von Uhrmarkierungen
        painter.setPen(QPen(Qt.black, 2))
        for i in range(12):
            angle = i * 30 * math.pi / 180
            x1 = int(90 * math.cos(angle))
            y1 = int(90 * math.sin(angle))
            x2 = int(100 * math.cos(angle))
            y2 = int(100 * math.sin(angle))
            painter.drawLine(x1, y1, x2, y2)

        current_time = QDateTime.currentDateTime().time()

        # Sekundenzeiger (einer Uhr)
        sec_angle = current_time.second() * 6 * math.pi / 180
        painter.setPen(QPen(Qt.red, 1))
        painter.drawLine(0, 0, int(80 * math.cos(sec_angle)), int(80 * math.sin(sec_angle)))

        # Minutenzeiger
        min_angle = current_time.minute() * 6 * math.pi / 180
        painter.setPen(QPen(Qt.darkBlue, 3))
        painter.drawLine(0, 0, int(60 * math.cos(min_angle)), int(60 * math.sin(min_angle)))

        # Stundenzeiger
        hour_angle = (current_time.hour() % 12 + current_time.minute() / 60) * 30 * math.pi / 180
        painter.setPen(QPen(Qt.black, 5))
        painter.drawLine(0, 0, int(40 * math.cos(hour_angle)), int(40 * math.sin(hour_angle)))
