import mysql.connector
LibMS = mysql.connector.connect(host='localhost', user='root', passwd='admin#246$', database='LibMS')
LibMSCursor = LibMS.cursor()


def update_category_name(previous, new):
    query = "UPDATE category SET category_name = %s WHERE category_name = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_book_price(previous, new):
    query = "UPDATE book SET price = %s WHERE price = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_book_copies(new, previous):
    query = "UPDATE book SET copies_owned = %s WHERE copies_owned = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_author_first(new, previous):
    query = "UPDATE author SET first_name = %s WHERE first_name = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_author_last(new, previous):
    query = "UPDATE author SET last_name = %s WHERE last_name = %s ;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_member_first(new, previous):
    query = "UPDATE member SET first_name = %s WHERE first_name = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_member_last(new, previous):
    query = "UPDATE member SET last_name = %s WHERE last_name = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_member_status(new, previous):
    query = "UPDATE member SET active_status_id = %s WHERE active_status_id = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_reservation_status(new, previous):
    query = "UPDATE reservation SET reservation_status_id = %s WHERE reservation_status_id = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_loan_return(new, previous):
    query = "UPDATE loan SET returned_date = %s WHERE returned_date = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_fine_amount(new, previous):
    query = "UPDATE fine SET fine_amount = %s WHERE fine_amount = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")


def update_payment_amount(new, previous):
    query = "UPDATE fine_payment SET payment_amount = %s WHERE payment_amount = %s;"
    if LibMS:
        LibMSCursor.execute(query, [new, previous])
        LibMS.commit()
        print(LibMSCursor.rowcount, "record(s) affected. ")
