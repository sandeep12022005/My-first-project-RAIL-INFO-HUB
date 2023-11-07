from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('findbus', views.findtrain, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),
    path('all_trains/', views.get_all_trains, name='all_trains'),
    path('find-trains/', views.find_trains_view, name='find-trains'),
    path('trains_at_station_on_day/<str:station_code>/<str:day>/', views.trains_at_station_on_day, name='trains_at_station_on_day'),
    path('trains_with_food/', views.trains_with_food, name='trains_with_food'),
    path('total_passengers/<int:train_no>/', views.tot_passengers, name='total_passengers'),
    path('total_stops/<int:train_no>/', views.total_stops_for_train, name='total_stops'),
    path('JourneyTime/<int:train_no>/', views.tot_journey, name='JourneyTime'),
    path('trains/update/<int:train_id>/', views.update_train_details, name='update_train_details'),
    path('cancel_ticket/<int:ticket_no>/', views.cancel_ticket, name='cancel_ticket'),
    path('train_schedule/<int:train_no>/', views.train_schedule, name='train_schedule'),
]