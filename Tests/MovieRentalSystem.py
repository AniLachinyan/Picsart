from abc import ABC,abstractmethod

class RentalOperation(ABC):
    @abstractmethod
    def rent_movie(self,customer,movie):
        pass

    @abstractmethod
    def return_movie(self,rental):
        pass




class Movies(ABC):
    def __init__(self,title,genre,rating):
        self.title=title
        self.genre=genre
        self.rating=rating
        self.available_for_renting=True

    @abstractmethod
    def display_info(self):
        pass




class Comedy(Movies):
    def __init__(self, title, genre, rating):
        super().__init__(title, genre, rating)

    def display_info(self):
        return f"{self.title} comedy rating is {self.rating}"
    

class Drama(Movies):
    def __init__(self, title, genre, rating):
        super().__init__(title, "Drama", rating)

    def display_info(self):
        return f"{self.title} comedy rating is {self.rating}"
        

class Customers:
    def __init__(self,name,contact_info):
        self.name=name
        self.contact_info=contact_info
        self.rental_history=[]


    def view_rental_history(self):
        for rent in self.rental_history:
            print(rent)


class Rentals:
    def __init__(self,customer:Customers,movie:Movies):
        self.customer=customer
        self.movie=movie



class MovieRent(RentalOperation):
    def rent_movie(self, customer:Customers, movie:Movies):
        customer.rental_history.append(movie)
        movie.available_for_renting=False

    def return_movie(self, rental:Rentals):
        customer=rental.customer
        customer.rental_history.remove(rental)
        rental.movie.available_for_renting=True


class RentalSystem:
    def __init__(self):
        self.customers=[]
        self.movies=[]
        self.rental_operation=MovieRent()      


    def add_movie(self,movie:Movies):
        self.movies.append(movie)

    def add_customer(self,customer:Customers):
        self.customers.append(Customers)

    def search_movie(self,movie:Movies):
        if movie in self.movies:
            return movie
        else:
            print(f"{movie} is not available")              