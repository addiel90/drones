import pymysql
   
def get_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='6pMk5wGr7z.sm5q',
                                db='drones_db')