

# Create your models here.
# Create your models here.
from django.db import models

from django.db import models
from datetime import date


def default_date():
    return date(2023, 1, 1)

class Train(models.Model):
    Train_No = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=25)
    Seat_Sleeper = models.IntegerField()
    Seat_FirstClass_AC = models.IntegerField()
    Seat_SecondClass_AC = models.IntegerField()
    Seat_Normal = models.IntegerField()
    Foodavailability = models.CharField(max_length=1, default='N')
    On_Sunday = models.CharField(max_length=1, default='N')
    On_Monday = models.CharField(max_length=1, default='N')
    On_Tuesday = models.CharField(max_length=1, default='N')
    On_Wednesday = models.CharField(max_length=1, default='N')
    On_Thursday = models.CharField(max_length=1, default='N')
    On_Friday = models.CharField(max_length=1, default='N')
    On_Saturday = models.CharField(max_length=1, default='N')
    source = models.CharField(max_length=100,default='Varanasi')
    dest = models.CharField(max_length=100)
    no_of_seats=models.IntegerField(default=50)
    no_of_seats_rem=models.IntegerField(default=50)
    ticket_price=models.IntegerField(default=2000)
    def __str__(self):
        return str(self.Train_No)
    
    def details(self):
        return {
           'Name'  : self.Name
        }
    def Day(self ,day = '') :
        if day == "On_Monday" :
            if self.On_Monday == 'Y' :
                return True
            else :
                return False
        if day == "On_Tuesday" :
            if self.On_Tuesday == 'Y' :
                return True
            else :
                return False
        if day == "On_Wednesday" :
            if self.On_Wednesday == 'Y' :
                return True
            else :
                return False
        if day == "On_Thursday" :
            if self.On_Thursday == 'Y' :
                return True
            else :
                return False
        if day == "On_Friday" :
            if self.On_Friday == 'Y' :
                return True
            else :
                return False
        if day == "On_Saturday" :
            if self.On_Saturday == 'Y' :
                return True
            else :
                return False
        if day == "On_Sunday" :
            if self.On_Sunday == 'Y' :
                return True
            else :
                return False




class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Bookings(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    name = models.CharField(max_length=30,blank=True,null=True)
    trainno=models.DecimalField(decimal_places=0, max_digits=2,blank=True,null=True)
    train_name = models.CharField(max_length=30,blank=True,null=True)
    source = models.CharField(max_length=30,blank=True,null=True)
    dest = models.CharField(max_length=30,blank=True,null=True)
    nos = models.DecimalField(decimal_places=0, max_digits=2,blank=True,null=True)
    ticket_price = models.DecimalField(decimal_places=2, max_digits=6,blank=True,null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2,blank=True,null=True)
    # email_id= models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)   
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=2,blank=True,null=True)
    def __str__(self):
        return self.email


class Account(models.Model):
    Username = models.CharField(max_length=15, primary_key=True)
    Password = models.CharField(max_length=20)
    Email_Id = models.CharField(max_length=35)
    Phone_No = models.CharField(max_length=10, default='', null=True)

class Passenger(models.Model):
    Passenger_Id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=1)
    Phone_No = models.CharField(max_length=10, default='', null=True)
    Ticket_No = models.IntegerField()
    Age = models.IntegerField()
    Class = models.CharField(max_length=20)

class Station(models.Model):
    Station_Code = models.CharField(max_length=5, primary_key=True)
    Station_Name = models.CharField(max_length=25)

class Stoppage(models.Model):
    Train_No = models.IntegerField()
    Station_Code = models.CharField(max_length=5)
    Arrival_Time = models.TimeField(null=True)
    Departure_Time = models.TimeField(null=True)

class Ticket(models.Model):
    Ticket_No = models.IntegerField(primary_key=True)
    Train_No = models.IntegerField()
    Date_of_Journey = models.DateField(default=default_date)
    Username = models.CharField(max_length=15)

  


