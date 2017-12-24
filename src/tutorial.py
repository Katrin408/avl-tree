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
from matplotlib.patches import Ellipse
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

        self.axes = self.mpl_figure.add_subplot(111)

        self.canvas = FigureCanvas(self.mpl_figure)
        self.mplVL.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self, coordinates=True)
        self.addToolBar(self.toolbar)

        self.AddButton.clicked.connect(self.AddButton_OnClick)
        self.LineList.itemClicked.connect(self.LineList_OnClick)


        self.axes.annotate("1",
                  xy=(0.2, 0.2), xycoords='data',
                  xytext=(0.8, 0.8), textcoords='data',
                  size=20, va="center", ha="center",
                  bbox=dict(boxstyle="circle", fc="w"),
                  arrowprops=dict(arrowstyle="->",
                                  connectionstyle="arc3,rad=-0.2",
                                  fc="w"),)



        self.show()

    def AddButton_OnClick(self):

        self.axes.annotate("2",
                           xy=(0.2, 0.2),
                           xytext=(0.2, 0.2), textcoords='data',
                           size=20, va="center", ha="center",
                           bbox=dict(boxstyle="circle", fc="w"),
                           )


        self.canvas.draw()

    def LineList_OnClick(self, item):
        self.canvas.draw()


def run():
    app = QApplication(sys.argv)

    Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()