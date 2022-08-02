
from Reservation import Loan
from datetime import timedelta, datetime
class Fine:
    def __init__(self, id, loan, amount):
        self._id = str(id)
        self._member_id = loan.getMemberId()
        self._loan_id = loan.getLoanId()
        self._fine_date = datetime.now().date()
        self._fine_amount = amount

    def setFineAmount(self, amount):
        self._fine_amount = amount

    def getFineId(self):
        return self._id

    def getMemberId(self):
        return self._member_id

    def getLoanId(self):
        return self._loan_id

    def getFineDate(self):
        return self._fine_date

    def getFineAmount(self):
        return self._fine_amount

    def getFineDetials(self):
        return{
            "ID" : self._id,
            "Member ID" : self._member_id,
            "Loan ID" : self._loan_id,
            "Fine Date" : self._fine_date,
            "Fine Amount": self._fine_amount
        }


class FinePayment:
    def __init__(self, id, loan, amount):
        self._id = str(id)
        self._member_id = loan.getMemberId()
        self._payment_date = datetime.now().date()
        self._payment_amount = amount

    def setPayAmount(self, amount):
        self._payment_amount = amount

    def getFinePaymentId(self):
        return self._id

    def getFinePaymentDate(self):
        return self._payment_date

    def getPaymentAmount(self):
        return self._payment_amount

    def getMemberID(self):
        return self._member_id

    def getFinePaymentDetails(self):
        return{
            "ID" : self._id,
            "MemberID" : self._member_id,
            "Payment Date" : self._payment_date,
            "Payment Amount" : self._payment_amount
        }

