# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'embeddeddialog.ui'
#
# Created: Wed May 28 15:07:08 2008
#      by: PyQt4 UI code generator 4.4.3-snapshot-20080526
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_embeddedDialog(object):
    def setupUi(self, embeddedDialog):
        embeddedDialog.setObjectName("embeddedDialog")
        embeddedDialog.resize(407,134)
        self.formLayout = QFormLayout(embeddedDialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(embeddedDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0,QFormLayout.LabelRole,self.label)
        self.layoutDirection = QComboBox(embeddedDialog)
        self.layoutDirection.setObjectName("layoutDirection")
        self.formLayout.setWidget(0,QFormLayout.FieldRole,self.layoutDirection)
        self.label_2 = QLabel(embeddedDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1,QFormLayout.LabelRole,self.label_2)
        self.fontComboBox = QFontComboBox(embeddedDialog)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout.setWidget(1,QFormLayout.FieldRole,self.fontComboBox)
        self.label_3 = QLabel(embeddedDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2,QFormLayout.LabelRole,self.label_3)
        self.style = QComboBox(embeddedDialog)
        self.style.setObjectName("style")
        self.formLayout.setWidget(2,QFormLayout.FieldRole,self.style)
        self.label_4 = QLabel(embeddedDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3,QFormLayout.LabelRole,self.label_4)
        self.spacing = QSlider(embeddedDialog)
        self.spacing.setOrientation(QtCore.Qt.Horizontal)
        self.spacing.setObjectName("spacing")
        self.formLayout.setWidget(3,QFormLayout.FieldRole,self.spacing)
        self.label.setBuddy(self.layoutDirection)
        self.label_2.setBuddy(self.fontComboBox)
        self.label_3.setBuddy(self.style)
        self.label_4.setBuddy(self.spacing)

        self.retranslateUi(embeddedDialog)
        QtCore.QMetaObject.connectSlotsByName(embeddedDialog)

    def retranslateUi(self, embeddedDialog):
        embeddedDialog.setWindowTitle(QApplication.translate("embeddedDialog", "Embedded Dialog", None))
        self.label.setText(QApplication.translate("embeddedDialog", "Layout Direction:", None))
        self.layoutDirection.addItem(QApplication.translate("embeddedDialog", "Left to Right", None))
        self.layoutDirection.addItem(QApplication.translate("embeddedDialog", "Right to Left", None))
        self.label_2.setText(QApplication.translate("embeddedDialog", "Select Font:", None))
        self.label_3.setText(QApplication.translate("embeddedDialog", "Style:", None))
        self.label_4.setText(QApplication.translate("embeddedDialog", "Layout spacing:", None))

