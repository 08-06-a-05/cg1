# Form implementation generated from reading ui file '.\kg2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, main_window, scene_objects):
        self.main_window = main_window
        self.scene_objects = scene_objects
        self.main_window.setObjectName("self.main_window")
        self.main_window.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(parent=self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.resultView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.resultView.setGeometry(QtCore.QRect(40, 30, 581, 321))
        self.resultView.setObjectName("resultView")
        self.rotate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.rotate_button.setGeometry(QtCore.QRect(480, 440, 140, 31))
        self.rotate_button.setObjectName("rotate_button")
        self.add_x_value = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.add_x_value.setGeometry(QtCore.QRect(100, 440, 70, 31))
        self.add_x_value.setText("")
        self.add_x_value.setObjectName("add_x_value")
        self.add_y_value = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.add_y_value.setGeometry(QtCore.QRect(190, 440, 70, 31))
        self.add_y_value.setText("")
        self.add_y_value.setObjectName("add_y_value")
        self.xValueLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.xValueLabel.setGeometry(QtCore.QRect(120, 420, 30, 16))
        self.xValueLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xValueLabel.setObjectName("xValueLabel")
        self.xValueLabel_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.xValueLabel_2.setGeometry(QtCore.QRect(210, 420, 30, 16))
        self.xValueLabel_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xValueLabel_2.setObjectName("xValueLabel_2")
        self.move_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.move_button.setGeometry(QtCore.QRect(480, 380, 140, 31))
        self.move_button.setObjectName("move_button")
        self.scale_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.scale_button.setGeometry(QtCore.QRect(480, 500, 161, 31))
        self.scale_button.setObjectName("scale_button")
        self.big_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.big_text.setGeometry(QtCore.QRect(40, 360, 280, 26))
        self.big_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.big_text.setObjectName("xValueLabel_5")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 390, 210, 26))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.add_x_value_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.add_x_value_2.setGeometry(QtCore.QRect(310, 380, 80, 31))
        self.add_x_value_2.setText("")
        self.add_x_value_2.setObjectName("add_x_value_2")
        self.add_y_value_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.add_y_value_2.setGeometry(QtCore.QRect(400, 380, 80, 31))
        self.add_y_value_2.setText("")
        self.add_y_value_2.setObjectName("add_y_value_2")
        self.xValueLabel_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.xValueLabel_3.setGeometry(QtCore.QRect(330, 360, 30, 16))
        self.xValueLabel_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xValueLabel_3.setObjectName("xValueLabel_3")
        self.xValueLabel_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.xValueLabel_4.setGeometry(QtCore.QRect(420, 360, 30, 16))
        self.xValueLabel_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xValueLabel_4.setObjectName("xValueLabel_4")
        self.xValueLabel_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.xValueLabel_6.setGeometry(QtCore.QRect(380, 420, 51, 16))
        self.xValueLabel_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xValueLabel_6.setObjectName("xValueLabel_6")
        self.add_x_value_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.add_x_value_3.setGeometry(QtCore.QRect(350, 440, 120, 31))
        self.add_x_value_3.setText("")
        self.add_x_value_3.setObjectName("add_x_value_3")
        self.xValueLabel_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.xValueLabel_7.setGeometry(QtCore.QRect(340, 480, 140, 16))
        self.xValueLabel_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xValueLabel_7.setObjectName("xValueLabel_7")
        self.add_x_value_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.add_x_value_4.setGeometry(QtCore.QRect(350, 500, 120, 31))
        self.add_x_value_4.setText("")
        self.add_x_value_4.setObjectName("add_x_value_4")
        self.main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self.main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 22))
        self.menubar.setObjectName("menubar")
        self.main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("self.main_window", "Лабораторная работа №2"))
        self.rotate_button.setText(_translate("self.main_window", "Вращать"))
        self.xValueLabel.setText(_translate("self.main_window", "x"))
        self.xValueLabel_2.setText(_translate("self.main_window", "y"))
        self.move_button.setText(_translate("self.main_window", "Перенести"))
        self.scale_button.setText(_translate("self.main_window", "Масштабировать"))
        self.big_text.setText(_translate("self.main_window", "Операции над фигурой"))
        self.label.setText(_translate("self.main_window", "Центр операции"))
        self.xValueLabel_3.setText(_translate("self.main_window", "x"))
        self.xValueLabel_4.setText(_translate("self.main_window", "y"))
        self.xValueLabel_6.setText(_translate("self.main_window", "Угол"))
        self.xValueLabel_7.setText(_translate("self.main_window", "Масштаб"))
