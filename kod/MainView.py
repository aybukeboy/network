# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aybuk\Desktop\deneme.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget2.setGeometry(QtCore.QRect(10, 20, 631, 541))
        self.tabWidget2.setObjectName("tabWidget2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labelPortServer = QtWidgets.QLabel(self.tab_2)
        self.labelPortServer.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.labelPortServer.setObjectName("labelPortServer")
        self.textEdit_Port_Server = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_Port_Server.setGeometry(QtCore.QRect(50, 20, 104, 21))
        self.textEdit_Port_Server.setObjectName("textEdit_Port_Server")
        self.labelIncoming = QtWidgets.QLabel(self.tab_2)
        self.labelIncoming.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.labelIncoming.setObjectName("labelIncoming")
        self.textBrowserIncoming_Server = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowserIncoming_Server.setGeometry(QtCore.QRect(10, 240, 601, 91))
        self.textBrowserIncoming_Server.setObjectName("textBrowserIncoming_Server")
        self.labelOutgoing = QtWidgets.QLabel(self.tab_2)
        self.labelOutgoing.setGeometry(QtCore.QRect(10, 360, 47, 13))
        self.labelOutgoing.setObjectName("labelOutgoing")
        self.textBrowserOutgoing_Server = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowserOutgoing_Server.setGeometry(QtCore.QRect(10, 380, 601, 111))
        self.textBrowserOutgoing_Server.setObjectName("textBrowserOutgoing_Server")
        self.textEditDataServer = QtWidgets.QTextEdit(self.tab_2)
        self.textEditDataServer.setGeometry(QtCore.QRect(260, 30, 351, 141))
        self.textEditDataServer.setObjectName("textEditDataServer")
        self.labelData = QtWidgets.QLabel(self.tab_2)
        self.labelData.setGeometry(QtCore.QRect(260, 10, 47, 13))
        self.labelData.setObjectName("labelData")
        self.ButonBaslat = QtWidgets.QPushButton(self.tab_2)
        self.ButonBaslat.setGeometry(QtCore.QRect(10, 60, 61, 23))
        self.ButonBaslat.setObjectName("ButonBaslat")
        self.ButonDurdur_Server = QtWidgets.QPushButton(self.tab_2)
        self.ButonDurdur_Server.setGeometry(QtCore.QRect(80, 60, 71, 23))
        self.ButonDurdur_Server.setObjectName("ButonDurdur_Server")
        self.ButonSendData_Server = QtWidgets.QPushButton(self.tab_2)
        self.ButonSendData_Server.setGeometry(QtCore.QRect(440, 190, 61, 23))
        self.ButonSendData_Server.setObjectName("ButonSendData_Server")
        self.labelSaniye_2 = QtWidgets.QLabel(self.tab_2)
        self.labelSaniye_2.setGeometry(QtCore.QRect(410, 190, 21, 20))
        self.labelSaniye_2.setObjectName("labelSaniye_2")
        self.textEdit_ServerPeriyot = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_ServerPeriyot.setGeometry(QtCore.QRect(350, 190, 51, 21))
        self.textEdit_ServerPeriyot.setObjectName("textEdit_ServerPeriyot")
        self.checkBoxPeriyodikServer = QtWidgets.QCheckBox(self.tab_2)
        self.checkBoxPeriyodikServer.setGeometry(QtCore.QRect(260, 190, 81, 17))
        self.checkBoxPeriyodikServer.setObjectName("checkBoxPeriyodikServer")
        self.ButonSendingStop_Server = QtWidgets.QPushButton(self.tab_2)
        self.ButonSendingStop_Server.setGeometry(QtCore.QRect(510, 190, 101, 23))
        self.ButonSendingStop_Server.setObjectName("ButonSendingStop_Server")
        self.labelSayiClient = QtWidgets.QLabel(self.tab_2)
        self.labelSayiClient.setGeometry(QtCore.QRect(10, 110, 121, 20))
        self.labelSayiClient.setObjectName("labelSayiClient")
        self.textBrowserClientSayisi = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowserClientSayisi.setEnabled(False)
        self.textBrowserClientSayisi.setGeometry(QtCore.QRect(140, 110, 71, 21))
        self.textBrowserClientSayisi.setObjectName("textBrowserClientSayisi")
        self.tabWidget2.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.labelOutgoing_2 = QtWidgets.QLabel(self.tab)
        self.labelOutgoing_2.setGeometry(QtCore.QRect(10, 370, 47, 13))
        self.labelOutgoing_2.setObjectName("labelOutgoing_2")
        self.labelPort_2 = QtWidgets.QLabel(self.tab)
        self.labelPort_2.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.labelPort_2.setObjectName("labelPort_2")
        self.textBrowserOutgoing_Client = QtWidgets.QTextBrowser(self.tab)
        self.textBrowserOutgoing_Client.setGeometry(QtCore.QRect(10, 390, 601, 101))
        self.textBrowserOutgoing_Client.setObjectName("textBrowserOutgoing_Client")
        self.labelIncoming_2 = QtWidgets.QLabel(self.tab)
        self.labelIncoming_2.setGeometry(QtCore.QRect(10, 230, 47, 13))
        self.labelIncoming_2.setObjectName("labelIncoming_2")
        self.textEdit_Port_Client = QtWidgets.QTextEdit(self.tab)
        self.textEdit_Port_Client.setGeometry(QtCore.QRect(60, 20, 104, 21))
        self.textEdit_Port_Client.setObjectName("textEdit_Port_Client")
        self.textBrowserIncoming_Client = QtWidgets.QTextBrowser(self.tab)
        self.textBrowserIncoming_Client.setGeometry(QtCore.QRect(10, 250, 601, 91))
        self.textBrowserIncoming_Client.setObjectName("textBrowserIncoming_Client")
        self.textEditData_Client = QtWidgets.QTextEdit(self.tab)
        self.textEditData_Client.setGeometry(QtCore.QRect(280, 30, 331, 161))
        self.textEditData_Client.setObjectName("textEditData_Client")
        self.labelData_2 = QtWidgets.QLabel(self.tab)
        self.labelData_2.setGeometry(QtCore.QRect(280, 10, 47, 13))
        self.labelData_2.setObjectName("labelData_2")
        self.labelIP = QtWidgets.QLabel(self.tab)
        self.labelIP.setGeometry(QtCore.QRect(10, 60, 21, 16))
        self.labelIP.setObjectName("labelIP")
        self.textEditClientIP = QtWidgets.QTextEdit(self.tab)
        self.textEditClientIP.setGeometry(QtCore.QRect(60, 60, 101, 21))
        self.textEditClientIP.setObjectName("textEditClientIP")
        self.ButonBaglanClient = QtWidgets.QPushButton(self.tab)
        self.ButonBaglanClient.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.ButonBaglanClient.setObjectName("ButonBaglanClient")
        self.ButonSendData_Client = QtWidgets.QPushButton(self.tab)
        self.ButonSendData_Client.setGeometry(QtCore.QRect(460, 210, 61, 23))
        self.ButonSendData_Client.setObjectName("ButonSendData_Client")
        self.ButonBaglantKes_Client = QtWidgets.QPushButton(self.tab)
        self.ButonBaglantKes_Client.setGeometry(QtCore.QRect(90, 100, 71, 23))
        self.ButonBaglantKes_Client.setObjectName("ButonBaglantKes_Client")
        self.checkBoxClientDurum = QtWidgets.QCheckBox(self.tab)
        self.checkBoxClientDurum.setGeometry(QtCore.QRect(10, 140, 70, 17))
        self.checkBoxClientDurum.setObjectName("checkBoxClientDurum")
        self.checkBoxPeriyodik_Client = QtWidgets.QCheckBox(self.tab)
        self.checkBoxPeriyodik_Client.setGeometry(QtCore.QRect(280, 210, 71, 17))
        self.checkBoxPeriyodik_Client.setObjectName("checkBoxPeriyodik_Client")
        self.textEditClientPeriyot = QtWidgets.QTextEdit(self.tab)
        self.textEditClientPeriyot.setGeometry(QtCore.QRect(370, 210, 51, 21))
        self.textEditClientPeriyot.setObjectName("textEditClientPeriyot")
        self.labelSaniye = QtWidgets.QLabel(self.tab)
        self.labelSaniye.setGeometry(QtCore.QRect(430, 210, 21, 20))
        self.labelSaniye.setObjectName("labelSaniye")
        self.ButonSendingStop_Client = QtWidgets.QPushButton(self.tab)
        self.ButonSendingStop_Client.setGeometry(QtCore.QRect(524, 210, 81, 23))
        self.ButonSendingStop_Client.setObjectName("ButonSendingStop_Client")
        self.tabWidget2.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_IP_UDP = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_IP_UDP.setGeometry(QtCore.QRect(60, 100, 101, 21))
        self.textEdit_IP_UDP.setObjectName("textEdit_IP_UDP")
        self.labelData_3 = QtWidgets.QLabel(self.tab_3)
        self.labelData_3.setGeometry(QtCore.QRect(280, 20, 47, 13))
        self.labelData_3.setObjectName("labelData_3")
        self.textEditUDPPeriyot = QtWidgets.QTextEdit(self.tab_3)
        self.textEditUDPPeriyot.setGeometry(QtCore.QRect(370, 220, 51, 21))
        self.textEditUDPPeriyot.setObjectName("textEditUDPPeriyot")
        self.ButonSendData_UDP = QtWidgets.QPushButton(self.tab_3)
        self.ButonSendData_UDP.setGeometry(QtCore.QRect(460, 220, 61, 23))
        self.ButonSendData_UDP.setObjectName("ButonSendData_UDP")
        self.textBrowserOutgoingUDP = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowserOutgoingUDP.setGeometry(QtCore.QRect(10, 400, 601, 91))
        self.textBrowserOutgoingUDP.setObjectName("textBrowserOutgoingUDP")
        self.labelIP_2 = QtWidgets.QLabel(self.tab_3)
        self.labelIP_2.setGeometry(QtCore.QRect(10, 100, 21, 16))
        self.labelIP_2.setObjectName("labelIP_2")
        self.labelSaniye_3 = QtWidgets.QLabel(self.tab_3)
        self.labelSaniye_3.setGeometry(QtCore.QRect(430, 220, 21, 20))
        self.labelSaniye_3.setObjectName("labelSaniye_3")
        self.ButonBaslaUDP = QtWidgets.QPushButton(self.tab_3)
        self.ButonBaslaUDP.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.ButonBaslaUDP.setObjectName("ButonBaslaUDP")
        self.ButonDurdurUDP = QtWidgets.QPushButton(self.tab_3)
        self.ButonDurdurUDP.setGeometry(QtCore.QRect(90, 140, 71, 23))
        self.ButonDurdurUDP.setObjectName("ButonDurdurUDP")
        self.labelIncoming_3 = QtWidgets.QLabel(self.tab_3)
        self.labelIncoming_3.setGeometry(QtCore.QRect(10, 240, 47, 13))
        self.labelIncoming_3.setObjectName("labelIncoming_3")
        self.labelPort_3 = QtWidgets.QLabel(self.tab_3)
        self.labelPort_3.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.labelPort_3.setObjectName("labelPort_3")
        self.ButonSendingStop_UDP = QtWidgets.QPushButton(self.tab_3)
        self.ButonSendingStop_UDP.setGeometry(QtCore.QRect(524, 220, 81, 23))
        self.ButonSendingStop_UDP.setObjectName("ButonSendingStop_UDP")
        self.textEditData_UDP = QtWidgets.QTextEdit(self.tab_3)
        self.textEditData_UDP.setGeometry(QtCore.QRect(280, 40, 331, 161))
        self.textEditData_UDP.setObjectName("textEditData_UDP")
        self.labelOutgoing_3 = QtWidgets.QLabel(self.tab_3)
        self.labelOutgoing_3.setGeometry(QtCore.QRect(10, 380, 47, 13))
        self.labelOutgoing_3.setObjectName("labelOutgoing_3")
        self.textEdit_ListenPort_UDP = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_ListenPort_UDP.setGeometry(QtCore.QRect(80, 20, 81, 21))
        self.textEdit_ListenPort_UDP.setObjectName("textEdit_ListenPort_UDP")
        self.checkBoxPeriyodik_UDP = QtWidgets.QCheckBox(self.tab_3)
        self.checkBoxPeriyodik_UDP.setGeometry(QtCore.QRect(280, 220, 81, 17))
        self.checkBoxPeriyodik_UDP.setObjectName("checkBoxPeriyodik_UDP")
        self.textBrowserIncomingUDP = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowserIncomingUDP.setGeometry(QtCore.QRect(10, 260, 601, 91))
        self.textBrowserIncomingUDP.setObjectName("textBrowserIncomingUDP")
        self.textEdit_SendPort_UDP = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_SendPort_UDP.setGeometry(QtCore.QRect(80, 60, 81, 21))
        self.textEdit_SendPort_UDP.setObjectName("textEdit_SendPort_UDP")
        self.labelPort_4 = QtWidgets.QLabel(self.tab_3)
        self.labelPort_4.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.labelPort_4.setObjectName("labelPort_4")
        self.tabWidget2.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COMM-22"))
        self.labelPortServer.setText(_translate("MainWindow", "Port"))
        self.textEdit_Port_Server.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4044</p></body></html>"))
        self.labelIncoming.setText(_translate("MainWindow", "Incoming"))
        self.labelOutgoing.setText(_translate("MainWindow", "Outgoing"))
        self.labelData.setText(_translate("MainWindow", "Data"))
        self.ButonBaslat.setText(_translate("MainWindow", "Start"))
        self.ButonDurdur_Server.setText(_translate("MainWindow", "Stop"))
        self.ButonSendData_Server.setText(_translate("MainWindow", "Send"))
        self.labelSaniye_2.setText(_translate("MainWindow", "sn"))
        self.textEdit_ServerPeriyot.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.checkBoxPeriyodikServer.setText(_translate("MainWindow", "Periodically"))
        self.ButonSendingStop_Server.setText(_translate("MainWindow", "Stop Sending"))
        self.labelSayiClient.setText(_translate("MainWindow", "Connected Client Count:"))
        self.textBrowserClientSayisi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_2), _translate("MainWindow", "TCP Server"))
        self.labelOutgoing_2.setText(_translate("MainWindow", "Outgoing"))
        self.labelPort_2.setText(_translate("MainWindow", "Port"))
        self.labelIncoming_2.setText(_translate("MainWindow", "Incoming"))
        self.textEdit_Port_Client.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4044</p></body></html>"))
        self.labelData_2.setText(_translate("MainWindow", "Data"))
        self.labelIP.setText(_translate("MainWindow", "IP"))
        self.textEditClientIP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">127.0.0.1</p></body></html>"))
        self.ButonBaglanClient.setText(_translate("MainWindow", "Connect"))
        self.ButonSendData_Client.setText(_translate("MainWindow", "Send"))
        self.ButonBaglantKes_Client.setText(_translate("MainWindow", "Disconnect"))
        self.checkBoxClientDurum.setText(_translate("MainWindow", "Connected"))
        self.checkBoxPeriyodik_Client.setText(_translate("MainWindow", "Periodically"))
        self.textEditClientPeriyot.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.labelSaniye.setText(_translate("MainWindow", "sn"))
        self.ButonSendingStop_Client.setText(_translate("MainWindow", "Stop Sending"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab), _translate("MainWindow", "TCP Client"))
        self.textEdit_IP_UDP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">127.0.0.1</p></body></html>"))
        self.labelData_3.setText(_translate("MainWindow", "Data"))
        self.textEditUDPPeriyot.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.ButonSendData_UDP.setText(_translate("MainWindow", "Send"))
        self.labelIP_2.setText(_translate("MainWindow", "IP"))
        self.labelSaniye_3.setText(_translate("MainWindow", "sn"))
        self.ButonBaslaUDP.setText(_translate("MainWindow", "Open"))
        self.ButonDurdurUDP.setText(_translate("MainWindow", "Close"))
        self.labelIncoming_3.setText(_translate("MainWindow", "Incoming"))
        self.labelPort_3.setText(_translate("MainWindow", "Listen Port"))
        self.ButonSendingStop_UDP.setText(_translate("MainWindow", "Stop Sending"))
        self.labelOutgoing_3.setText(_translate("MainWindow", "Outgoing"))
        self.textEdit_ListenPort_UDP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4044</p></body></html>"))
        self.checkBoxPeriyodik_UDP.setText(_translate("MainWindow", "Periodically"))
        self.textEdit_SendPort_UDP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4043</p></body></html>"))
        self.labelPort_4.setText(_translate("MainWindow", "Send Port"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_3), _translate("MainWindow", "UDP"))


if __name__ == "__main__":
    import sys
    sys.path.append(r'C:\Users\aybuk\PycharmProjects\Deneme')
    from MainViewController import MainViewController

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    mainViewController = MainViewController(ui)
    MainWindow.show()
    sys.exit(app.exec_())