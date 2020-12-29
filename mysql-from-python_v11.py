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
        list_of_names = ['fred', 'Fred']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({})".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()