# A Bike Rental System
### A full fledged bike rental system implemented in Python using object oriented programming.
# 

''' Customers can
- See available bikes on the shop
- Rent bikes on hourly basis $5 per hour.
- Rent bikes on daily basis $20 per day.
- Rent bikes on weekly basis $60 per week.
- Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price '''

''' The bike rental shop can
- issue a bill when customer decides to return the bike.
- display available inventory
- take requests on hourly, daily and weekly basis by cross verifying stock'''

import datetime
# Shop Class
class BikeRental:

    def __init__(self, stock=10, revenue=0):

        self.stock = stock
        self.revenue = revenue

# See available bikes on the shop
    
    def display_bikes(self):
        # print(f'We have {self.stock} bikes in Hour store')
        return self.stock
    
## Hourly basis $5 per hour

    def rental_hourly_basis(self, n_bikes):
        now = datetime.datetime.now()
        self.stock -= n_bikes
        print(f"Congrats, You Rent {n_bikes} bikes, From {now.time()} it will cost 5$ per Hour")

## Daily basis $20 per hour

    def rental_daily_basis(self):
        pass

## weekly basis $60 per hour

    def rental_weeklty_basis(self):
        pass

## Return Bike

    def return_bike(self,n_bikes):
        now = datetime.datetime.now()
        self.stock += n_bikes
        

class Customer(BikeRental):

    def __init__(self, av_money=0,bikes=0):
        super().__init__()
        self.av_money = av_money
        self.bikes=bikes

    def request_bike(self):

        service = input("Choose (Request) or (Return)? ").lower()
        if service == 'request':
            n_bikes = input('How Many bikes you want to Rent? ')
            rental_method = input(f"Enter (hourly) or (daily) or (weekly) ? ").lower()
            n_bikes = int(n_bikes)

            if n_bikes > self.display_bikes():
                print(f'We Don\'t have {n_bikes} in our Shop, Available bikes are {self.display_bikes()}')
            else:
                if rental_method == 'hourly':
                    self.rental_hourly_basis(n_bikes)
        elif service == 'return':
            n_bikes = int(input('n_bikes'))
            self.av_money -= 5*n_bikes
            self.stock += n_bikes
        else:
            print('Choose right Service')



if __name__ == '__main__':
    ## Test
    abdullah = Customer(25)
    abdullah.request_bike()
    print(abdullah.stock)
    print(abdullah.av_money)
    ahmed = Customer(25)
    ahmed.request_bike()
    print(ahmed.stock)
    print(ahmed.av_money)


