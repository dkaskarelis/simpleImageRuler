# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simpleImageRuler.ui'
#
# Created: Mon Nov 25 19:29:14 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(70, 0))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.toolButtonCal = QtGui.QToolButton(self.groupBox)
        self.toolButtonCal.setGeometry(QtCore.QRect(20, 20, 32, 32))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/cal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonCal.setIcon(icon)
        self.toolButtonCal.setIconSize(QtCore.QSize(32, 32))
        self.toolButtonCal.setObjectName("toolButtonCal")
        self.toolButtonLine = QtGui.QToolButton(self.groupBox)
        self.toolButtonLine.setGeometry(QtCore.QRect(20, 100, 32, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonLine.setIcon(icon1)
        self.toolButtonLine.setIconSize(QtCore.QSize(32, 32))
        self.toolButtonLine.setObjectName("toolButtonLine")
        self.toolButtonPath = QtGui.QToolButton(self.groupBox)
        self.toolButtonPath.setGeometry(QtCore.QRect(20, 140, 32, 32))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/path.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonPath.setIcon(icon2)
        self.toolButtonPath.setIconSize(QtCore.QSize(32, 32))
        self.toolButtonPath.setObjectName("toolButtonPath")
        self.toolButtonClear = QtGui.QToolButton(self.groupBox)
        self.toolButtonClear.setGeometry(QtCore.QRect(20, 470, 32, 32))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonClear.setIcon(icon3)
        self.toolButtonClear.setObjectName("toolButtonClear")
        self.toolButtonNeutral = QtGui.QToolButton(self.groupBox)
        self.toolButtonNeutral.setGeometry(QtCore.QRect(20, 60, 32, 32))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/neutral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonNeutral.setIcon(icon4)
        self.toolButtonNeutral.setIconSize(QtCore.QSize(32, 32))
        self.toolButtonNeutral.setObjectName("toolButtonNeutral")
        self.toolButtonBlack = QtGui.QToolButton(self.groupBox)
        self.toolButtonBlack.setGeometry(QtCore.QRect(20, 210, 32, 32))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonBlack.setIcon(icon5)
        self.toolButtonBlack.setObjectName("toolButtonBlack")
        self.toolButtonWhite = QtGui.QToolButton(self.groupBox)
        self.toolButtonWhite.setGeometry(QtCore.QRect(20, 250, 32, 32))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonWhite.setIcon(icon6)
        self.toolButtonWhite.setObjectName("toolButtonWhite")
        self.toolButtonYellow = QtGui.QToolButton(self.groupBox)
        self.toolButtonYellow.setGeometry(QtCore.QRect(20, 290, 32, 32))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonYellow.setIcon(icon7)
        self.toolButtonYellow.setObjectName("toolButtonYellow")
        self.toolButtonRed = QtGui.QToolButton(self.groupBox)
        self.toolButtonRed.setGeometry(QtCore.QRect(20, 330, 32, 32))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonRed.setIcon(icon8)
        self.toolButtonRed.setObjectName("toolButtonRed")
        self.toolButtonZoomIn = QtGui.QToolButton(self.groupBox)
        self.toolButtonZoomIn.setGeometry(QtCore.QRect(20, 380, 32, 32))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonZoomIn.setIcon(icon9)
        self.toolButtonZoomIn.setObjectName("toolButtonZoomIn")
        self.toolButtonZoomOut = QtGui.QToolButton(self.groupBox)
        self.toolButtonZoomOut.setGeometry(QtCore.QRect(20, 420, 32, 32))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonZoomOut.setIcon(icon10)
        self.toolButtonZoomOut.setObjectName("toolButtonZoomOut")
        self.horizontalLayout.addWidget(self.groupBox)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(140, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtGui.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.menuDatei.addAction(self.actionOpen)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SIR - Simple Image Ruler", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCal.setToolTip(QtGui.QApplication.translate("MainWindow", "calibrate", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCal.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonLine.setToolTip(QtGui.QApplication.translate("MainWindow", "line", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonLine.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonPath.setToolTip(QtGui.QApplication.translate("MainWindow", "path", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonPath.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonClear.setToolTip(QtGui.QApplication.translate("MainWindow", "delete", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonClear.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonNeutral.setToolTip(QtGui.QApplication.translate("MainWindow", "neutral", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonNeutral.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonBlack.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonWhite.setToolTip(QtGui.QApplication.translate("MainWindow", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonWhite.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonYellow.setToolTip(QtGui.QApplication.translate("MainWindow", "yellow", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonYellow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonRed.setToolTip(QtGui.QApplication.translate("MainWindow", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonRed.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonZoomIn.setToolTip(QtGui.QApplication.translate("MainWindow", "zoom in", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonZoomIn.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonZoomOut.setToolTip(QtGui.QApplication.translate("MainWindow", "zoom out", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonZoomOut.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatei.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBeenden.setText(QtGui.QApplication.translate("MainWindow", "Beenden", None, QtGui.QApplication.UnicodeUTF8))

