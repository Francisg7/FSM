from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from stripManagement import views

# def trigger_error(request):
#     division_by_zero = 1 / 0

urlpatterns = [
    path('home', views.index, name='home'),
    path('', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout, name='logout'),
    path('flight/list_flight', views.list_flight, name='list_flight'),
    path('flight/add_flight', views.add_flight.as_view(), name='add_flight'),
    path('flight/add_flight_excel', views.uploadexcel, name = 'add_flight_excel'),
    path('flight/update_flight_plan/<int:aeronef_id>/', views.update_flight.as_view(), name = 'update_flight_plan'),
    path('flight/delete_flight_plan/<int:aeronef_id>/', views.delete_flight.as_view(), name = 'delete_flight_plan')


    # path('sentry-debug/', trigger_error),
]
urlpatterns += staticfiles_urlpatterns()