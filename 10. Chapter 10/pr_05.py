from numpy import rint


class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatusInfo(self):
        print("**********")
        print(f"Train Name - {self.name}")
        print(f"Total Number of Seats Available - {self.seats}")
        print("**********")


    def getFareInfo(self):
        print(f"Price of the Train Ticket - RS {self.fare}")

    def bookingTicket(self):
        if(self.seats>0):
            print("Yout Ticket Has Been Booked") 
            print(f"Your Seat Number is: {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, This Train Is Full.Kindly Try in in other Train") 
    def cancelTicket(self,seatnumber):
        pass

intercity = Train("Intercity Express:14015",150,2)
intercity.getStatusInfo()
intercity.getFareInfo()
intercity.bookingTicket()
intercity.getStatusInfo()
intercity.bookingTicket()
intercity.getStatusInfo()
intercity.bookingTicket()