# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_add_old.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OWindow(object):
    def setupUi(self, OWindow):
        OWindow.setObjectName("OWindow")
        OWindow.resize(570, 316)
        OWindow.setMinimumSize(QtCore.QSize(570, 316))
        OWindow.setMaximumSize(QtCore.QSize(570, 316))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("online.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(OWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.header_old = QtWidgets.QLabel(self.centralwidget)
        self.header_old.setGeometry(QtCore.QRect(340, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.header_old.setFont(font)
        self.header_old.setObjectName("header_old")
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(20, 250, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Lotus")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(120, 250, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Lotus")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.question_box = QtWidgets.QComboBox(self.centralwidget)
        self.question_box.setGeometry(QtCore.QRect(12, 80, 531, 31))
        font = QtGui.QFont()
        font.setFamily("B Zar")
        font.setPointSize(9)
        self.question_box.setFont(font)
        self.question_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.question_box.setObjectName("question_box")
        self.labelButton2 = QtWidgets.QLabel(self.centralwidget)
        self.labelButton2.setGeometry(QtCore.QRect(190, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelButton2.setFont(font)
        self.labelButton2.setText("")
        self.labelButton2.setObjectName("labelButton2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.labelButton4 = QtWidgets.QLabel(self.centralwidget)
        self.labelButton4.setGeometry(QtCore.QRect(360, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelButton4.setFont(font)
        self.labelButton4.setText("")
        self.labelButton4.setObjectName("labelButton4")
        self.labelButton3 = QtWidgets.QLabel(self.centralwidget)
        self.labelButton3.setGeometry(QtCore.QRect(10, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelButton3.setFont(font)
        self.labelButton3.setText("")
        self.labelButton3.setObjectName("labelButton3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.labelButton1 = QtWidgets.QLabel(self.centralwidget)
        self.labelButton1.setGeometry(QtCore.QRect(370, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelButton1.setFont(font)
        self.labelButton1.setText("")
        self.labelButton1.setObjectName("labelButton1")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.labelButton5 = QtWidgets.QLabel(self.centralwidget)
        self.labelButton5.setGeometry(QtCore.QRect(190, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelButton5.setFont(font)
        self.labelButton5.setText("")
        self.labelButton5.setObjectName("labelButton5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        OWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OWindow)
        self.statusbar.setObjectName("statusbar")
        OWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OWindow)
        QtCore.QMetaObject.connectSlotsByName(OWindow)

    def retranslateUi(self, OWindow):
        _translate = QtCore.QCoreApplication.translate
        OWindow.setWindowTitle(_translate("OWindow", "بارگذاری نظرسنجی"))
        self.label.setText(_translate("OWindow", "سوال:"))
        self.header_old.setText(_translate("OWindow", "بارگذاری نظرسنجی های قبلی"))
        self.ok_button.setText(_translate("OWindow", "تایید"))
        self.cancel_button.setText(_translate("OWindow", "انصراف"))
        self.label_7.setText(_translate("OWindow", "گزینه سه:"))
        self.label_4.setText(_translate("OWindow", "گزینه چهار:"))
        self.label_3.setText(_translate("OWindow", "گزینه یک:"))
        self.label_5.setText(_translate("OWindow", "گزینه دو:"))
        self.label_6.setText(_translate("OWindow", "گزینه پنج:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OWindow = QtWidgets.QMainWindow()
    ui = Ui_OWindow()
    ui.setupUi(OWindow)
    OWindow.show()
    sys.exit(app.exec_())

