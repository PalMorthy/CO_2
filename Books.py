class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        """
        TEST UNIT:
        ~~~~~~~~~~
        """
        if not isinstance(pages, int):
            raise TypeError("Pages must be int!!!")
        if pages < 0:
            raise ValueError("Amount of Pages must be positive")
        self.__name = name
        self.__author = author
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Duration must be int!!!")
        if duration < 0:
            raise ValueError("Duration must be positive!!!")
        self.__name = name
        self.__author = author
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self.duration})"
