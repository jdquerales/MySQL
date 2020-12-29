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
        rows = cursor.execute("DELETE FROM Friends WHERE name= %s;", 'Bob')
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
