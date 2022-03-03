from datetime import datetime, timedelta

class Person:
    def __init__(self, forename, surname, dob, gender):
        self._forename = forename
        self._surname = surname
        self._dob = dob
        self._gender = gender

    def get_forename(self):
        return self._forename
    def get_surname(self):
        return self._surname
    
    def get_dob(self):
        return self._age

    def get_gender(self):
        return self._gender
    def set_gender(self, new):
        self._gender = new

    def can_vote(self):
        return (datetime.now() - self.dob) > timedelta(days=365*18)

p1 = Person("")