from Book import Book, BookAuthor, Category
from Person import Member, Author, MemberStatus
from Reservation import Reservation, ReservationStatus, Loan
from Fine import Fine, FinePayment

# Get data from System ...........
categories = ["Architecture", "Biography", "Business", "Crafts", "Cookbook", "Diary", "Dictionary",
              "Encyclopedia", "Guide", "Health", "History", "Journal", "Math", "Memoir", "Philosophy",
              "Prayer", "Religion", "Textbook", "Review", "Science", "Sport"]
# Create Objects of Categories
category_objects = []
for index1, category in enumerate(categories):
    category_objects.append(Category("cat10"+str(index1), category))
    # insertCategoryTable("cat10"+str(index1), category)
    # Display Objects of Categories
    # print(category_objects[index1].getCategoryDetails())

# Get data from System ...........
authors = [["Michael", "Sims"],
           ["Jean", "Freadette"],
           ["Jeffrey", "Smith"],
           ["Barak", "Obama"],
           ["Stephen", "Hawking"]]
# # Create Objects of Authors
author_objects = []
for index2, [fname, lname] in enumerate(authors):
    author_objects.append(Author("auth20"+str(index2), fname, lname))
    # insert_author_table("auth20"+str(index2), fname, lname)
    # Display Objects of Authors
    # print(author_objects[index2].get_Person())

# Get data from System ...........
books = [{'book': str('The Story Of Charlette\'s Web'), 'id': "cat101", 'year': 2011, 'copy': 2, 'price': 10},
         {'book': str('The Witler\'s Digest Handbook Of Short Story Writing'), 'id': "cat102", 'year': 1994,
          'copy': 5, 'price': 15},
         {'book': str('The Frugal Gourmet'), 'id': "cat104", 'year': 1984, 'copy': 3, 'price': 15},
         {'book': str('The Audacity Of Hope'), 'id': "cat1010", 'year': 2006, 'copy': 5, 'price': 20},
         {'book': str('Black Holes and Baby Universes'), 'id': "cat1019", 'year': 1993, 'copy': 0, 'price': 20}]
# # Create Book Objects
book_objects = []
for index3, book1 in enumerate(books):
    book_objects.append(Book("bok30" + str(index3), book1.get('book'), book1.get('id'), book1.get('year'),
                             book1.get('copy'), book1.get('price')))
    # insert_book_table(book_objects[index3].get_bookid(),
    #                   book_objects[index3].get_title(),
    #                   book_objects[index3].getCategoryId(),
    #                   book_objects[index3].getPublicationDate(),
    #                   book_objects[index3].getCopiesOwned(),
    #                   book_objects[index3].getAvailableCopies(),
    #                   book_objects[index3].getBookPrice())
    # Display Book Objects
    # print(book_objects[index3].getBookDetials())

# Get data from System ...........
bookauthor = [["bok300", "auth200"],
              ["bok301", "auth201"],
              ["bok302", "auth202"],
              ["bok303", "auth203"],
              ["bok304", "auth204"]]
# Create BookAuthor Objects
bookauthor_objects = []
for index4, [book_id1, author_id] in enumerate(bookauthor):
    bookauthor_objects.append(BookAuthor(book_id1, author_id))
    # insert_bookauthor_table(book_id1, author_id)
    # Display BookAuthor Objects
    # print(bookauthor_objects[index4].getBookAuthorDetails())

# Get data from System ...........
member_status = ["Active", "Closed", "Canceled", "Balcklisted"]
# Create Member Status Objects
member_status_objects = []
for index5, status1 in enumerate(member_status):
    member_status_objects.append(MemberStatus("mesta40"+str(index5), status1))
    # insert_memberstatus_table("mesta40"+str(index5), status1)
    # Display Member Status Objects
    # print(member_status_objects[index5].getMemberStatusDetails())


# Create update status of membership Function
# //////////////////////////////////////////
def update_member_status():
    pass


# Create Member Objects
# Get data from user MENU instance .............
members = [{'first name': "Olive", 'last name': "Yew", 'status': "mesta400"},
           {'first name': "Allie", 'last name': "Grater", 'status': "mesta400"},
           {'first name': "Lois", 'lasfine_amountt name': "Nominator", 'status': "mesta400"},
           {'first name': "Rita", 'last name': "Book", 'status': "mesta401"},
           {'first name': "Augusta", 'last name': "Wind", 'status': "mesta400"},
           {'first name': "Rhoda", 'last name': "Report", 'status': "mesta400"},
           {'first name': "Chris", 'last name': "Anthemum", 'status': "mesta402"},
           {'first name': "Anit", 'last name': "Bath", 'status': "mesta400"},
           {'first name': "Jack", 'last name': "Armada", 'stataus': "mesta403"}]
member_objects = []
for index6, mm in enumerate(members):
    member_objects.append(Member("meb50"+str(index6), mm.get('first name'), mm.get('last name'), mm.get('status')))
    # insert_member_table(member_objects[index6].getId(),
    #                     member_objects[index6].getFirstName(),
    #                     member_objects[index6].getLastName(),
    #                     member_objects[index6].getJoinedDate(),
    #                     member_objects[index6].getActivateStatusId())
    # print(member_objects[index6].get_Person())

# Get data from System ...........
reservation_status = ["Waiting", "Pending", "Completed", "Canceled"]
# Create Reservation Status Objects
reservation_status_objects = []
for index7, status3 in enumerate(reservation_status):
    reservation_status_objects.append(ReservationStatus("ressta60"+str(index7), status3))
    # insert_reservation_status_table("ressta60"+str(index7), status3)
    # Display Reservation Status Objects
    # print(reservation_status_objects[index7].getReservationStatusDetails())

# Get data from user MENU instance .............
reservation_data = [["meb500", "bok300", 'The Witler\'s Digest Handbook Of Short Story Writing'],
                    ["meb504", "bok302", 'The Frugal Gourmet'],
                    ["meb503", "bok300", 'The Audacity Of Hope'],
                    ["meb502", "bok303", 'The Witler\'s Digest Handbook Of Short Story Writing'],
                    ["meb501", "bok304", 'Black Holes and Baby Universes'],
                    ["meb507", "bok303", 'The Audacity Of Hope']]
# print(reservation_data)

# Create Loan Objects
loan_objects = []


# Create Set Book Loaned Function
def set_book_loaned(bookid22):
    for book in book_objects:
        if bookid22 == book.get_bookid():
            book.updateAvalibleCopies()


# Create update status of reservation Function
def update_reservation_status(memberid1, bookid3):
    for index8, member1 in enumerate(member_objects):
        if member1.getId() == memberid1:
            if member1.getActivateStatusId() == "mesta400":
                for book2 in book_objects:
                    # if book2.get_bookid() != bookid3:
                    #     print("Sorry! Looks like the book is not available in the library yet.")
                    #     return "ressta600"  # waiting
                    if book2.get_bookid() == bookid3:
                        if book2.getAvailableCopies() != 0:
                            print("book found")
                            loan_objects.append(Loan("lan80" + str(index8), memberid1, bookid3))
                            set_book_loaned(bookid3)
                            print("Good Job! Your reserving has completed successfully.")
                            return "ressta602"  # completed
                        elif book2.getAvailableCopies() == 0:
                            print("Sorry! All book items, that are available in the library, has been borrowed.")
                            return "ressta601"  # pending
            else:
                print("Check out your membership status please!")
                return "ressta603"  # canceled


# Create Reservation Objects
reservation_objects = []
for index9, [memberid2, bookid2, title] in enumerate(reservation_data):
    reservation_objects.append(
        Reservation("res70" + str(index9), memberid2, bookid2, update_reservation_status(memberid2, bookid2)))
    # insert_reservation_table("res70" + str(index9),
    #                          reservation_objects[index9].getBookId(),
    #                          reservation_objects[index9].getMemberId(),
    #                          reservation_objects[index9].getReservationDate(),
    #                          reservation_objects[index9].getReservationStatusID())
    # Display Reservation Objects
    # print(reservation_objects[index9].getReservationDetails())

# Display Loan Objects
for loan in loan_objects:
    # insert_loan_table(loan.getLoanId(),
    #                   loan.getBookId(),
    #                   loan._member_id,
    #                   loan.getLoanDate(),
    #                   loan.getReturnDate())
    print(loan.getLoan())


# Create Find Amount Function
def find_amount(loann):
    memberid3 = loann.getMemberId()
    idbooks = []
    summation = 0
    for loan1 in loan_objects:
        if memberid3 == loan1.getMemberId():
            idbooks.append(loan1.getBookId())
            print("yes")
    for ID in idbooks:
        for book3 in book_objects:
            if book3.get_bookid() == ID:
                summation = summation + book3.getBookPrice()
            else:
                summation = summation
    return summation


# Create Fine Objects
fine_objects = []
for index10, loan2 in enumerate(loan_objects):
    fine_objects.append(Fine("fin09"+str(index10), loan2, find_amount(loan2)))
    # insert_fine_table(fine_objects[index10].getFineId(),
    #                   fine_objects[index10].getMemberId(),
    #                   fine_objects[index10].getLoanId(),
    #                   fine_objects[index10].getFineDate(),
    #                   fine_objects[index10].getFineAmount())
    print(fine_objects[index10].getFineDetials())


# Create Balance Fine Function
def get_balance_fine(mbmid, amount):
    for fine1 in fine_objects:
        if fine1.getMemberId() == mbmid:
            fine1.setFineAmount(fine1.getFineAmount() - amount)
            print("payed")
            return None


# Get data from System
payments = [5, 5, 6, 0]
# Create FinePayment Objects
fine_payment_objects = []
for index11, loan3 in enumerate(loan_objects):
    fine_payment_objects.append(FinePayment("fipy10"+str(index11), loan3, payments[index11]))
    # insert_finepay_table(fine_payment_objects[index11].getFinePaymentId(),
    #                      fine_payment_objects[index11].getMemberID(),
    #                      fine_payment_objects[index11].getFinePaymentDate(),
    #                      fine_payment_objects[index11].getPaymentAmount())
    # print(fine_payment_objects[index11].getFinePaymentDetails())

for index, payment in enumerate(fine_payment_objects):
    print(payment.getMemberID())
    get_balance_fine(payment.getMemberID(), payments[index])

