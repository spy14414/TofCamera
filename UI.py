# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(862, 594)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Grab = QtGui.QPushButton(self.centralwidget)
        self.Grab.setGeometry(QtCore.QRect(620, 540, 101, 31))
        self.Grab.setObjectName(_fromUtf8("Grab"))
        self.Test = QtGui.QPushButton(self.centralwidget)
        self.Test.setGeometry(QtCore.QRect(310, 540, 101, 31))
        self.Test.setObjectName(_fromUtf8("Test"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 141, 91))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.Opencamera = QtGui.QPushButton(self.centralwidget)
        self.Opencamera.setGeometry(QtCore.QRect(160, 540, 101, 31))
        self.Opencamera.setObjectName(_fromUtf8("Opencamera"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 0, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(3, _fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 0, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 0, 69, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 190, 141, 181))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(210, 0, 69, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.label = MyLabel(self.centralwidget)
        #self.label =QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 640, 480))
        self.label.setObjectName(_fromUtf8("label"))

        #self.label.lst_bbox[0] = [[20, 20, 160, 160]]
        self.StopTest = QtGui.QPushButton(self.centralwidget)
        self.StopTest.setGeometry(QtCore.QRect(470, 540, 101, 31))
        self.StopTest.setObjectName(_fromUtf8("StopTest"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #     self.pixel_x = -1  # pixel coordinate
    #     self.pixel_y = -1
        self.x = -1  # 3D coordinate
        self.y = -1
        self.z = -1
        # labelStatus = QtGui.QLabel();
        # labelStatus.setText(self.tr("Mouse Position:"))
        # labelStatus.setFixedWidth(100)
        #
        # self.labelMousePos = QtGui.QLabel();
        # self.labelMousePos.setText(self.tr(""))
        # self.labelMousePos.setFixedWidth(100)
        #
        # self.sBar = self.statusBar()
        # self.sBar.addPermanentWidget(labelStatus)
        # self.sBar.addPermanentWidget(self.labelMousePos)
        # self.labelMousePos.setText(self.label.labelMousePos)
        # self.sBar.showMessage(self.label.sBars)
    #
    # def mouseMoveEvent(self, e):
    #         if 170 < e.x() < 810 and 40 < e.y() < 520:
    #             self.labelMousePos.setText("(" + QtCore.QString.number(e.x() - 170) + "," + QtCore.QString.number(e.y() - 40) + ")")
    #
    # def mousePressEvent(self, e):
    #     if 170 < e.x() < 810 and 40 < e.y() < 520:
    #         str = "(" + QtCore.QString.number(e.x() - 170) + "," + QtCore.QString.number(e.y() - 40) + ")"
    #         if e.button() == QtCore.Qt.LeftButton:
    #             self.sBar.showMessage(self.tr("Mouse Left Button Pressed:") + str)
    #         elif e.button() == QtCore.Qt.RightButton:
    #             self.sBar.showMessage(self.tr("Mouse Right Button Pressed:") + str)
    #         elif e.button() == QtCore.Qt.MidButton:
    #             self.sBar.showMessage(self.tr("Mouse Middle Button Pressed:") + str)
    #         self.pixel_x = e.x() - 170
    #         self.pixel_y = e.y() - 40


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Test.setText(_translate("MainWindow", "检测", None))
        self.Grab.setText(_translate("MainWindow", "抓取", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "2DCamera", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "3DCamera", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.Opencamera.setText(_translate("MainWindow", "打开相机", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "文件", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "sagsj", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "sasasas", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "帮助", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "训练", None))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pixel X", None))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pixel Y", None))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3D X", None))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3D Y", None))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "3D Z", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "设置", None))
        self.label.setText(_translate("MainWindow", "No images to display.", None))
        self.StopTest.setText(_translate("MainWindow", "停止检测", None))


class MyLabel(QtGui.QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.pixel_x = -1  # pixel coordinate
        self.pixel_y = -1
        self.setAlignment(QtCore.Qt.AlignTop)
        self.lst_bbox = []
        self.lst_bbox.append([[0, 0, 0, 0]])
        self.lst_bbox.append(1)
        self.bbox = [0, 0, 0, 0]
    def paintEvent(self, e):
        QtGui.QLabel.paintEvent(self, e)
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.pixel_x > 0 and self.pixel_y > 0:
            self.drawPoints(qp)
        if any(self.lst_bbox[0][0]):
            bbox = self.lst_bbox[0]
            for i, ibbox in enumerate(bbox):
                self.bbox = ibbox
                self.drawRectengle(qp)
        qp.end()
    def drawRectengle(self,qp):
        qp.setPen(QtGui.QPen(QtCore.Qt.blue, 4, QtCore.Qt.SolidLine));
        #qp.setBrush(QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern))
        qp.drawRect(self.bbox[0], self.bbox[1], self.bbox[2], self.bbox[3])
    def drawPoints(self, qp):
        qp.setPen(QtGui.QPen(QtCore.Qt.red, 5))
        qp.drawPoint(self.pixel_x, self.pixel_y)

    # def mouseMoveEvent(self, e):
    #     self.setText("(" + QtCore.QString.number(e.x()) + "," + QtCore.QString.number(e.y()) + ")")

    def mousePressEvent(self, e):
        # str = "(" + QtCore.QString.number(e.x()) + "," + QtCore.QString.number(e.y()) + ")"
        # if e.button() == QtCore.Qt.LeftButton:
        #     self.setText(self.tr("Mouse Left Button Pressed:") + str)
        # elif e.button() == QtCore.Qt.RightButton:
        #     self.setText(self.tr("Mouse Right Button Pressed:") + str) #self.sBar.showMessage
        # elif e.button() == QtCore.Qt.MidButton:
        #     self.setText(self.tr("Mouse Middle Button Pressed:") + str)
        self.clear()
        self.pixel_x = e.x()
        self.pixel_y = e.y()
#end


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        print self.label.lst_bbox[1]
        # self.label.lst_bbox[0] = [[20, 20, 160, 160], [180, 180, 20, 20]]
        # print type(self.label.lst_bbox[0])
        # print self.label.lst_bbox[0][0][0]

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())