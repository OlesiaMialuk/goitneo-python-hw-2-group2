"""
Модуль бота-помічника
"""
from typing import List, Tuple

def input_error(func):
    """
    Декоратор для обробки помилок у функціях.

    Parameters:
    - func: Функція, яку обгортати декоратором.

    Returns:
    - inner: Обгорнута функція з обробкою помилок.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments provided."

    return inner

@input_error
def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Розбирає введений користувачем рядок та виділяє команду та аргументи.

    Параметри:
    - user_input (str): Рядок введення від користувача.

    Повертає:
    - tuple: Кортеж, що містить команду (str) та аргументи (list).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args: List[str], contacts: dict) -> str:
    """
    Додає новий контакт до словника контактів.

    Параметри:
    - args (list): Список, що містить ім'я та номер телефону.
    - contacts (dict): Словник, де зберігаються контакти.

    Повертає:
    - str: Повідомлення про успішне додавання контакту.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: List[str], contacts: dict) -> str:
    """
    Змінює номер телефону для існуючого контакту.

    Параметри:
    - args (list): Список, що містить ім'я та новий номер телефону.
    - contacts (dict): Словник, де зберігаються контакти.

    Повертає:
    - str: Повідомлення про успішну зміну контакту або про помилку, якщо ім'я не знайдено.
    """
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Contact {name} not found."

@input_error
def show_phone(args: List[str], contacts: dict) -> str:
    """
    Виводить номер телефону для зазначеного контакту.

    Параметри:
    - args (list): Список, що містить ім'я контакту.
    - contacts (dict): Словник, де зберігаються контакти.

    Повертає:
    - str: Номер телефону для вказаного контакту або повідомлення про помилку, 
    якщо ім'я не знайдено.
    """
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number: {contacts[name]}"
    else:
        return f"Contact {name} not found."

@input_error
def show_all(contacts: dict) -> str:
    """
    Виводить усі збережені контакти.

    Параметри:
    - contacts (dict): Словник, де зберігаються контакти.

    Повертає:
    - str: Рядок із всіма збереженими контактами та їхніми номерами телефонів
    або повідомлення про їх відсутність.
    """
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts found."

def main():
    """
    Основна функція для взаємодії з користувачем у консольному режимі.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()