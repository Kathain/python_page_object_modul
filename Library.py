class Library:
    last_searched_book = None

    def __init__(self, books: list):
        self.__books = books

    def __check_availability(self):
        if self.last_searched_book in self.__books:
            return True
        else:
            return False

    def search_book(self, name):
        self.last_searched_book = name
        return self.__check_availability()


if __name__ == '__main__':
    library = Library(["Fuck", "Fuck books", "FUCK YOU"])
    is_book_found = library.search_book("Fuck")
    print(is_book_found)