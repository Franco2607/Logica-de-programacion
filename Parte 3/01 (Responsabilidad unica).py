
# Incorrecto


class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def save_to_database(self):
        pass

    def send_email(self):
        pass

# Correcto


class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


class UserService:

    def save_to_database(self, user):
        pass


class EmailService:

    def send_email(self, email, message):
        pass

# EXTRA 

# Incorrecto


class Library:

    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.Prestamos = []

    def add_book(self, title, author, copies):
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, name, id, email):
        self.users.append({"name": name, "id": id, "email": email})

    def Prestamo_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1
                self.Prestamos.append(
                    {"user_id": user_id, "book_title": book_title})
                return True
        return False

    def return_book(self, user_id, book_title):
        for Prestamo in self.Prestamos:
            if Prestamo["user_id"] == user_id and Prestamo["book_title"] == book_title:
                self.Prestamos.remove(Prestamo)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1
                    return True
        return False

# Correcto


class Book:

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


class User:

    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email


class Prestamo:

    def __init__(self):
        self.Prestamos = []

    def Prestamo_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            self.Prestamos.append(
                {"user_id": user.id, "book_title": book.title})
            return True
        return False

    def return_book(self, user, book):
        for Prestamo in self.Prestamos:
            if Prestamo["user_id"] == user.id and Prestamo["book_title"] == book.title:
                self.Prestamos.remove(Prestamo)
                book.copies += 1
                return True
        return False


class Library:

    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.Prestamos_service = Prestamo()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def Prestamo_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.Prestamos_service.Prestamo_book(user, book)
        return False

    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.Prestamos_service.return_book(user, book)
        return False