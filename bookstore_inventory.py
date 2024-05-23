import sqlite3
import pyfiglet

# ANSI CODE FORMATTING

ascii_banner = pyfiglet.figlet_format("menu")

BLACK = "\x1b[30m"
MAGENTA = "\x1b[35m"
RED = "\x1b[31m"
DARK_RED = "\x1b[38;5;1m"
ORANGE = "\x1b[38;5;208m"
YELLOW = "\x1b[38;5;11m"
GREEN = "\x1b[38;5;82m"
CYAN = "\x1b[38;5;24m"
LIGHT_CYAN = "\x1b[38;5;159m"
PURPLE = "\x1b[38;5;91m"
DARK_BLUE = "\x1b[38;5;25m"
LIGHT_BLUE = "\x1b[36m"
PINK = "\x1b[38;5;13m"

END = "\033[0m"
BOLD = "\033[1m"

db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()


def enter_book():
    '''Entered book is added to ebookstore_db.
       Checks for unique ID and requires ID and stock to be a digit.'''
    id_list = []
    cursor.execute('''SELECT id FROM book''')
    messed_id_list = cursor.fetchall()
    for messed_id in messed_id_list:
        id_list.append(str(messed_id).strip("(,)"))
    while True:
        newbook_id = input("Enter book ID:")
        if newbook_id.isdigit() and newbook_id not in id_list:
            pass
        else:
            print(f"{RED}Invalid ID. Please enter a unique ID.{END}")

        newbook_title = input("Enter book title:")

        newbook_author = input("Enter author name:")

        newbook_qty = input("Enter stock quantity:")
        if newbook_qty.isdigit():
            pass
        else:
            print(f"{RED}Invalid quantity. Please enter an integer.{END}")
        cursor.execute('''INSERT INTO book(id, title, author, quantity)
                    VALUES(?,?,?,?)''', (newbook_id, newbook_title,
                                         newbook_author, newbook_qty))
        db.commit()
        print("")
        print(f"{GREEN}{newbook_title} has been successfully"
              f" added to the database.{END}")
        print("")
        break


def update_book():
    '''Updates book info in ebookstore_db.
       Checks for existing ID and requires stock to be a digit.'''
    id_list = []
    cursor.execute('''SELECT id FROM book''')
    messed_id_list = cursor.fetchall()
    for messed_id in messed_id_list:
        id_list.append(str(messed_id).strip("(,)"))

    while True:
        search_id = input("Please enter book ID:")
        if search_id in id_list:
            pass
        else:
            print(f"{RED}The ID you entered does not exist."
                  f" Please try again.{END}")
        update_menu = input("1. Update ID\n"
                            "2. Update title\n"
                            "3. Update author\n"
                            "4. Update quantity\n"
                            f"{BLACK}Select via entering corresponding"
                            f" number:{END}")

        if update_menu == '1':
            update_id = input("Please enter new ID:")
            cursor.execute('''UPDATE book SET id = ? WHERE id = ? ''',
                           (update_id, search_id))
            cursor.execute('''SELECT title FROM book WHERE id = ? ''',
                           (search_id,))
            update_title = str(cursor.fetchone()).strip("(,)")
            print(f"\n{GREEN}{update_title} succussfully updated.\n{END}")
            db.commit()
            break

        elif update_menu == '2':
            update_title = input("Please enter new title:")
            cursor.execute('''UPDATE book SET title = ? WHERE id = ? ''',
                           (update_title, search_id))
            cursor.execute('''SELECT title FROM book WHERE id = ? ''',
                           (search_id,))
            update_title = str(cursor.fetchone()).strip("(,)")
            print(f"\n{GREEN}{update_title} succussfully updated.\n{END}")
            db.commit()
            break

        elif update_menu == '3':
            update_author = input("Please enter new author:")
            cursor.execute('''UPDATE book SET author = ? WHERE id = ? ''',
                           (update_author, search_id))
            cursor.execute('''SELECT title FROM book WHERE id = ? ''',
                           (search_id,))
            update_title = str(cursor.fetchone()).strip("(,)")
            print(f"\n{GREEN}{update_title} succussfully updated.\n{END}")
            db.commit()
            break

        elif update_menu == '4':
            while True:
                update_qty = input("Please enter new quantity:")
                if update_qty.isdigit():
                    cursor.execute('''UPDATE book SET quantity = ? WHERE
                                    id = ?''', (update_qty, search_id))
                    cursor.execute('''SELECT title FROM book WHERE
                                    id = ? ''', (search_id,))
                    update_title = str(cursor.fetchone()).strip("(,)")
                    print(f"\n{GREEN}{update_title} succussfully updated.\n"
                          f"{END}")
                    db.commit()
                    break
                else:
                    print(f"{RED}You did not enter an integer."
                          f" Please try again.{END}")
        break


def delete_book():
    '''Deletes book info from ebookstore_db.
       Checks for existing ID to be removed.'''
    id_list = []
    cursor.execute('''SELECT id FROM book''')
    messed_id_list = cursor.fetchall()
    for messed_id in messed_id_list:
        id_list.append(str(messed_id).strip("(,)"))

    search_id = input("Enter book ID to remove from database:")
    if search_id not in id_list:
        print(f"{RED}The ID you entered does not exist."
              f" Please try again.{END}")
        return delete_book()
    cursor.execute('''SELECT title FROM book WHERE id = ? ''', (search_id,))
    deleted_book = str(cursor.fetchone()).strip("(,)")
    cursor.execute('''DELETE FROM book WHERE id = ? ''', (search_id,))
    print(f"\n{GREEN}{deleted_book} succussfully deleted.{END}\n")
    db.commit()


def search_book():
    '''Searches book info in ebookstore_db.
       Checks for existing ID, title or author.'''
    search_menu = input(f"{BLACK}Search by:{END}\n"
                        "1. ID\n"
                        "2. Title\n"
                        "3. Author\n"
                        f"{BLACK}Select via entering corresponding"
                        f" number:{END}")
    if search_menu == '1':
        while True:
            search_id = input("Enter ID:")
            cursor.execute('''SELECT * FROM book
                        WHERE id=?''', (search_id,))
            book_info = cursor.fetchone()
            try:
                id, title, author, quantity = book_info
                print(f"\nID:{id}\n"
                      f"Title:{title}\n"
                      f"Author:{author}\n"
                      f"Quantity:{quantity}\n")
                break
            except TypeError:
                print(f"{RED}The ID you entered does not exist."
                      f" Please try again.{END}")
    elif search_menu == '2':
        while True:
            search_title = input("Enter title:")
            cursor.execute('''SELECT id, title, author, quantity FROM book
                        WHERE title=?''', (search_title,))
            book_info = cursor.fetchone()
            try:
                id, title, author, quantity = book_info
                print(f"\nID:{id}\n"
                      f"Title:{title}\n"
                      f"Author:{author}\n"
                      f"Quantity:{quantity}\n")
                break
            except TypeError:
                print(f"{RED}The title you entered does not exist."
                      " Please try again.{END}")
    elif search_menu == '3':
        while True:
            search_author = input("Enter author name:")
            cursor.execute('''SELECT id, title, author, quantity FROM book
                        WHERE author=?''', (search_author,))
            book_info = cursor.fetchone()
            try:
                id, title, author, quantity = book_info
                print(f"\nID:{id}\n"
                      f"Title:{title}\n"
                      f"Author:{author}\n"
                      f"Quantity:{quantity}\n")
                break
            except TypeError:
                print(f"{RED}The author you entered does not exist."
                      " Please try again.{END}")


while True:
    print(f"{BOLD}{ascii_banner}{END}")
    menu = input("1. Enter book\n"
                 "2. Update book\n"
                 "3. Delete book\n"
                 "4. Search books\n"
                 "0. Exit\n"
                 f"{BLACK}Select via entering corresponding number:{END}")
    if menu == '1':
        enter_book()
    elif menu == '2':
        update_book()
    elif menu == '3':
        delete_book()
    elif menu == '4':
        search_book()
    elif menu == '0':
        exit()
