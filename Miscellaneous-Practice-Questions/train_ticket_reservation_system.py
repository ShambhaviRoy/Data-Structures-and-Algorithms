# Design a train ticket reservation system
import random
import datetime

class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ticket = None

    def book_ticket(self, start, end, date):
        self.ticket = Ticket(self.name, start, end, date)

    def cancel_ticket(self, ticket_no):
        self.ticket = None
        Train.cancel_ticket(ticket_no)

    def modify_ticket(self, start, end, date):
        self.ticket.start = start
        self.ticket.end = end
        self.ticket.date = date
        


class Ticket:
    def __init__(self, name, start, end, journey_date):
        self.passenger_name = name
        self.start = start
        self.end = end
        self.booking_date = datetime.datetime.now()
        self.journey_date = journey_date
        self.ticket_no = self.create_ticket_no()

    def create_ticket_no(self):
        self.ticket_no = random.randint()



class Train:
    def __init__(self, train_no, origin, destination):
        self.train_no = train_no
        self.origin = origin
        self.destination = destination
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)
    
    def cancel_ticket(self, ticket):
        self.tickets.remove(ticket)
                    

    