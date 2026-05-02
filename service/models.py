import logging

class DataValidationError(Exception):
    """Used for data validation errors when deserializing"""

class Account:
    """Class that represents an Account"""
    data = []
    index = 0

    def __init__(self, name, email, address, phone_number):
        self.id = None
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number

    def create(self):
        """Creates an Account in the database"""
        Account.index += 1
        self.id = Account.index
        Account.data.append(self)

    def update(self):
        """Updates an Account in the database"""
        for account in Account.data:
            if account.id == self.id:
                account.name = self.name
                account.email = self.email
                account.address = self.address
                account.phone_number = self.phone_number
                return

    def delete(self):
        """Removes an Account from the database"""
        Account.data = [a for a in Account.data if a.id != self.id]

    @classmethod
    def all(cls):
        """Returns all Accounts"""
        return cls.data

    @classmethod
    def find(cls, account_id):
        """Finds an Account by its ID"""
        for account in cls.data:
            if account.id == account_id:
                return account
        return None

    def serialize(self):
        """Serializes an Account into a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number,
        }

    def deserialize(self, data):
        """Deserializes an Account from a dictionary"""
        try:
            self.name = data["name"]
            self.email = data["email"]
            self.address = data["address"]
            self.phone_number = data["phone_number"]
        except KeyError as error:
            raise DataValidationError("Invalid Account: missing " + error.args[0])
        except TypeError:
            raise DataValidationError("Invalid Account: body of request contained bad or no data")
        return self