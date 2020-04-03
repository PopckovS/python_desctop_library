import pymysql.cursors

# Конфиги для подключения к Базе данных, в виде словаря
connection = {'host' : 'localhost',
              'user' : 'serg',
              'password' : 11,
              'db' : 'tutorial',
              'charset' : 'utf8mb4'}


# Подключиться к базе данных.
def connectionToDataBase():
    # return connection
    # connectionDB = pymysql.connect(host=connection['host'],
    return pymysql.connect(host=connection['host'],
                             user=connection['user'],
                             password=connection['password'],
                             db=connection['db'],
                             charset=connection['charset'],
                             cursorclass=pymysql.cursors.DictCursor)