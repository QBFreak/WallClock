#!/usr/bin/python3

"""
Python Wall Clock

This program creates a full-screen wall-clock that can be controlled with an
external infrared remote control.

Author: Jason Hill
Website: qbfreak.net
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QWidget, QLabel, QPushButton, QApplication
from PyQt5.QtCore import *

class StretchedLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def resizeEvent(self, evt):
        font = self.font()
        rect = self.contentsRect()

        if self.text() == "":
            return

        fontSize = 1

        while True:
            font.setPixelSize( fontSize )
            r = QFontMetrics(font).boundingRect(self.text())
            if r.height() <= rect.height() and r.width() <= rect.width():
                fontSize += 1
            else:
                break
            self.setFont(font)

        # Tweak the size back down a little...
        fontSize = max(12, fontSize - 10)
        font.setPixelSize( fontSize )
        self.setFont(font)

class WallClock(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.clock = StretchedLabel('--:--:--', self, font=QFont("FreeMono", 12, QFont.Bold))
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setStyleSheet("QLabel {color: #00CC00;}")
        self.clock.mousePressEvent = self.quit

        self.layout = QGridLayout()
        self.layout.addWidget(self.clock, 0, 0)

        self.setLayout(self.layout)
        self.setWindowTitle('Clock')
        self.showFullScreen()

        self.curr_time = QTime(00,00,00)

        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(1000)
        self.skipTimer = 2

    def time(self):
        if self.skipTimer > 0:
            self.skipTimer -= 1
            return

        self.clock.setText(QTime.currentTime().toString())

    def quit(self, event):
        exit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget {background: black;}")
    ex = WallClock()
    sys.exit(app.exec_())
