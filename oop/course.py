from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, title, duration, price):
        self.title = title
        self.duration = duration
        self.price = price

    @abstractmethod
    def print_details(self):
        pass


class OfflineCourse(Course):
    def __init__(self, title, duration, price, address):
        Course.__init__(self, title, duration, price)
        self.address = address

    def print_details(self):
        print(self.title, self.duration, self.price, self.address)


class OnlineCourse(Course):
    def __init__(self, title, duration, price, url):
        Course.__init__(self, title, duration, price)
        self.url = url

    def print_details(self):
        pass


c1 = OfflineCourse("Python", 40, 5000, 'Vizag')
c1.print_details()

# c2 = Course("Angular", 15, 2000)
c2 = OnlineCourse("Python", 40, 5000, "http://werjeele")
