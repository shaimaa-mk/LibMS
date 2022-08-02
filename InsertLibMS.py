import mysql.connector
LibMSdb = mysql.connector.connect(host='localhost', user='root', passwd='admin#246$', database='LibMS')
LibMSCursor = LibMSdb.cursor()
if LibMSdb:
    print("Connected Successfully")


def insert_category_table(iidd, cateyy):
    query = "INSERT INTO category (id, category_name) VALUES (%s,%s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.executemany(query, [iidd, cateyy])
        LibMSdb.commit()


def insert_author_table(ii, ff, ll):
    query = "INSERT INTO author (id, first_name, last_name) VALUES (%s,%s,%s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [ii, ff, ll])
        LibMSdb.commit()


def insert_book_table(p1, p2, p3, p4, p5, p6, p7):
    query = "INSERT INTO book (id, title, category_id, publication_date, copies_owned, available_copies, price)" \
            "VALUES (%s,%s,%s,%s,%s,%s,%s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [p1, p2, p3, p4, p5, p6, p7])
        LibMSdb.commit()


def insert_bookauthor_table(bb, aa):
    query = "INSERT INTO book_author (book_id, author_id) VALUES(%s, %s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [bb, aa])
        LibMSdb.commit()


def insert_memberstatus_table(iii, sss):
    query = "INSERT INTO member_status(id, status_value) VALUES (%s, %s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [iii, sss])
        LibMSdb.commit()


def insert_member_table(m1, m2, m3, m4, m5):
    query = "INSERT INTO member (id, first_name, last_name, joined_date, active_status_id) " \
        "VALUES ( %s, %s, %s, %s, %s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [m1, m2, m3, m4, m5])
        LibMSdb.commit()


def insert_reservation_status_table(idid, sasa):
    query = "INSERT INTO reservation_status(id, status_value) VALUES (%s, %s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [idid, sasa])
        LibMSdb.commit()


def insert_reservation_table(r1, r2, r3, r4, r5):
    query = "INSERT INTO reservation (id, book_id, member_id, reservation_date, reservation_status_id)" \
            "VALUES (%s, %s, %s, %s, %s)"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [r1, r2, r3, r4, r5])
        LibMSdb.commit()


def insert_loan_table(l1, l2, l3, l4, l5):
    query = "INSERT INTO loan (id, book_id, member_id, loan_date, returned_date)" \
            "VALUES (%s, %s, %s, %s, %s)"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [l1, l2, l3, l4, l5])
        LibMSdb.commit()


def insert_fine_table(f1, f2, f3, f4, f5):
    query = "INSERT INTO fine(id, member_id, loan_id, fine_date, fine_amount)" \
            "VALUES(%s , %s, %s, %s, %s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [f1, f2, f3, f4, f5])
        LibMSdb.commit()


def insert_finepay_table(n1, n2, n3, n4):
    query = "INSERT INTO fine_payment (id, member_id, payment_date, payment_amount)" \
            "VALUES (%s, %s, %s, %s);"
    if LibMSdb:
        print("Connected Successfully")
        LibMSCursor.execute(query, [n1, n2, n3, n4])
        LibMSdb.commit()
