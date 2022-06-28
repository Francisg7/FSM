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

    # path('sentry-debug/', trigger_error),
]
