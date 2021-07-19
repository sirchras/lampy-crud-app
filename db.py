import pymysql

from dotenv import dotenv_values

db_config = dotenv_values('.env')

def connect():
    return pymysql.connect(db=db_config['DB-NAME'], user=db_config['DB-USER'], passwd=db_config['DB-PASSWD'], host=db_config['DB-HOST'])

