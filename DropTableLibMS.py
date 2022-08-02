import mysql.connector
LibMS = mysql.connector.connect(host='localhost', user='root', passwd='admin#246$', database='LibMS')
LibCursor = LibMS.cursor()


def drop_table(table_name):
    query = "DROP TABLE %s;"
    if LibMS:
        LibCursor.execute(query, [table_name, ])


def drop_database(database_name):
    query = "DROP DATABASE %s;"
    if LibMS:
        LibCursor.execute(query, [database_name, ])

