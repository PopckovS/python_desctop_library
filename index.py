#! /usr/bin/python3



# Выводит список всех модулей
# help('modules')

# ------------ Первый способ создания формы, конвертацией из ui ---------------
# from PyQt5 import QtWidgets, uic
# import sys
#
# app = QtWidgets.QApplication([])
# win = uic.loadUi("form.ui")  # расположение вашего файла .ui
#
# win.show()
# sys.exit(app.exec())
# -----------------------------------------------------------------------------

from PyQt5 import QtWidgets, QtGui, QtCore
from form import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import pymysql.cursors


# Подключиться к базе данных.
connectionDB = pymysql.connect(host='localhost',
                             user='serg',
                             password='11',
                             db='tutorial',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# connectionDB = pymysql.connect(host=connection['host'],
#                              user=connection['user'],
#                              password=connection['password'],
#                              db=connection['db'],
#                              charset=connection['charset'],
#                              cursorclass=pymysql.cursors.DictCursor)



def getAllFromMenu():
    if(connectionDB):
        sql = "SELECT * FROM `menu`"
        cursor = connectionDB.cursor()
        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)
        return cursor

        # for row in cursor:
        #     print(row['name'])








# Главный класс для определения формы
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # -------------- Изменения тут не повлияют на изменения в форме что в Designer ---------------
        # self.ui.label.setFont( QtGui.QFont('SansSerif', 30) )        # Изменение шрифта и размера
        # self.ui.label.setGeometry( QtCore.QRect(10, 10, 200, 200) )  # изменить геометрию ярлыка
        # self.ui.label.setText("PyScripts")                           # Меняем текст
        # ---------------------------------------------------------------------------------------------

        # -------------- Добавляем новые значения --------------
        menu = getAllFromMenu()
        for row in menu:
            # print(row['name'])
            self.ui.comboBox.addItem(row['name'])

        # self.ui.comboBox.addItem("Функции")
        # self.ui.comboBox.addItem("Классы")
        # self.ui.comboBox.addItem("Алгоритмы")
        # self.ui.comboBox.addItem("Программы")
        # self.ui.comboBox.addItem("Заметки")
        # -------------------------------------------------------


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())