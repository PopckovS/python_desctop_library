import pymysql.cursors

class ModelBase:

    # атрибут для хранения подключения к Бд
    connectionDB = None

    # Конфиги для подключения к Базе данных, в виде словаря
    connection = {'host' : 'localhost',
                  'user' : 'serg',
                  'password' : 11,
                  'db' : 'tutorial',
                  'charset' : 'utf8mb4'}


    # Подключиться к базе данных.
    def __init__(self):
        self.connectionDB = pymysql.connect(host='localhost',
                                       user='serg',
                                       password='11',
                                       db='tutorial',
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)

        # self.connectionDB = pymysql.connect(host=self.connection['host'],
        #                                  user=self.connection['user'],
        #                                  password=self.connection['password'],
        #                                  db=self.connection['db'],
        #                                  charset=self.connection['charset'],
        #                                  cursorclass=pymysql.cursors.DictCursor)


    # Получить главное меню для приложения
    def getAllFromMenu(self):

        if(self.connectionDB):
            cursor = self.connectionDB.cursor()
            sql = "SELECT * FROM `menu`"
            cursor.execute(sql) # Выполнить команду запроса
            # print("cursor.description: ", cursor.description)
            return cursor

        else:
            return None




















# # Подключиться к базе данных.
#     def connectionToDataBase(self):
#
#         # return pymysql.connect(host=connection['host'],
#         #                          user=connection['user'],
#         #                          password=connection['password'],
#         #                          db=connection['db'],
#         #                          charset=connection['charset'],
#         #                          cursorclass=pymysql.cursors.DictCursor)
#
#         connectionDB = pymysql.connect(host='localhost',
#                                        user='serg',
#                                        password='11',
#                                        db='tutorial',
#                                        charset='utf8mb4',
#                                        cursorclass=pymysql.cursors.DictCursor)
#
#         # connectionDB = ModelBase.connectionToDataBase()