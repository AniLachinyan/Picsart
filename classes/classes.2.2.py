class Book:
    def __init__(self,title,author,price):
        self.__title=title
        self.__author=author
        self.__price=price


    def set_title(self,title):
        self.__title=title


    def get_title(self):
        return self.__title


    def set_author(self,author):
        self.__author=author

    def get_author(self):
        return self.__author


    def get_price(self):
        return self.__price

    def set_price(self,price):
        if (price>100):
            self.__price=price
        else:
            raise ValueError("Price can't be less than 100$ ")

    def display_book_detail(self):
        print(f"Book's title is {self.__title}, author is {self.__author}, price is {self.__price}")



book = Book("1984", "George Orwell", 15) 
book.display_book_detail()

book.set_price(200)
book.display_book_detail()

