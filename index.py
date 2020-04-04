#! /usr/bin/python3

from form import Ui_MainWindow  # Импорт главной сгенерированной формы
from secondForm import Ui_Form      # Импорт вторичной формы

from PyQt5 import QtWidgets, QtGui, QtCore
from ModelBase import ModelBase
import sys
import os



# Вторичная форма, вызывается при клике на кнопку
class secondwindow(QtWidgets.QMainWindow):

    # Главный метод для запуска формы, и методов для извлечения данных из Бд
    def __init__(self):
        super(secondwindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)




# Главный класс для запуска формы
class mywindow(QtWidgets.QMainWindow):

    ModelBase = None


    # Главный метод для запуска формы, и методов для извлечения данных из Бд
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.createConnection()  # Запуск метода создания подключения к Бд
        self.createMainMenu()    # Запуск метода для создания главного меню

        # привязка клика на кнопку к Методу(для запуска второго окна)
        self.ui.pushButton.clicked.connect(self.btnClicked)




    # Событие связвает клик на кнопку и создание вторичной формы
    def btnClicked(self):
        self.ex3 = secondwindow()
        self.ex3.show()



    # Этот метод выбирает текущий эллемент из ComboBox
    def whichComboBoxSelect(self):
        er = self.ui.comboBox.setCurrentIndex(1)



    # Этот метод выбирает все эллементы из ComboBox
    # def whichSelect(self):
    #     for i in range(self.ui.comboBox.count()):
    #         print(self.ui.comboBox.itemText(i))



    # Создает Экземпляр класса для работы с БД
    def createConnection(self):
        self.ModelBase = ModelBase()


    # Метод для создания главного меню со списком разделов
    def createMainMenu(self):
        menu = self.ModelBase.getAllFromMenu()
        for row in menu:
            self.ui.comboBox.addItem(row['name'])



# Запуск всего приложения
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())