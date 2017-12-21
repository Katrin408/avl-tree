# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:09:33 2017

@author: KandK
"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

form_class = uic.loadUiType("mainwindow4.ui")[0]


class Window(QMainWindow, form_class):
    mpl_figure = Figure()
    lines_pic = {}
    lines = {}

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.home()

    def home(self):
        self.axes = self.mpl_figure.add_axes([0.1, 0.1, 0.8, 0.8])
        # self.axes = self.mpl_figure.add_subplot(111)

        self.canvas = FigureCanvas(self.mpl_figure)
        self.mplVL.addWidget(self.canvas)
        self.canvas.draw()

        # self.toolbar = NavigationToolbar(self.canvas, self.MPLWindow, coordinates = True)
        # self.mplVL.addWidget(self.toolbar)

        self.toolbar = NavigationToolbar(self.canvas, self, coordinates=True)
        self.addToolBar(self.toolbar)

        self.AddButton.clicked.connect(self.AddButton_OnClick)
        self.LineList.itemClicked.connect(self.LineList_OnClick)

        self.show()

    def AddButton_OnClick(self):
        x1_c = self.x1_lineEdit.text()
        y1_c = self.y1_lineEdit.text()
        x2_c = self.x2_lineEdit.text()
        y2_c = self.y2_lineEdit.text()

        key = '([' + x1_c + ';' + y1_c + '],[' + x2_c + ';' + y2_c + '])'
        x_coord = [int(x1_c), int(x2_c)]
        y_coord = [int(y1_c), int(y2_c)]

        self.lines[key] = [x_coord, y_coord]

        temp_list = self.axes.plot(x_coord, y_coord, color='blue');

        for line in temp_list:
            self.lines_pic[key] = line

        self.LineList.addItem(key)
        self.canvas.draw()

    def LineList_OnClick(self, item):
        key = item.text()
        for i, line in self.lines_pic.items():
            line.set_color('blue')
        self.lines_pic[key].set_color('red')

        self.canvas.draw()


def run():
    app = QApplication(sys.argv)

    GUI = Window()
    # sys.exit(app.exec_())
    app.exec_()


if __name__ == "__main__":
    run()