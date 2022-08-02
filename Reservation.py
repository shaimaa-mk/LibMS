
from datetime import timedelta, datetime

class Reservation:

    def __init__(self, id, memberId, bookId, status):
        self._id = str(id)
        self._reservation_date = datetime.now().date()
        self._member_id = memberId
        self._book_id = bookId
        self._reservation_status_id = status
        print("An order with ID: %s has created" %self._id)
###########################################################
    def setReservationStatusID(self,status):
        self._reservation_status_id

    def getBookId(self):
        return self._book_id

    def getReservationId(self):
        return self._id

    def getMemberId(self):
        return self._member_id

    def getReservationDate(self):
        return self._reservation_date

    def getReservationStatusID(self):
        return self._reservation_status_id

    def getReservationDetails(self):
        return {
            "Reservation ID": self._id,
            "Reservation Date": self._reservation_date,
            "Book ID": self._book_id,
            "Member ID": self._member_id,
            "Reservation Status ID": self._reservation_status_id
        }

class ReservationStatus:
    def __init__(self, id, status):
        self._id =  str(id)
        self._reservation_status = status
    def setReservationStatus(self, status):
        self._reservation_status

    def getReservationStatusID(self):
        return self._id

    def getReservationStatus(self):
        return self._reservation_status

    def getReservationStatusDetails(self):
        return{
            "ID": self._id,
            "Reservation Status": self._reservation_status
        }



class Loan:
    def __init__(self, id, memberid, bookid):
        self._id = str(id)
        self._member_id = memberid
        self._book_id = bookid
        self._loan_date = datetime.now().date()
        seprateDate = datetime.strptime(str(self._loan_date), "%Y-%m-%d")
        self._return_date = seprateDate + timedelta(days=10)


    def getLoanId(self):
        return self._id

    def getMemberId(self):
        return self._member_id

    def getBookId(self):
        return self._book_id

    def getLoanDate(self):
        return self._loan_date

    def getReturnDate(self):
        return self._return_date

    def getLoan(self):
        return{
            "ID" : self._id,
            "Member ID" : self._member_id,
            "Book ID" : self._book_id,
            "Loan Date" : self._loan_date,
            "Return Date" : self._return_date
        }



