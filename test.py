import sqlalchemy as db
import pandas as pd
database_username = 'root'
database_password = 'root'
database_ip       = 'localhost'
database_name     = 'dbtest'


database_engine = db.create_engine('mysql+mysqlconnector://{0}:{1}@{2}'.
                                               format(database_username, database_password, 
                                                      database_ip))
for exam_name in database_engine.execute('show databases').fetchall():
    print(exam_name[0])