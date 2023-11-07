
from django.shortcuts import render
from decimal import Decimal
from datetime import datetime
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Train, Bookings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return render(request, 'myapp/signin.html')


@login_required(login_url='signin')
def findtrain(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        date_obj = datetime.strptime(date_r, "%Y-%m-%d")
        day = date_obj.strftime("%A")
        day = "On_" + day
        bus_list = Train.objects.filter(source=source_r, dest=dest_r)
        details = {}
        j = 0
        for i in bus_list :
            if i.Day(day = day) :
                details[j] = i 
                j = j+ 1
            print(details)   
        if bus_list:
            return render(request, 'myapp/list.html', {'bus_list':bus_list})
        else:
            context["error"] = "Sorry no trains availiable"
            return render(request, 'myapp/findbus.html', context)
    else:
        return render(request, 'myapp/findbus.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('Train_No')
        seats_r = int(request.POST.get('no_seats'))
        bus = Train.objects.get(Train_No=id_r)
        if bus:
            bus_rem=bus.no_of_seats_rem
            if bus_rem > int(seats_r):
                name_r = bus.Name
                cost = int(seats_r) * bus.ticket_price
                source_r = bus.source
                dest_r = bus.dest
                nos_r = Decimal(bus.no_of_seats)
                price_r = bus.ticket_price
                # date_r = bus.date
                # time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                # userid_r = request.user.user_id
                rem_r = bus_rem - seats_r
                Train.objects.filter(Train_No=id_r).update(no_of_seats_rem=rem_r)
                book = Bookings.objects.create(name=username_r, train_name=name_r,
                                           source=source_r, trainno=id_r,
                                           dest=dest_r, ticket_price=price_r, nos=seats_r,
                                           status='BOOKED',)
                print('------------book id-----------', book.id)
                # book.save()
                print("fun")
                return render(request, 'myapp/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findbus.html', context)

    else:
        print("Done")
        return render(request, 'myapp/findbus.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Bookings.objects.get(id=id_r)
            bus = Train.objects.get(id=book.trainno)
            rem_r = bus.rem + book.nos
            Train.objects.filter(id=book.trainno).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Bookings.objects.filter(id=id_r).update(status='CANCELLED')
            Bookings.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookings)
        except Bookings.DoesNotExist:
            context["error"] = "Sorry You have not booked that Train"
            return render(request, 'myapp/error.html', context)
    else:
        return render(request, 'myapp/findbus.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    book_list = Bookings.objects.all()
    if book_list:
        return render(request, 'myapp/booklist.html', {'book_list':book_list})
    else:
        context["error"] = "Sorry no Trains booked"
        # print("1")
        return render(request, 'myapp/findbus.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'myapp/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)

from .models import Train  # Import your model

def get_all_trains(request):
    all_trains = Train.objects.all()  # Retrieve all trains
    return render(request, 'all_train.html', {'trains': all_trains})

from django.shortcuts import render
from .models import Train  # Import your Train model

def find_trains_view(request):
    trains = {}  # Initialize an empty list for trains
    j = 0
    for i in Train.objects.all() :
        print(i)
        trains[j] = i.details() 
        print(i.details())
        j = j+ 1
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        
        # Perform a query to find trains based on the user's input
        # Replace this with your actual query logic
        # Example query: trains = Train.objects.filter(source=source, destination=destination, date=date)

    # Render a template and pass context data
    return render(request, 'myapp/trains_list.html', {'trains': trains})
    
    return render(request, 'myapp/find_trains.html')
from .models import Stoppage, Train

def trains_at_station_on_day(request, station_code, day):
    # Filter trains that have a stop at the specified station on the given day
    # trains = Train.objects.filter(stoppage_station_code=station_code, stoppage_day=day).distinct()
    date = request.GET.get('days')
    date1 = request.GET.get('v')
    return render(request, 'myapp/trains_at_station_on_day.html',{'data' : request.path})

# views.py
from django.shortcuts import render
from .models import Train

def trains_with_food(request):
    # Filter trains that have food availability
    trains = Train.objects.filter(Foodavailability='Y')

    return render(request, 'myapp/trains_with_food.html', {'trains': trains})

from .models import Passenger

def tot_passengers(request, train_no):
    male_passengers = Passenger.objects.filter(Ticket_No__Train_No=train_no, Gender='M').count()
    female_passengers = Passenger.objects.filter(Ticket_No__Train_No=train_no, Gender='F').count()

    context = {
        'train_no': train_no,
        'male_passengers': male_passengers,
        'female_passengers': female_passengers,
    }

    return render(request, 'myapp/tot_passengers.html', context)

from .models import Stoppage

def total_stops_for_train(request, train_no):
    total_stops = Stoppage.objects.filter(Train_No=train_no).count()

    context = {
        'train_no': train_no,
        'total_stops': total_stops,
    }

    return render(request, 'myapp/total_stops.html', context)

# views.py
from django.shortcuts import render
from .models import Stoppage

def tot_journey(request, train_no):
    # Get the first and last stops for the train
    first_stop = Stoppage.objects.filter(Train_No=train_no).earliest('Arrival_Time')
    last_stop = Stoppage.objects.filter(Train_No=train_no).latest('Arrival_Time')

    total_journey = last_stop.Arrival_Time - first_stop.Arrival_Time

    context = {
        'train_no': train_no,
        'total_journey': total_journey,
    }

    return render(request, 'myapp/tot_journey_time.html', context)


from django.shortcuts import render, redirect
from .models import Train
from .forms import TrainUpdateForm  # Create this form in forms.py

# views.py

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Train
from .forms import TrainUpdateForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def update_train_details(request, train_id):
    train = get_object_or_404(Train, Train_No=train_id)

    if request.method == 'POST':
        form = TrainUpdateForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            return redirect('train_detail', train_id=train_id)
    else:
        form = TrainUpdateForm(instance=train)

    context = {
        'train': train,
        'form': form,
    }
    return render(request, 'myapp/update_train_details.html', context)

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Train, Stoppage

def train_schedule(request, train_no):
    train = get_object_or_404(Train, Train_No=train_no)
    stoppages = Stoppage.objects.filter(Train_No=train_no).order_by('Arrival_Time')

    context = {
        'train': train,
        'stoppages': stoppages,
    }

    return render(request, 'myapp/train_schedule.html', context)

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket

def cancel_ticket(request, ticket_no):
    try:
        ticket = Ticket.objects.get(Ticket_No=ticket_no)
        if ticket.status != 'C':
            ticket.status = 'C'  # Update the status to 'Cancelled'
            ticket.save()
            messages.success(request, 'Ticket has been successfully cancelled.')
        else:
            messages.error(request, 'This ticket has already been cancelled.')
    except Ticket.DoesNotExist:
        messages.error(request, 'Ticket not found.')

    return redirect('my_tickets')  # Redirect to the user's ticket list (adjust the URL name accordingly)