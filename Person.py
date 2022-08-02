

#parent class person
from datetime import datetime
class Person:

    def __init__(self, id, fname, lname):
        self._id = str(id)
        self._fname = fname
        self._lname = lname

    def getId(self):
        return self._id

    def getFirstName(self):
        return self._fname

    def getLastName(self):
        return self._lname

    def getFullName(self):
        return self._fname + " " + self._lname


    #modify propreties
    def setId(self, id):
        self._id = id

    def setFirstName(self, name):
        self._fname = name

    def setLastName(self,name):
        self._lname

    def get_Person(self):
       pass

    ############children##################

class Member(Person):

    def __init__(self, id, fname, lname, member_status_id):
        self._joined_date = datetime.now().date()
        self._member_status_id = member_status_id
        super().__init__(id, fname, lname)
        print("A Member has created with ID %s" % self.getId())
        # print('A client called %s has created and your ID is %s'%name%self.getId())

    def getJoinedDate(self):
        return self._joined_date

    def getActivateStatusId(self):
        return self._member_status_id

    def get_Person(self):
        return {
            "ID": self._id,
            "Fist Name": self._fname,
            "Last Name": self._lname,
            "Joined Date": self._joined_date,
            "Status": self._member_status_id
        }

class Author(Person):
    def __init__(self, id, fname, lname):
        super().__init__(id, fname, lname)
        print("An Author has created with ID %s" % self.getId())
        # print('An Author called %s has created and your ID is %s'%name%self.getId())

    def get_Person(self):
        return{
             "ID": self._id,
            "Fist Name": self._fname,
            "Last Name": self._lname
        }

class MemberStatus:
    def __init__(self,id ,  status):
        self._id = self._id = str(id)
        self._status_value = status


    def getStatus(self):
        return self._status_value

    def getMemberStatusId(self):
        return self._id

    def setStatus(self, value):
        self._status_value = value

    def getMemberStatusDetails(self):
        return {
            "Status ID" : self._id,
            "Status Value" : self._status_value
        }


