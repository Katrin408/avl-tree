# -*- coding: utf-8 -*-

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from avl import AVLTree

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
        self.values = set()

        self.show()

    def add_node(self):
        data = self.key.text()
        self.key.clear()
        value = None
        try:
            value = int(data)
        except ValueError:
            print("Wrong node value inserted. %s is not integer" % (data))
            return

        if value not in self.values:
            self.values.add(value)
        else:
            print("%d is already in tree" % value)
            return

        self.tree.add(value)

        # clean up old annotations
        for node in self.nodes:
            node.remove()
        self.nodes.clear()

        new_tree = self.tree.nodes_as_annotations()

        for node, options in new_tree.items():
            if not (node.left or node.right):
                annotation = self.axes.annotate(node.value, **options)
                self.nodes.append(annotation)
                self.canvas.draw()
                continue

            if node.left:
                left_data = options.copy()
                left_node = new_tree.get(node.left)
                if not left_node:
                    continue
                left_data.update(xy=left_node['xytext'])
                annotation = self.axes.annotate(node.value, **left_data)
                self.nodes.append(annotation)
                self.canvas.draw()

            if node.right:
                right_data = options.copy()
                right_node = new_tree.get(node.right)
                if not right_node:
                    continue
                right_data.update(xy=right_node['xytext'])
                annotation = self.axes.annotate(node.value, **right_data)
                self.nodes.append(annotation)
                self.canvas.draw()

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window()
    sys.exit(app.exec_())