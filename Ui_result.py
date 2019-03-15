# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PYTHON\Study_Case\result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 # นำเข้า libraly sqlite3
class ResultWindow(object):
    ##### ตัวเเปร แบบ global ประกาศใต้ Class เวลาเรียกใช้ self.ชื่อตัวเเปร
    a = []
    save_stat = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 966)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(430, 50, 75, 31))
        self.btnEdit.setObjectName("btnEdit")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(430, 170, 75, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(430, 10, 75, 31))
        self.btnAdd.setObjectName("btnAdd")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(430, 90, 75, 31))
        self.btnDelete.setObjectName("btnDelete")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(430, 130, 75, 31))
        self.btnSave.setObjectName("btnSave")
        self.cmbStage = QtWidgets.QComboBox(self.centralwidget)
        self.cmbStage.setGeometry(QtCore.QRect(230, 171, 171, 31))
        self.cmbStage.setObjectName("cmbStage")
        self.cmbSwimer = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSwimer.setGeometry(QtCore.QRect(230, 10, 171, 31))
        self.cmbSwimer.setObjectName("cmbSwimer")
        self.cmbDis = QtWidgets.QComboBox(self.centralwidget)
        self.cmbDis.setGeometry(QtCore.QRect(230, 50, 171, 31))
        self.cmbDis.setObjectName("cmbDis")
        self.cmbStroke = QtWidgets.QComboBox(self.centralwidget)
        self.cmbStroke.setGeometry(QtCore.QRect(230, 90, 171, 31))
        self.cmbStroke.setObjectName("cmbStroke")
        self.cmbGender = QtWidgets.QComboBox(self.centralwidget)
        self.cmbGender.setGeometry(QtCore.QRect(230, 130, 171, 31))
        self.cmbGender.setObjectName("cmbGender")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 260, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 220, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 170, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 300, 691, 661))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.txtTime = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTime.setGeometry(QtCore.QRect(230, 210, 171, 31))
        self.txtTime.setObjectName("txtTime")
        self.txtPlace = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPlace.setGeometry(QtCore.QRect(230, 250, 171, 31))
        self.txtPlace.setObjectName("txtPlace")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Load() # เรียกฟังชั่น Load เมื่อเปิดโปรแกรม
        ################  อีเว้นต่าง อยากให้รันฟังกชั่นไหนตอนเปิด เอามาใส่ที่นี่  ###############
        self.btnAdd.clicked.connect(self.btnAdd_click)
        self.btnCancel.clicked.connect(self.btnCancel_click)
        self.btnEdit.clicked.connect(self.btnEdit_click)
        self.tableWidget.cellClicked.connect(self.call_cmb)
        ####################################
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Result"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Swimer"))
        self.label_2.setText(_translate("MainWindow", "Distance"))
        self.label_3.setText(_translate("MainWindow", "Place"))
        self.label_4.setText(_translate("MainWindow", "Time"))
        self.label_5.setText(_translate("MainWindow", "Stage"))
        self.label_6.setText(_translate("MainWindow", "Gender"))
        self.label_7.setText(_translate("MainWindow", "Stroke"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Swimer"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Distance"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Stroke"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stage"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Place"))

############# โหลด ข้อมูล ใส่ Combobox ##############

    def cmb_Load_data(self,sql):
        conn = sqlite3.connect("swimer.db")
        cur = conn.cursor()
        result = cur.execute(sql)
        data = result.fetchall()
        conn.close()
        #print(sql)
        return data

    def cmbSwimer_ (self):
        value = self.cmb_Load_data("select Swimer_ID,Fname ||' '|| Lname from Swimer")
        if(len(value)>0):
            for i in range(len(value)):
                a = value[i]
                self.cmbSwimer.addItem(str(a[1]),str(a[0]))

    def cmbDis_ (self):
        value = self.cmb_Load_data("select * from Distance")
        if(len(value)>0):
            for i in range(len(value)):
                a = value[i]
                self.cmbDis.addItem(str(a[1]),str(a[0]))

    def cmbGender_ (self):
        value = self.cmb_Load_data("select * from Gender")
        if(len(value)>0):
            for i in range(len(value)):
                a = value[i]
                self.cmbGender.addItem(str(a[1]),str(a[0]))

    def cmbStage_ (self):
        value = self.cmb_Load_data("select * from Stage")
        if(len(value)>0):
            for i in range(len(value)):
                a = value[i]
                self.cmbStage.addItem(str(a[1]),str(a[0]))

    def cmbStroke_ (self):
        value = self.cmb_Load_data("select * from Stroke")
        if(len(value)>0):
            for i in range(len(value)):
                a = value[i]
                self.cmbStroke.addItem(str(a[1]),str(a[0]))

############# ปิด Combobox ##########

    def dis_cmb_txt(self):
        self.cmbDis.setEnabled(False)
        self.cmbStage.setEnabled(False)
        self.cmbStroke.setEnabled(False)
        self.cmbSwimer.setEnabled(False)
        self.cmbGender.setEnabled(False)

        self.txtPlace.setEnabled(False)
        self.txtTime.setEnabled(False)

########## เปิดโปรแกรมจะมารัน ฟังกชั่นนี้ก่อน ####

    def Load(self):
############# เรียก ฟังกชั่น โหลด ข้อมูล ใส่ Combobox ##############
        self.a.clear()
        self.cmbDis.clear()
        self.cmbStage.clear()
        self.cmbStroke.clear()
        self.cmbSwimer.clear()
        self.cmbGender.clear()

        self.txtPlace.clear()
        self.txtTime.clear()

        self.cmbDis_()
        self.cmbGender_()
        self.cmbStage_()
        self.cmbStroke_()
        self.cmbSwimer_()
        self.twgLoad_()

        self.dis_cmb_txt()

############# ปิด ปุ่ม ##############
        self.btnAdd.setEnabled(True)
        self.btnEdit.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.btnCancel.setEnabled(True)
        self.btnSave.setEnabled(False)
############# ตั้งค่า Combobox เป็นค่าว่าง ##############
        self.cmbGender.setCurrentIndex(-1)
        self.cmbDis.setCurrentIndex(-1)
        self.cmbStage.setCurrentIndex(-1)
        self.cmbStroke.setCurrentIndex(-1)
        self.cmbSwimer.setCurrentIndex(-1)
        self.cmbGender.setCurrentIndex(-1)

        
############# ฟังกชั่นเปิดปิดปุ่ม เมื่อ กดปุ่ม Add Edit ##############
    def call_btn(self,x):
        if x == 1:
            self.btnAdd.setEnabled(False)
            self.btnSave.setEnabled(True)
            self.btnDelete.setEnabled(False)
        elif x == 2:  
            self.btnAdd.setEnabled(False)
            self.btnEdit.setEnabled(True)
            self.btnSave.setEnabled(False)
            self.btnDelete.setEnabled(True)

        self.btnCancel.setEnabled(True)
        
        self.cmbDis.setEnabled(True)
        self.cmbStage.setEnabled(True)
        self.cmbStroke.setEnabled(True)
        self.cmbSwimer.setEnabled(True)
        self.cmbGender.setEnabled(True)

        self.txtPlace.setEnabled(True)
        self.txtTime.setEnabled(True)

############# โหลดข้อมูลจาก Combobox ให้ตรงกับแถวในตารางเมื่อต้องการ แก้ไข หรือ ลบ ##############
    def call_cmb(self):
        row = self.tableWidget.currentRow()
        cb1 = self.cmbSwimer.findText(self.tableWidget.item(row,0).text(),QtCore.Qt.MatchFixedString)
        cb2 = self.cmbDis.findText(self.tableWidget.item(row,1).text(),QtCore.Qt.MatchFixedString)
        cb3 = self.cmbStroke.findText(self.tableWidget.item(row,2).text(),QtCore.Qt.MatchFixedString)
        cb4 = self.cmbGender.findText(self.tableWidget.item(row,3).text(),QtCore.Qt.MatchFixedString)
        cb5 = self.cmbStage.findText(self.tableWidget.item(row,4).text(),QtCore.Qt.MatchFixedString)
        self.txtPlace.setText(self.tableWidget.item(row,5).text())
        self.txtTime.setText(self.tableWidget.item(row,6).text())
        if cb1 >= 0:
            self.cmbSwimer.setCurrentIndex(cb1)
        if cb2 >= 0:
            self.cmbDis.setCurrentIndex(cb2)
        if cb3 >= 0:
            self.cmbStroke.setCurrentIndex(cb3)
        if cb4 >= 0:
            self.cmbGender.setCurrentIndex(cb4)
        if cb5 >= 0:
            self.cmbStage.setCurrentIndex(cb5)
        self.call_btn(2)
        self.dis_cmb_txt()
        self.save_stat = "del"

############# เก็บค่าจาก Combobox ก่อนทำการอัพเดท หรือ ลบ เพื่อไปใช้ยืนยัน ##############
    def get_twg_update_values(self):
        self.a.clear()
        self.a.append(self.cmbSwimer.currentData())
        self.a.append(self.cmbDis.currentData())
        self.a.append(self.cmbStroke.currentData())
        self.a.append(self.cmbGender.currentData())
        self.a.append(self.cmbStage.currentData())

    def btnAdd_click(self):
        self.save_stat = "add"
        self.call_btn(1)

    def btnEdit_click(self):
        self.save_stat = "edit"
        self.call_btn(1)
        self.get_twg_update_values()
        self.btnEdit.setEnabled(False)
        self.btnSave.setEnabled(True)

    def btnCancel_click(self):
        self.Load()

############# รันคำสั่ง sql ทั้งหมดที่นี่ ##############
    def excute_data(self,sql):
        conn = sqlite3.connect('swimer.db') # เชื่อมต่อ ฐานข้อมูล
        cur = conn.cursor() 
        cur.execute(sql) # execute คำสั่ง sql
        data = cur.fetchall() # ดึงข้อมูลที่ได้จากการรันไปไว้ที่ตัวเเปร data เก็บข้อมูลเป็น List
        conn.close() # ปิดการเชื่อมต่อ ฐานข้อมูล
        #print(data)
        return data

    def twgLoad_(self):
        sql = "select (Swimer.Fname ||' '|| Swimer.Lname),Distance.Length,Stroke.Stroke_,Gender.Gender_,Stage.Stage_,Result.Time,Result.Place "
        sql += "FROM Swimer,Gender,Result,Stage,Stroke,Distance "
        sql += "where Result.Swimer = Swimer.Swimer_ID and Result.Gender = Gender.Gender_ID and Result.Distance = Distance.Distance_ID "
        sql += "and Result.Stage = Stage.Stage_ID and Result.Stroke = Stroke.Stroke_ID order by Swimer.Swimer_ID"
        #print(sql)
        data = self.excute_data(sql) # เรียกฟังชั่น execute_data ส่งคำสั่ง sql ไป แล้ว return ค่าที่ได้กลับมา
        self.tableWidget.setRowCount(len(data)) # เพิ่มจำนวนเเถว โดยนับจากความยาวข้องข้อมูล
        for i,row in enumerate(data):     # วนลูปใสข้อมูลทีล่ะเเถวในตาราง
            for j,val in enumerate(row):       
                self.tableWidget.setItem(i, j,QtWidgets.QTableWidgetItem(str(val)))
    
            
            
