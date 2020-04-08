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

        # self.ui.pushButton.clicked.connect(self.btnClicked)
        # self.ui.pushButton.clicked.connect(self.changePHPversion('5.6', '7.2'))
        # self.ui.pushButton_2.clicked.connect(self.changePHPversion('7.2', '5.6'))

        # self.cre1()
        # self.cre2()

    # def cre1(self):
    #     button1 = QtWidgets.QPushButton('7.2', self)
    #     button1.setToolTip('This is an example button')
    #     button1.move(200, 70)  # Указать место положение для кнопки
    #     button1.show()  # Этот метод отображает кнопку на форме, без этого будет скрыта
    #     button1.clicked.connect(self.changePHPversion('5.6', '7.2'))
    #
    # def cre2(self):
    #     button = QtWidgets.QPushButton('5.6', self)
    #     button.setToolTip('This is an example button')
    #     button.move(100, 70)  # Указать место положение для кнопки
    #     button.show()  # Этот метод отображает кнопку на форме, без этого будет скрыта
    #     button.clicked.connect(self.changePHPversion('7.2', '5.6'))


    # def changePHPversion(self, disable_php, enable_php):
    #
    #     disable = [
    #         'sudo a2dismod php7.4',
    #         'sudo a2dismod php7.3',
    #         'sudo a2dismod php7.2',
    #         'sudo a2dismod php7.1',
    #         'sudo a2dismod php5.6'
    #     ]
    #
    #     list = [
    #         'sudo a2enmod php{0}'.format(disable_php),
    #         'sudo service apache2 restart',
    #         'sudo update-alternatives  --set php /usr/bin/php{0}'.format(enable_php)
    #     ]
    #
    #     for i in disable:
    #         os.system(i)
    #
    #     for i in list:
    #         os.system(i)





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


    def createNewButton(self):
        button = QtWidgets.QPushButton('Туц Баттон', self)
        button.setToolTip('This is an example button')
        button.move(100, 70) # Указать место положение для кнопки
        button.show() # Этот метод отображает кнопку на форме, без этого будет скрыта

    def createNewSomthing(self):
        some = QtWidgets.QCheckBox('Check', self)
        some.move(200,200)
        some.show()

    # Событие связвает клик на кнопку и создание вторичной формы
    def btnClicked(self):
        self.ex3 = secondwindow()
        self.ex3.show()

        # У каждого виджета есть метод deleteLater - который удаляет эллемент
        self.ui.pushButton.deleteLater()
        self.ui.pushButton = None

        # Метод создания новой кнопки
        self.createNewButton()
        self.createNewButton()

        self.createNewSomthing()
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(50, 520, 89, 25))
        # self.pushButton.setObjectName("pushButton")
        # self.pushButton.setStyleSheet('background-color: green;')

        # self.btn = QtWidgets.QPushButton('Button', self)
        # self.btn.setStyleSheet('background-color: green;')
        # # self.btn.clicked.connect(self.buts)
        # self.setGeometry(300, 300, 300, 220)
        # self.setWindowTitle('Icon')
        # self.setWindowIcon(QtGui.QIcon('web.png'))

        # self.show()

        # layout.removeWidget(self.widget_name)
        # self.widget_name.deleteLater()
        # self.widget_name = None



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