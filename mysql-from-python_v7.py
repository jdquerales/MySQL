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
        rows = [(23,'Bob'),
        (24,'Jim'),
        (25,'Fred')]
        cursor.executemany("UPDATE  Friends SET age=%s WHERE name=%s;",rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
