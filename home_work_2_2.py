"""
Система для управляння адресною книгою
"""
from collections import UserDict

class Field:
    """Базовий клас для полів запису."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """
    Клас для зберігання імені контакту. Обов'язкове поле.
    """
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    """
    Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    """
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format. Must be a string of 10 digits.")
        super().__init__(value)

class Record:
    """
    Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        """
        Додавання телефону до запису.
        """
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        """
        Видалення телефону з запису.
        """
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        """
        Редагування номера телефону в запису.
        """
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number

    def find_phone(self, phone_number):
        """
        Пошук телефону в запису.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    """
    Клас для зберігання та управління записами.
    """
    def add_record(self, record):
        """
        Додавання запису.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Пошук запису за ім'ям.
        """
        return self.data.get(name)

    def delete(self, name):
        """
        Видалення запису за ім'ям.
        """
        if name in self.data:
            del self.data[name]

if __name__ == "__main__":
    