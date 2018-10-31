from PySide2 import QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class DemoScene(QGraphicsScene):
    def drawItems(self, painter, items, options, widget):
        for item, option in zip(items, options):
            painter.save()
            painter.setMatrix(item.sceneMatrix(), True)
            item.paint(painter, option, widget)
            painter.restore()
