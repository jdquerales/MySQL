import os
import datetime
import pymysql

username = os.getenv('C9_USER')

print("Value of 'gitpod' environment variable :", username)

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try: 
    #run a query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime)""")
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
