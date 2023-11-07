
from django.contrib import admin
from .models import  User, Bookings,Passenger,Account, Station, Stoppage, Ticket, Train

# Register your models here.
admin.site.register(User)
admin.site.register(Bookings)
admin.site.register(Account)
admin.site.register(Passenger)
admin.site.register(Station)
admin.site.register(Stoppage)
admin.site.register(Ticket)
admin.site.register(Train)
