import mysql.connector
LibMS = mysql.connector.connect(host='localhost', user='root', passwd='admin#246$', database='LibMS')
LibMSCursor = LibMS.cursor()


def delete_table(table):
    query = "DELETE FROM %s ;"
    if LibMS:
        LibMSCursor.execute(query, [table, ])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_category_row(row, value):
    query = "DELETE FROM category WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_book_row(row, value):
    query = "DELETE FROM book WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_author_row(row, value):
    query = "DELETE FROM author WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_bookauthor_row(row, value):
    query = "DELETE FROM book_author WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_member_row(row, value):
    query = "DELETE FROM member WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_reservation_row(row, value):
    query = "DELETE FROM reservation WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_fine_row(row, value):
    query = "DELETE FROM fine WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_loan_row(row, value):
    query = "DELETE FROM loan WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def delete_fine_payment_row(row, value):
    query = "DELETE FROM fine_payment WHERE %s = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [row, value])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")
