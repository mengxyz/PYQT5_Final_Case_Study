import sys, sqlite3 
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui_result import * # นำเข้าฟรอม Result

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui = ResultWindow()
        self.ui.setupUi(self)
        self.ui.btnSave.clicked.connect(self.save_click)
        self.ui.btnDelete.clicked.connect(self.save_click)
        self.show

    def exe_query(self,sql):
        try:
            conn = sqlite3.connect("swimer.db")
            with conn:
                cur = conn.cursor()
                cur.execute(sql)
        except Error as e:
            print(e)
            msg = QMessageBox()
            msg.critical(
                self, 'Error',  '%s' % e,
                QMessageBox.Ok, 
                QMessageBox.Ok
            )
        finally:
            conn.close()

    def save_click(self):
        dis = str(self.ui.cmbDis.currentData())
        sw = str(self.ui.cmbSwimer.currentData())
        stg = str(self.ui.cmbStage.currentData())
        st = str(self.ui.cmbStroke.currentData())
        gd = str(self.ui.cmbGender.currentData())
        time = str(self.ui.txtTime.text())
        place = str(self.ui.txtPlace.text())

        if (self.ui.save_stat == "add"):
            sql = "insert into Result values ('"+ sw +"','"+ dis +"','"+ st +"','"+ gd +"','"+ stg +"','"+ time +"','"+ place +"')"
        elif (self.ui.save_stat == "edit"):
            d = self.ui.a
            sql = "update Result set Swimer = '"+ sw +"',Distance = '"+ dis +"',Stroke = '"+ st +"',Gender = '"+ gd +"',Stage = '"+ stg +"',"
            sql += "Time = '"+ time +"',Place = '"+ place +"' where "
            sql += "Swimer = '"+ d[0] +"' and Distance = '"+ d[1] +"' and Stroke = '"+ d[2] +"' and Gender = '"+ d[3] +"' and Stage = '"+ d[4] +"'"
        else:
            self.ui.a.clear()
            self.ui.get_twg_update_values()
            d = self.ui.a
            sql = "delete from Result where Swimer = '"+ d[0] +"' and Distance = '"+ d[1] +"' and Stroke = '"+ d[2] +"' and Gender = '"+ d[3] +"' and Stage = '"+ d[4] +"'"
        if(
            self.ui.cmbDis.currentIndex() == -1 or
            self.ui.cmbSwimer.currentIndex() == -1 or
            self.ui.cmbStage.currentIndex() == -1 or
            self.ui.cmbStroke.currentIndex() == -1 or
            self.ui.cmbGender.currentIndex() == -1 or
            self.ui.txtTime.text() == '' or
            self.ui.txtPlace.text() == ''
        ):
            msg = QMessageBox()
            msg.critical(
                self, 'Error',  'กรุณาใสข้อมูลให้ครบถ้วน',
                QMessageBox.Ok, 
                QMessageBox.Ok
            )
        else:
            self.exe_query(sql)
        self.ui.Load()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())