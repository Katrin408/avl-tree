# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:09:33 2017

@author: KandK
"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from avl import AVLTree


from drawtree import draw_bst

form_class = uic.loadUiType("mainwindow.ui")[0]


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

        self.add_button.clicked.connect(self.add_node)

        self.tree = AVLTree()
        self.nodes = []

        self.show()

    def add_node(self):
        data = self.key.text()
        self.key.clear()
        value = None
        try:
            value = int(data)
        except ValueError:
            print("Wrong node value inserted. Expected int, got %s" % (type(value)))
            return

        self.tree.add(value)

        # clean up old annotations
        for node in self.nodes:
            node.remove()
        self.nodes.clear()

        new_tree = self.tree.nodes_as_annotations()

        for node in new_tree:
            value = node[0]
            options = node[1]
            annotation = self.axes.annotate(value, **options)
            self.nodes.append(annotation)

        self.canvas.draw()

def run():
    app = QApplication(sys.argv)

    Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()