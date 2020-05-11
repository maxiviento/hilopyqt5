# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\dPython\ejemplo_hilos\window_lite.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 600)
        MainWindow.setMinimumSize(QtCore.QSize(480, 600))
        MainWindow.setMaximumSize(QtCore.QSize(480, 760))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow, #scrollAreaWidgetContents {\n"
"background-color: #03B0B3;\n"
"}\n"
"QTabWidget QTabBar{\n"
"background-color: #373738;\n"
"height: 30px;\n"
"}\n"
"QTabWidget QTabBar::tab{\n"
"text-align: left;\n"
"background-color: #136ba2;\n"
"border-style: 1px rgb(67, 67, 67);\n"
"height: 30px;\n"
"width: 130px;\n"
"color: #136ba2;\n"
"padding: 0px 5px 0px 5px;\n"
"}\n"
"QTabWidget QTabBar::tab:selected{\n"
"background-color: #03F2F2;\n"
"font-weight: bold;\n"
"color: #4B1A70;\n"
"}\n"
"QTabWidget QTabBar::tab:!selected{\n"
"background-color:#027A8C;\n"
"color: #fff;\n"
"}\n"
"QTabWidget QTabBar::tab:hover{\n"
"background-color: #03F2F2;\n"
"color: #4B1A70;\n"
"}\n"
"QTabWidget #tab_auth, #tab_env, #tab_pars{\n"
"background-color: #03F2F2;\n"
"color: #4B1A70;\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #962455;\n"
"  color:  #fff;\n"
"  font-size: 14px\n"
"    }\n"
"QPushButton:disabled {\n"
"background-color:#5BB1B3;\n"
"color:#8FC9C9\n"
"}\n"
"QLineEdit, QPlainTextEdit {\n"
"    border: 1px solid #962455;\n"
"    padding: 0 8px;\n"
"    background-color: #D5FFF5;\n"
"    selection-background-color: #fff;\n"
"    }\n"
"\n"
"QLineEdit:onfocus, QPlainTextEdit {\n"
"    background-color: #fff;\n"
"    }\n"
"\n"
"QPlainTextEdit:disabled {\n"
"border: 1px solid #5BB1B3;\n"
"}\n"
"QLineEdit:disabled {\n"
"border: 1px solid #5BB1B3;\n"
"}\n"
"QLabel, QRadioButton, QCheckBox {\n"
"color: #4B1A70;\n"
"font-size: 14px\n"
"}\n"
"QGroupBox {\n"
"    border: 1px solid;\n"
"    border-color: #5BB1B3;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px 260px 5px 15px;\n"
"    background-color: #43A5AB;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"#rbtn_verificarwa:disabled, #rbtn_xcontactos:disabled, #rbtn_xenlace:disabled, #lbl_salutacion:disabled, #lbl_objetivo:disabled{\n"
"color: #5BB1B3\n"
"}")
        MainWindow.setAnimated(True)
        self.widget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 480, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(480, 760))
        self.scrollAreaWidgetContents.setBaseSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lbl_logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_logo.setGeometry(QtCore.QRect(30, 15, 191, 70))
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("../Yudi/img/logo.png"))
        self.lbl_logo.setScaledContents(False)
        self.lbl_logo.setWordWrap(False)
        self.lbl_logo.setObjectName("lbl_logo")
        self.btn_parsear = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_parsear.setEnabled(True)
        self.btn_parsear.setGeometry(QtCore.QRect(30, 150, 360, 60))
        self.btn_parsear.setStyleSheet("")
        self.btn_parsear.setObjectName("btn_parsear")
        self.progressBar_pars = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_pars.setGeometry(QtCore.QRect(30, 250, 360, 35))
        self.progressBar_pars.setProperty("value", 0)
        self.progressBar_pars.setTextVisible(True)
        self.progressBar_pars.setInvertedAppearance(False)
        self.progressBar_pars.setObjectName("progressBar_pars")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 330, 360, 121))
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YUDI DESKTOP"))
        self.btn_parsear.setText(_translate("MainWindow", "INICIAR LECTURA"))
