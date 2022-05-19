# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QMainWindow, QMenuBar, QPushButton, QSizePolicy,
                               QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1302, 1045)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(80, 90, 421, 421))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        self.gridLayoutWidget.setFont(font)
        self.grid2 = QGridLayout(self.gridLayoutWidget)
        self.grid2.setObjectName(u"grid2")
        self.grid2.setContentsMargins(0, 0, 0, 0)
        self.b1 = QPushButton(self.gridLayoutWidget)
        self.b1.setObjectName(u"b1")
        sizePolicy1.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy1)
        self.b1.setFont(font)

        self.grid2.addWidget(self.b1, 0, 1, 1, 1)

        self.c1 = QPushButton(self.gridLayoutWidget)
        self.c1.setObjectName(u"c1")
        sizePolicy1.setHeightForWidth(self.c1.sizePolicy().hasHeightForWidth())
        self.c1.setSizePolicy(sizePolicy1)
        self.c1.setFont(font)

        self.grid2.addWidget(self.c1, 0, 2, 1, 1)

        self.a1 = QPushButton(self.gridLayoutWidget)
        self.a1.setObjectName(u"a1")
        sizePolicy1.setHeightForWidth(self.a1.sizePolicy().hasHeightForWidth())
        self.a1.setSizePolicy(sizePolicy1)
        self.a1.setFont(font)

        self.grid2.addWidget(self.a1, 0, 0, 1, 1)

        self.a3 = QPushButton(self.gridLayoutWidget)
        self.a3.setObjectName(u"a3")
        sizePolicy1.setHeightForWidth(self.a3.sizePolicy().hasHeightForWidth())
        self.a3.setSizePolicy(sizePolicy1)
        self.a3.setFont(font)

        self.grid2.addWidget(self.a3, 2, 0, 1, 1)

        self.a2 = QPushButton(self.gridLayoutWidget)
        self.a2.setObjectName(u"a2")
        sizePolicy1.setHeightForWidth(self.a2.sizePolicy().hasHeightForWidth())
        self.a2.setSizePolicy(sizePolicy1)
        self.a2.setFont(font)

        self.grid2.addWidget(self.a2, 1, 0, 1, 1)

        self.a4 = QPushButton(self.gridLayoutWidget)
        self.a4.setObjectName(u"a4")
        sizePolicy1.setHeightForWidth(self.a4.sizePolicy().hasHeightForWidth())
        self.a4.setSizePolicy(sizePolicy1)
        self.a4.setFont(font)

        self.grid2.addWidget(self.a4, 3, 0, 1, 1)

        self.b2 = QPushButton(self.gridLayoutWidget)
        self.b2.setObjectName(u"b2")
        sizePolicy1.setHeightForWidth(self.b2.sizePolicy().hasHeightForWidth())
        self.b2.setSizePolicy(sizePolicy1)
        self.b2.setFont(font)

        self.grid2.addWidget(self.b2, 1, 1, 1, 1)

        self.b3 = QPushButton(self.gridLayoutWidget)
        self.b3.setObjectName(u"b3")
        sizePolicy1.setHeightForWidth(self.b3.sizePolicy().hasHeightForWidth())
        self.b3.setSizePolicy(sizePolicy1)
        self.b3.setFont(font)

        self.grid2.addWidget(self.b3, 2, 1, 1, 1)

        self.b4 = QPushButton(self.gridLayoutWidget)
        self.b4.setObjectName(u"b4")
        sizePolicy1.setHeightForWidth(self.b4.sizePolicy().hasHeightForWidth())
        self.b4.setSizePolicy(sizePolicy1)
        self.b4.setFont(font)

        self.grid2.addWidget(self.b4, 3, 1, 1, 1)

        self.c2 = QPushButton(self.gridLayoutWidget)
        self.c2.setObjectName(u"c2")
        sizePolicy1.setHeightForWidth(self.c2.sizePolicy().hasHeightForWidth())
        self.c2.setSizePolicy(sizePolicy1)
        self.c2.setFont(font)

        self.grid2.addWidget(self.c2, 1, 2, 1, 1)

        self.c3 = QPushButton(self.gridLayoutWidget)
        self.c3.setObjectName(u"c3")
        sizePolicy1.setHeightForWidth(self.c3.sizePolicy().hasHeightForWidth())
        self.c3.setSizePolicy(sizePolicy1)
        self.c3.setFont(font)

        self.grid2.addWidget(self.c3, 2, 2, 1, 1)

        self.c4 = QPushButton(self.gridLayoutWidget)
        self.c4.setObjectName(u"c4")
        sizePolicy1.setHeightForWidth(self.c4.sizePolicy().hasHeightForWidth())
        self.c4.setSizePolicy(sizePolicy1)
        self.c4.setFont(font)

        self.grid2.addWidget(self.c4, 3, 2, 1, 1)

        self.d2 = QPushButton(self.gridLayoutWidget)
        self.d2.setObjectName(u"d2")
        sizePolicy1.setHeightForWidth(self.d2.sizePolicy().hasHeightForWidth())
        self.d2.setSizePolicy(sizePolicy1)
        self.d2.setFont(font)

        self.grid2.addWidget(self.d2, 1, 3, 1, 1)

        self.d3 = QPushButton(self.gridLayoutWidget)
        self.d3.setObjectName(u"d3")
        sizePolicy1.setHeightForWidth(self.d3.sizePolicy().hasHeightForWidth())
        self.d3.setSizePolicy(sizePolicy1)
        self.d3.setFont(font)

        self.grid2.addWidget(self.d3, 2, 3, 1, 1)

        self.d4 = QPushButton(self.gridLayoutWidget)
        self.d4.setObjectName(u"d4")
        sizePolicy1.setHeightForWidth(self.d4.sizePolicy().hasHeightForWidth())
        self.d4.setSizePolicy(sizePolicy1)
        self.d4.setFont(font)

        self.grid2.addWidget(self.d4, 3, 3, 1, 1)

        self.d1 = QPushButton(self.gridLayoutWidget)
        self.d1.setObjectName(u"d1")
        sizePolicy1.setHeightForWidth(self.d1.sizePolicy().hasHeightForWidth())
        self.d1.setSizePolicy(sizePolicy1)
        self.d1.setFont(font)

        self.grid2.addWidget(self.d1, 0, 3, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(510, 90, 421, 421))
        sizePolicy1.setHeightForWidth(
            self.gridLayoutWidget_2.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget_2.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget_2.setFont(font)
        self.grid1 = QGridLayout(self.gridLayoutWidget_2)
        self.grid1.setObjectName(u"grid1")
        self.grid1.setContentsMargins(0, 0, 0, 0)
        self.g3 = QPushButton(self.gridLayoutWidget_2)
        self.g3.setObjectName(u"g3")
        sizePolicy1.setHeightForWidth(self.g3.sizePolicy().hasHeightForWidth())
        self.g3.setSizePolicy(sizePolicy1)
        self.g3.setFont(font)

        self.grid1.addWidget(self.g3, 2, 2, 1, 1)

        self.g4 = QPushButton(self.gridLayoutWidget_2)
        self.g4.setObjectName(u"g4")
        sizePolicy1.setHeightForWidth(self.g4.sizePolicy().hasHeightForWidth())
        self.g4.setSizePolicy(sizePolicy1)
        self.g4.setFont(font)

        self.grid1.addWidget(self.g4, 3, 2, 1, 1)

        self.h3 = QPushButton(self.gridLayoutWidget_2)
        self.h3.setObjectName(u"h3")
        sizePolicy1.setHeightForWidth(self.h3.sizePolicy().hasHeightForWidth())
        self.h3.setSizePolicy(sizePolicy1)
        self.h3.setFont(font)

        self.grid1.addWidget(self.h3, 2, 3, 1, 1)

        self.h2 = QPushButton(self.gridLayoutWidget_2)
        self.h2.setObjectName(u"h2")
        sizePolicy1.setHeightForWidth(self.h2.sizePolicy().hasHeightForWidth())
        self.h2.setSizePolicy(sizePolicy1)
        self.h2.setFont(font)

        self.grid1.addWidget(self.h2, 1, 3, 1, 1)

        self.h4 = QPushButton(self.gridLayoutWidget_2)
        self.h4.setObjectName(u"h4")
        sizePolicy1.setHeightForWidth(self.h4.sizePolicy().hasHeightForWidth())
        self.h4.setSizePolicy(sizePolicy1)
        self.h4.setFont(font)

        self.grid1.addWidget(self.h4, 3, 3, 1, 1)

        self.e3 = QPushButton(self.gridLayoutWidget_2)
        self.e3.setObjectName(u"e3")
        sizePolicy1.setHeightForWidth(self.e3.sizePolicy().hasHeightForWidth())
        self.e3.setSizePolicy(sizePolicy1)
        self.e3.setFont(font)

        self.grid1.addWidget(self.e3, 2, 0, 1, 1)

        self.e2 = QPushButton(self.gridLayoutWidget_2)
        self.e2.setObjectName(u"e2")
        sizePolicy1.setHeightForWidth(self.e2.sizePolicy().hasHeightForWidth())
        self.e2.setSizePolicy(sizePolicy1)
        self.e2.setFont(font)

        self.grid1.addWidget(self.e2, 1, 0, 1, 1)

        self.g1 = QPushButton(self.gridLayoutWidget_2)
        self.g1.setObjectName(u"g1")
        sizePolicy1.setHeightForWidth(self.g1.sizePolicy().hasHeightForWidth())
        self.g1.setSizePolicy(sizePolicy1)
        self.g1.setFont(font)

        self.grid1.addWidget(self.g1, 0, 2, 1, 1)

        self.f2 = QPushButton(self.gridLayoutWidget_2)
        self.f2.setObjectName(u"f2")
        sizePolicy1.setHeightForWidth(self.f2.sizePolicy().hasHeightForWidth())
        self.f2.setSizePolicy(sizePolicy1)
        self.f2.setFont(font)

        self.grid1.addWidget(self.f2, 1, 1, 1, 1)

        self.f3 = QPushButton(self.gridLayoutWidget_2)
        self.f3.setObjectName(u"f3")
        sizePolicy1.setHeightForWidth(self.f3.sizePolicy().hasHeightForWidth())
        self.f3.setSizePolicy(sizePolicy1)
        self.f3.setFont(font)

        self.grid1.addWidget(self.f3, 2, 1, 1, 1)

        self.f4 = QPushButton(self.gridLayoutWidget_2)
        self.f4.setObjectName(u"f4")
        sizePolicy1.setHeightForWidth(self.f4.sizePolicy().hasHeightForWidth())
        self.f4.setSizePolicy(sizePolicy1)
        self.f4.setFont(font)

        self.grid1.addWidget(self.f4, 3, 1, 1, 1)

        self.g2 = QPushButton(self.gridLayoutWidget_2)
        self.g2.setObjectName(u"g2")
        sizePolicy1.setHeightForWidth(self.g2.sizePolicy().hasHeightForWidth())
        self.g2.setSizePolicy(sizePolicy1)
        self.g2.setFont(font)

        self.grid1.addWidget(self.g2, 1, 2, 1, 1)

        self.e4 = QPushButton(self.gridLayoutWidget_2)
        self.e4.setObjectName(u"e4")
        sizePolicy1.setHeightForWidth(self.e4.sizePolicy().hasHeightForWidth())
        self.e4.setSizePolicy(sizePolicy1)
        self.e4.setFont(font)
        self.e4.setFocusPolicy(Qt.StrongFocus)
        self.e4.setAutoFillBackground(False)
        self.e4.setCheckable(False)

        self.grid1.addWidget(self.e4, 3, 0, 1, 1)

        self.h1 = QPushButton(self.gridLayoutWidget_2)
        self.h1.setObjectName(u"h1")
        sizePolicy1.setHeightForWidth(self.h1.sizePolicy().hasHeightForWidth())
        self.h1.setSizePolicy(sizePolicy1)
        self.h1.setFont(font)

        self.grid1.addWidget(self.h1, 0, 3, 1, 1)

        self.f1 = QPushButton(self.gridLayoutWidget_2)
        self.f1.setObjectName(u"f1")
        sizePolicy1.setHeightForWidth(self.f1.sizePolicy().hasHeightForWidth())
        self.f1.setSizePolicy(sizePolicy1)
        self.f1.setFont(font)

        self.grid1.addWidget(self.f1, 0, 1, 1, 1)

        self.e1 = QPushButton(self.gridLayoutWidget_2)
        self.e1.setObjectName(u"e1")
        sizePolicy1.setHeightForWidth(self.e1.sizePolicy().hasHeightForWidth())
        self.e1.setSizePolicy(sizePolicy1)
        self.e1.setFont(font)

        self.grid1.addWidget(self.e1, 0, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(80, 520, 421, 421))
        sizePolicy1.setHeightForWidth(
            self.gridLayoutWidget_3.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget_3.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget_3.setFont(font)
        self.grid3 = QGridLayout(self.gridLayoutWidget_3)
        self.grid3.setObjectName(u"grid3")
        self.grid3.setContentsMargins(0, 0, 0, 0)
        self.b5 = QPushButton(self.gridLayoutWidget_3)
        self.b5.setObjectName(u"b5")
        sizePolicy1.setHeightForWidth(self.b5.sizePolicy().hasHeightForWidth())
        self.b5.setSizePolicy(sizePolicy1)
        self.b5.setFont(font)

        self.grid3.addWidget(self.b5, 0, 1, 1, 1)

        self.c5 = QPushButton(self.gridLayoutWidget_3)
        self.c5.setObjectName(u"c5")
        sizePolicy1.setHeightForWidth(self.c5.sizePolicy().hasHeightForWidth())
        self.c5.setSizePolicy(sizePolicy1)
        self.c5.setFont(font)

        self.grid3.addWidget(self.c5, 0, 2, 1, 1)

        self.a5 = QPushButton(self.gridLayoutWidget_3)
        self.a5.setObjectName(u"a5")
        sizePolicy1.setHeightForWidth(self.a5.sizePolicy().hasHeightForWidth())
        self.a5.setSizePolicy(sizePolicy1)
        self.a5.setFont(font)

        self.grid3.addWidget(self.a5, 0, 0, 1, 1)

        self.a7 = QPushButton(self.gridLayoutWidget_3)
        self.a7.setObjectName(u"a7")
        sizePolicy1.setHeightForWidth(self.a7.sizePolicy().hasHeightForWidth())
        self.a7.setSizePolicy(sizePolicy1)
        self.a7.setFont(font)

        self.grid3.addWidget(self.a7, 2, 0, 1, 1)

        self.a6 = QPushButton(self.gridLayoutWidget_3)
        self.a6.setObjectName(u"a6")
        sizePolicy1.setHeightForWidth(self.a6.sizePolicy().hasHeightForWidth())
        self.a6.setSizePolicy(sizePolicy1)
        self.a6.setFont(font)

        self.grid3.addWidget(self.a6, 1, 0, 1, 1)

        self.a8 = QPushButton(self.gridLayoutWidget_3)
        self.a8.setObjectName(u"a8")
        sizePolicy1.setHeightForWidth(self.a8.sizePolicy().hasHeightForWidth())
        self.a8.setSizePolicy(sizePolicy1)
        self.a8.setFont(font)

        self.grid3.addWidget(self.a8, 3, 0, 1, 1)

        self.b6 = QPushButton(self.gridLayoutWidget_3)
        self.b6.setObjectName(u"b6")
        sizePolicy1.setHeightForWidth(self.b6.sizePolicy().hasHeightForWidth())
        self.b6.setSizePolicy(sizePolicy1)
        self.b6.setFont(font)

        self.grid3.addWidget(self.b6, 1, 1, 1, 1)

        self.b7 = QPushButton(self.gridLayoutWidget_3)
        self.b7.setObjectName(u"b7")
        sizePolicy1.setHeightForWidth(self.b7.sizePolicy().hasHeightForWidth())
        self.b7.setSizePolicy(sizePolicy1)
        self.b7.setFont(font)

        self.grid3.addWidget(self.b7, 2, 1, 1, 1)

        self.b8 = QPushButton(self.gridLayoutWidget_3)
        self.b8.setObjectName(u"b8")
        sizePolicy1.setHeightForWidth(self.b8.sizePolicy().hasHeightForWidth())
        self.b8.setSizePolicy(sizePolicy1)
        self.b8.setFont(font)

        self.grid3.addWidget(self.b8, 3, 1, 1, 1)

        self.c6 = QPushButton(self.gridLayoutWidget_3)
        self.c6.setObjectName(u"c6")
        sizePolicy1.setHeightForWidth(self.c6.sizePolicy().hasHeightForWidth())
        self.c6.setSizePolicy(sizePolicy1)
        self.c6.setFont(font)

        self.grid3.addWidget(self.c6, 1, 2, 1, 1)

        self.c7 = QPushButton(self.gridLayoutWidget_3)
        self.c7.setObjectName(u"c7")
        sizePolicy1.setHeightForWidth(self.c7.sizePolicy().hasHeightForWidth())
        self.c7.setSizePolicy(sizePolicy1)
        self.c7.setFont(font)

        self.grid3.addWidget(self.c7, 2, 2, 1, 1)

        self.c8 = QPushButton(self.gridLayoutWidget_3)
        self.c8.setObjectName(u"c8")
        sizePolicy1.setHeightForWidth(self.c8.sizePolicy().hasHeightForWidth())
        self.c8.setSizePolicy(sizePolicy1)
        self.c8.setFont(font)

        self.grid3.addWidget(self.c8, 3, 2, 1, 1)

        self.d6 = QPushButton(self.gridLayoutWidget_3)
        self.d6.setObjectName(u"d6")
        sizePolicy1.setHeightForWidth(self.d6.sizePolicy().hasHeightForWidth())
        self.d6.setSizePolicy(sizePolicy1)
        self.d6.setFont(font)

        self.grid3.addWidget(self.d6, 1, 3, 1, 1)

        self.d7 = QPushButton(self.gridLayoutWidget_3)
        self.d7.setObjectName(u"d7")
        sizePolicy1.setHeightForWidth(self.d7.sizePolicy().hasHeightForWidth())
        self.d7.setSizePolicy(sizePolicy1)
        self.d7.setFont(font)

        self.grid3.addWidget(self.d7, 2, 3, 1, 1)

        self.d8 = QPushButton(self.gridLayoutWidget_3)
        self.d8.setObjectName(u"d8")
        sizePolicy1.setHeightForWidth(self.d8.sizePolicy().hasHeightForWidth())
        self.d8.setSizePolicy(sizePolicy1)
        self.d8.setFont(font)

        self.grid3.addWidget(self.d8, 3, 3, 1, 1)

        self.d5 = QPushButton(self.gridLayoutWidget_3)
        self.d5.setObjectName(u"d5")
        sizePolicy1.setHeightForWidth(self.d5.sizePolicy().hasHeightForWidth())
        self.d5.setSizePolicy(sizePolicy1)
        self.d5.setFont(font)

        self.grid3.addWidget(self.d5, 0, 3, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(510, 520, 421, 421))
        sizePolicy1.setHeightForWidth(
            self.gridLayoutWidget_4.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget_4.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget_4.setFont(font)
        self.grid4 = QGridLayout(self.gridLayoutWidget_4)
        self.grid4.setObjectName(u"grid4")
        self.grid4.setContentsMargins(0, 0, 0, 0)
        self.f5 = QPushButton(self.gridLayoutWidget_4)
        self.f5.setObjectName(u"f5")
        sizePolicy1.setHeightForWidth(self.f5.sizePolicy().hasHeightForWidth())
        self.f5.setSizePolicy(sizePolicy1)
        self.f5.setFont(font)

        self.grid4.addWidget(self.f5, 0, 1, 1, 1)

        self.g5 = QPushButton(self.gridLayoutWidget_4)
        self.g5.setObjectName(u"g5")
        sizePolicy1.setHeightForWidth(self.g5.sizePolicy().hasHeightForWidth())
        self.g5.setSizePolicy(sizePolicy1)
        self.g5.setFont(font)

        self.grid4.addWidget(self.g5, 0, 2, 1, 1)

        self.e5 = QPushButton(self.gridLayoutWidget_4)
        self.e5.setObjectName(u"e5")
        sizePolicy1.setHeightForWidth(self.e5.sizePolicy().hasHeightForWidth())
        self.e5.setSizePolicy(sizePolicy1)
        self.e5.setFont(font)

        self.grid4.addWidget(self.e5, 0, 0, 1, 1)

        self.e7 = QPushButton(self.gridLayoutWidget_4)
        self.e7.setObjectName(u"e7")
        sizePolicy1.setHeightForWidth(self.e7.sizePolicy().hasHeightForWidth())
        self.e7.setSizePolicy(sizePolicy1)
        self.e7.setFont(font)

        self.grid4.addWidget(self.e7, 2, 0, 1, 1)

        self.e6 = QPushButton(self.gridLayoutWidget_4)
        self.e6.setObjectName(u"e6")
        sizePolicy1.setHeightForWidth(self.e6.sizePolicy().hasHeightForWidth())
        self.e6.setSizePolicy(sizePolicy1)
        self.e6.setFont(font)

        self.grid4.addWidget(self.e6, 1, 0, 1, 1)

        self.e8 = QPushButton(self.gridLayoutWidget_4)
        self.e8.setObjectName(u"e8")
        sizePolicy1.setHeightForWidth(self.e8.sizePolicy().hasHeightForWidth())
        self.e8.setSizePolicy(sizePolicy1)
        self.e8.setFont(font)

        self.grid4.addWidget(self.e8, 3, 0, 1, 1)

        self.h5 = QPushButton(self.gridLayoutWidget_4)
        self.h5.setObjectName(u"h5")
        sizePolicy1.setHeightForWidth(self.h5.sizePolicy().hasHeightForWidth())
        self.h5.setSizePolicy(sizePolicy1)
        self.h5.setFont(font)

        self.grid4.addWidget(self.h5, 0, 3, 1, 1)

        self.f6 = QPushButton(self.gridLayoutWidget_4)
        self.f6.setObjectName(u"f6")
        sizePolicy1.setHeightForWidth(self.f6.sizePolicy().hasHeightForWidth())
        self.f6.setSizePolicy(sizePolicy1)
        self.f6.setFont(font)

        self.grid4.addWidget(self.f6, 1, 1, 1, 1)

        self.f7 = QPushButton(self.gridLayoutWidget_4)
        self.f7.setObjectName(u"f7")
        sizePolicy1.setHeightForWidth(self.f7.sizePolicy().hasHeightForWidth())
        self.f7.setSizePolicy(sizePolicy1)
        self.f7.setFont(font)

        self.grid4.addWidget(self.f7, 2, 1, 1, 1)

        self.f8 = QPushButton(self.gridLayoutWidget_4)
        self.f8.setObjectName(u"f8")
        sizePolicy1.setHeightForWidth(self.f8.sizePolicy().hasHeightForWidth())
        self.f8.setSizePolicy(sizePolicy1)
        self.f8.setFont(font)

        self.grid4.addWidget(self.f8, 3, 1, 1, 1)

        self.g6 = QPushButton(self.gridLayoutWidget_4)
        self.g6.setObjectName(u"g6")
        sizePolicy1.setHeightForWidth(self.g6.sizePolicy().hasHeightForWidth())
        self.g6.setSizePolicy(sizePolicy1)
        self.g6.setFont(font)

        self.grid4.addWidget(self.g6, 1, 2, 1, 1)

        self.g7 = QPushButton(self.gridLayoutWidget_4)
        self.g7.setObjectName(u"g7")
        sizePolicy1.setHeightForWidth(self.g7.sizePolicy().hasHeightForWidth())
        self.g7.setSizePolicy(sizePolicy1)
        self.g7.setFont(font)

        self.grid4.addWidget(self.g7, 2, 2, 1, 1)

        self.g8 = QPushButton(self.gridLayoutWidget_4)
        self.g8.setObjectName(u"g8")
        sizePolicy1.setHeightForWidth(self.g8.sizePolicy().hasHeightForWidth())
        self.g8.setSizePolicy(sizePolicy1)
        self.g8.setFont(font)

        self.grid4.addWidget(self.g8, 3, 2, 1, 1)

        self.h6 = QPushButton(self.gridLayoutWidget_4)
        self.h6.setObjectName(u"h6")
        sizePolicy1.setHeightForWidth(self.h6.sizePolicy().hasHeightForWidth())
        self.h6.setSizePolicy(sizePolicy1)
        self.h6.setFont(font)

        self.grid4.addWidget(self.h6, 1, 3, 1, 1)

        self.h7 = QPushButton(self.gridLayoutWidget_4)
        self.h7.setObjectName(u"h7")
        sizePolicy1.setHeightForWidth(self.h7.sizePolicy().hasHeightForWidth())
        self.h7.setSizePolicy(sizePolicy1)
        self.h7.setFont(font)

        self.grid4.addWidget(self.h7, 2, 3, 1, 1)

        self.h8 = QPushButton(self.gridLayoutWidget_4)
        self.h8.setObjectName(u"h8")
        sizePolicy1.setHeightForWidth(self.h8.sizePolicy().hasHeightForWidth())
        self.h8.setSizePolicy(sizePolicy1)
        self.h8.setFont(font)

        self.grid4.addWidget(self.h8, 3, 3, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 60, 841, 31))
        font1 = QFont()
        font1.setBold(True)
        self.horizontalLayoutWidget.setFont(font1)
        self.horizontalCoordinate_upper = QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalCoordinate_upper.setObjectName(
            u"horizontalCoordinate_upper")
        self.horizontalCoordinate_upper.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label_4)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label_3)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label_5)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label_7)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label_6)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_upper.addWidget(self.label_8)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(
            u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(80, 940, 841, 31))
        self.horizontalLayoutWidget_3.setFont(font1)
        self.horizontalCoordinate_down = QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalCoordinate_down.setObjectName(
            u"horizontalCoordinate_down")
        self.horizontalCoordinate_down.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_9)

        self.label_10 = QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_10)

        self.label_11 = QLabel(self.horizontalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_11)

        self.label_12 = QLabel(self.horizontalLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_12)

        self.label_13 = QLabel(self.horizontalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_13)

        self.label_14 = QLabel(self.horizontalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_14)

        self.label_15 = QLabel(self.horizontalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_15)

        self.label_16 = QLabel(self.horizontalLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalCoordinate_down.addWidget(self.label_16)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(930, 90, 31, 841))
        self.verticalLayoutWidget.setFont(font2)
        self.verticalCoordinate_rignt = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalCoordinate_rignt.setObjectName(
            u"verticalCoordinate_rignt")
        self.verticalCoordinate_rignt.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_17)

        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_18)

        self.label_19 = QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_19)

        self.label_20 = QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_20)

        self.label_21 = QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_21)

        self.label_22 = QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_22)

        self.label_23 = QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_23)

        self.label_24 = QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_rignt.addWidget(self.label_24)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(50, 100, 31, 841))
        self.verticalLayoutWidget_2.setFont(font2)
        self.verticalCoordinate_left = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalCoordinate_left.setObjectName(u"verticalCoordinate_left")
        self.verticalCoordinate_left.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_25)

        self.label_26 = QLabel(self.verticalLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_26)

        self.label_27 = QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_27)

        self.label_28 = QLabel(self.verticalLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_28)

        self.label_29 = QLabel(self.verticalLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_29)

        self.label_30 = QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_30)

        self.label_31 = QLabel(self.verticalLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_31)

        self.label_32 = QLabel(self.verticalLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalCoordinate_left.addWidget(self.label_32)

        self.GameInfoLabel = QLabel(self.centralwidget)
        self.GameInfoLabel.setObjectName(u"GameInfoLabel")
        self.GameInfoLabel.setGeometry(QRect(990, 430, 271, 71))
        font3 = QFont()
        font3.setPointSize(16)
        self.GameInfoLabel.setFont(font3)
        self.GameInfoLabel.setAlignment(Qt.AlignCenter)
        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(1020, 520, 211, 51))
        self.reset_button.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1302, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.b1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.b2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.b3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.b4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f3.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g2.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e4.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e1.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.b5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.a8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.b6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.b7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.b8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.c8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.d5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.e8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h5.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.f8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.g8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h6.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h7.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.h8.setText(QCoreApplication.translate(
            "MainWindow", u"Button", None))
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"B", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"C", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"D", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"E", None))
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"F", None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"G", None))
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u"H", None))
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", u"B", None))
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"C", None))
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", u"D", None))
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"E", None))
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", u"F", None))
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", u"G", None))
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", u"H", None))
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", u"3", None))
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", u"4", None))
        self.label_21.setText(
            QCoreApplication.translate("MainWindow", u"5", None))
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", u"6", None))
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", u"7", None))
        self.label_24.setText(
            QCoreApplication.translate("MainWindow", u"8", None))
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        self.label_26.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", u"3", None))
        self.label_28.setText(
            QCoreApplication.translate("MainWindow", u"4", None))
        self.label_29.setText(
            QCoreApplication.translate("MainWindow", u"5", None))
        self.label_30.setText(
            QCoreApplication.translate("MainWindow", u"6", None))
        self.label_31.setText(
            QCoreApplication.translate("MainWindow", u"7", None))
        self.label_32.setText(
            QCoreApplication.translate("MainWindow", u"8", None))
        self.GameInfoLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Black Gose First", None))
        self.reset_button.setText(QCoreApplication.translate(
            "MainWindow", u"Reset Game", None))
    # retranslateUi
