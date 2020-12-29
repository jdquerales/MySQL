import os
import pymysql

username = os.getenv('C9_USER')

print("Value of 'gitpod' environment variable :", username)

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try: 
    #run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        #sql = "SELECT * FROM Artist"
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
        #result = cursor.fetchall()
        #print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
