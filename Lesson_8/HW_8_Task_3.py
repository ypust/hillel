import datetime


class Record:
    def __init__(self, name, phone, surname=None, date_of_birth=None):
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        self.__date_of_birth = self.__parse_date_of_birth(date_of_birth)

    def __parse_date_of_birth(self, date_of_birth):
        if date_of_birth is not None:
            try:
                return datetime.datetime.strptime(date_of_birth, "%d.%m.%Y")
            except ValueError:
                print('Incorrect date format')
                return None

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_surname(self):
        return self.__surname

    def get_date_of_birth(self):
        return self.__date_of_birth

    def __str__(self):
        return f'{self.__name} - {self.__phone}'


class PhoneBook:
    def __init__(self):
        self.emergency_records = (Record('Fire_Station', 101), Record('Police', 102),
                                  Record('Ambulance', 103), Record('Gaz_Station', 104))
        self.records = []

    def add_record(self, record: Record):
        self.records.append(record)

    def delete_record(self, phone: str):
        for user_record in self.records:
            if user_record.get_phone() == phone:
                self.records.remove(user_record)
                return True
        return False

    def edit_record(self, record: Record):
        if self.delete_record(record.get_phone()):
            self.add_record(record)



class Interface:
    def __init__(self, book: PhoneBook):
        self.book = book

    """Add a new record"""

    def create_record(self):
        name = input('Add a new record to the Phone Book. Enter a user name:')
        phone = input('Add a new record to the Phone Book. Enter a phone number:')
        surname = input('Add a new record to the Phone Book. Enter a surname:')
        date_of_birth = input('Add a new record to the Phone Book. Enter a date of birth:')
        new_record = Record(name, phone, surname, date_of_birth)
        self.book.add_record(new_record)
        print(f'{new_record} was added to the Phone Book')

    """Remove a record"""

    def remove_record(self):
        removed_record = input('Enter a phone number to be removed:')
        self.book.delete_record(removed_record)
        print(f'The {removed_record} was deleted')

    """Edit a record"""

    def edit_record(self):
        name = input('Edit a record in the Phone Book. Enter a user name:')
        phone = input('Edit a record in the Phone Book. Enter a phone number:')
        surname = input('Edit a record in the Phone Book. Enter a surname:')
        date_of_birth = input('Edit a record in the Phone Book. Enter a date of birth:')
        new_record = Record(name, phone, surname, date_of_birth)
        self.book.edit_record(new_record)
        print(f'The {new_record} was updated')


if __name__ == '__main__':
    phone_book = PhoneBook()
    interface = Interface(phone_book)

    interface.create_record()
    interface.edit_record()
    interface.remove_record()
