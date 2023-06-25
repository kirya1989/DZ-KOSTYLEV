class Library:
    # класс означает библиотеку
    # позволяет добавлять в него книги
    
    # осуществлять поиск по книгам
    # добавлять или удалять читателей
    # осуществлять поиск по читателям
    def add_book(book):
        #добавить книгу в библиотеку
        pass

    def remove_book(book):
        #удалить книгу из библиотеки
        pass

    def find_book(title, author):
        # найти книгу
        pass

    def add_reader(reader):
        # добавить читателя
        pass

    def remove_reader(reader):
        # удалить читателя
        pass
    
    def find_reader(name):
        # найти читателя
        pass

class Book:
    # класс означает книгу
    # позволяет добавлять или изменять информацию о книге
    # у нее есть атрибут - владелец книги
    # и аттрибут, к какой библиотеке она принадлежит
    # класс позволяет получить доступ к книге
    def change_info(title, author, isbn, tags, description, year):
        pass

    def change_owner(reader):
        pass

    def request_access():
        pass

    def pin_to_library(library):
        pass

class Reader:
    # класс означает посетителя библиотеки
    # ползволяет смотреть, какие книги у него есть
    # и к каким библиотекам он прикреплен
    def list_owned_books():
        pass

    def reader_of_libraries():
        pass

class NoSuchBookException(Exception):
    # ошибка возникает если такой книги нет в библиотеке, но мы ее пытаемся найти или удалить
    pass

class NoSuchReaderException(Exception):
    # ошибка возникает если такого читателя нет в библиотеке, но мы его пытаемся найти или удалить
    pass

class RestrictedBookAccessException(Exception):
    # ошибка возникает, если нельзя получить доступ к книге
    pass

class RestrictedOwnerTransfer(Exception):
    # ошибка возникает, если нельзя изменить владельца книги
    pass