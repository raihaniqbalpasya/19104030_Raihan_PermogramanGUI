# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tugas1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.setEnabled(True)
        Calendar.resize(763, 437)
        Calendar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Calendar.setMouseTracking(False)
        Calendar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Calendar.setToolTip("")
        Calendar.setAccessibleName("")
        Calendar.setAccessibleDescription("")
        Calendar.setLayoutDirection(QtCore.Qt.LeftToRight)
        Calendar.setAutoFillBackground(False)
        Calendar.setStyleSheet("")
        Calendar.setWindowFilePath("")
        self.label = QtWidgets.QLabel(Calendar)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(Calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 30, 341, 211))
        self.calendarWidget.setSelectedDate(QtCore.QDate(2017, 5, 30))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_2 = QtWidgets.QLabel(Calendar)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 47, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Calendar)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Calendar)
        self.label_4.setGeometry(QtCore.QRect(30, 340, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Calendar)
        self.label_5.setGeometry(QtCore.QRect(30, 370, 81, 21))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(Calendar)
        self.dateEdit.setGeometry(QtCore.QRect(180, 310, 151, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setDate(QtCore.QDate(1900, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Calendar)
        self.dateEdit_2.setGeometry(QtCore.QRect(180, 340, 151, 22))
        self.dateEdit_2.setDate(QtCore.QDate(2017, 5, 30))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_3 = QtWidgets.QDateEdit(Calendar)
        self.dateEdit_3.setGeometry(QtCore.QRect(180, 370, 151, 22))
        self.dateEdit_3.setDate(QtCore.QDate(3000, 1, 1))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_6 = QtWidgets.QLabel(Calendar)
        self.label_6.setGeometry(QtCore.QRect(380, 10, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Calendar)
        self.label_7.setGeometry(QtCore.QRect(390, 50, 47, 21))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Calendar)
        self.comboBox.setGeometry(QtCore.QRect(490, 50, 251, 20))
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Calendar)
        self.comboBox_2.setGeometry(QtCore.QRect(490, 90, 251, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Calendar)
        self.comboBox_3.setGeometry(QtCore.QRect(490, 130, 251, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.checkBox = QtWidgets.QCheckBox(Calendar)
        self.checkBox.setGeometry(QtCore.QRect(390, 160, 70, 21))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Calendar)
        self.checkBox_2.setGeometry(QtCore.QRect(650, 160, 91, 21))
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.comboBox_4 = QtWidgets.QComboBox(Calendar)
        self.comboBox_4.setGeometry(QtCore.QRect(490, 190, 251, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(Calendar)
        self.comboBox_5.setGeometry(QtCore.QRect(490, 230, 251, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.label_8 = QtWidgets.QLabel(Calendar)
        self.label_8.setGeometry(QtCore.QRect(390, 190, 91, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Calendar)
        self.label_9.setGeometry(QtCore.QRect(390, 130, 91, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Calendar)
        self.label_10.setGeometry(QtCore.QRect(390, 90, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Calendar)
        self.label_11.setGeometry(QtCore.QRect(390, 230, 91, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Calendar)
        self.label_12.setGeometry(QtCore.QRect(380, 270, 71, 31))
        self.label_12.setObjectName("label_12")
        self.comboBox_6 = QtWidgets.QComboBox(Calendar)
        self.comboBox_6.setGeometry(QtCore.QRect(570, 310, 171, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(Calendar)
        self.comboBox_7.setGeometry(QtCore.QRect(570, 340, 171, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(Calendar)
        self.comboBox_8.setGeometry(QtCore.QRect(570, 370, 171, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.label_13 = QtWidgets.QLabel(Calendar)
        self.label_13.setGeometry(QtCore.QRect(390, 310, 81, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Calendar)
        self.label_14.setGeometry(QtCore.QRect(390, 340, 81, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Calendar)
        self.label_15.setGeometry(QtCore.QRect(390, 370, 81, 21))
        self.label_15.setObjectName("label_15")
        self.checkBox_3 = QtWidgets.QCheckBox(Calendar)
        self.checkBox_3.setGeometry(QtCore.QRect(390, 400, 111, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Calendar)
        self.checkBox_4.setGeometry(QtCore.QRect(660, 400, 81, 21))
        self.checkBox_4.setObjectName("checkBox_4")

        self.retranslateUi(Calendar)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Calendar Widget"))
        self.label.setText(_translate("Calendar", "Preview"))
        self.label_2.setText(_translate("Calendar", "Dates"))
        self.label_3.setText(_translate("Calendar", "Minimum Date:"))
        self.label_4.setText(_translate("Calendar", "Current Date:"))
        self.label_5.setText(_translate("Calendar", "Maximum Date:"))
        self.dateEdit.setDisplayFormat(_translate("Calendar", "MMM d yyyy"))
        self.dateEdit_2.setDisplayFormat(_translate("Calendar", "MMM d yyyy"))
        self.dateEdit_3.setDisplayFormat(_translate("Calendar", "MMM d yyyy"))
        self.label_6.setText(_translate("Calendar", "General Options"))
        self.label_7.setText(_translate("Calendar", "Locale"))
        self.comboBox.setItemText(0, _translate("Calendar", "German/Germany"))
        self.comboBox_2.setItemText(0, _translate("Calendar", "Sunday"))
        self.comboBox_2.setItemText(1, _translate("Calendar", "Monday"))
        self.comboBox_2.setItemText(2, _translate("Calendar", "Tuesday"))
        self.comboBox_2.setItemText(3, _translate("Calendar", "Wednesday"))
        self.comboBox_2.setItemText(4, _translate("Calendar", "Thursday"))
        self.comboBox_2.setItemText(5, _translate("Calendar", "Friday"))
        self.comboBox_2.setItemText(6, _translate("Calendar", "Saturday"))
        self.comboBox_3.setItemText(0, _translate("Calendar", "Single Selection"))
        self.checkBox.setText(_translate("Calendar", "Grid"))
        self.checkBox_2.setText(_translate("Calendar", "Navigation bar"))
        self.comboBox_4.setItemText(0, _translate("Calendar", "Short day names"))
        self.comboBox_5.setItemText(0, _translate("Calendar", "ISO week numbers"))
        self.label_8.setText(_translate("Calendar", "Horizontal header:"))
        self.label_9.setText(_translate("Calendar", "Selection header:"))
        self.label_10.setText(_translate("Calendar", "Week starts on:"))
        self.label_11.setText(_translate("Calendar", "Vertical header:"))
        self.label_12.setText(_translate("Calendar", "Text Formats"))
        self.comboBox_6.setItemText(0, _translate("Calendar", "Black"))
        self.comboBox_7.setItemText(0, _translate("Calendar", "Red"))
        self.comboBox_8.setItemText(0, _translate("Calendar", "Bold"))
        self.label_13.setText(_translate("Calendar", "Weekday color:"))
        self.label_14.setText(_translate("Calendar", "Weekend color:"))
        self.label_15.setText(_translate("Calendar", "Header text:"))
        self.checkBox_3.setText(_translate("Calendar", "First Friday in blue"))
        self.checkBox_4.setText(_translate("Calendar", "May 1 in red"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calendar = QtWidgets.QWidget()
    ui = Ui_Calendar()
    ui.setupUi(Calendar)
    Calendar.show()
    sys.exit(app.exec_())
