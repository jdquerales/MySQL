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
    with connection.cursor() as cursor:
        cursor.execute("UPDATE  Friends SET age=%s WHERE name=%s;",(23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
