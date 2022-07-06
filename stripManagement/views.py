import openpyxl
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from stripManagement.forms import FlightForm
from stripManagement.models import *


def index(request):
    return render(request, 'index.html', {})


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lasttname = request.POST['first_name']
        email = request.POST['email']
        matricule = request.POST['matricule']
        phone = request.POST['tel']
        service = request.POST['service']
        password = request.POST['password']

        user = users.objects.create(username=username, password=password, first_name=firstname,
                                    last_name=lasttname,
                                    phone=phone, email=email, matricule=matricule,
                                    service=service
                                    )
        print(user.save())
        if user is not None:
            user.save()
            return redirect('login')
        else:
            return render(request, 'authenticate/register.html', {'error': 'matricule or password is incorrect'})

    return render(request, 'authenticate/register.html')


def login_user(request):
    if request.method == 'POST':
        matricule = request.POST['matricule']
        password = request.POST['password']

        user = auth.authenticate(password=password, matricule=matricule)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            # messages.success(request, 'There was an error logging in, Try Again...')
            return render(request, 'authenticate/login.html', {'error': 'matricule or password is incorrect'})
    else:
        return render(request, 'authenticate/login.html', {})


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def list_flight(request):
    list_flight = flightPlan.objects.all()
    return render(request, "list_flight_plan.html", {'list_flight': list_flight})


class add_flight(CreateView, PermissionRequiredMixin):
    model = flightPlan
    # fields = ('aircraft_id', 'flight_num', 'company', 'departAirport', 'destAirport', 'safety_airport', 'estDepTime',
    #           'estArrTime', 'flight_level',
    #           'flight_route', 'totPassengers', 'dateFrom', 'dateTo')
    form_class = FlightForm
    template_name = 'stripManagement/flightplan_form.html'
    success_url = reverse_lazy('list_flight')
    permission_required = 'stripManagement.can_add_flight_plan'

    def form_valid(self, form):
        form.instance.users = self.request.users
        return super().form_valid(form)
    # def get_absolute_url(self):  # new
    #     return reverse('list_flight', args=[str(self.aircraft_id)])


class update_flight(UpdateView):
    model = flightPlan
    # fields = ('aircraft_id', 'flight_num', 'company', 'departAirport', 'destAirport', 'safety_airport', 'estDepTime',
    #           'estArrTime', 'flight_level',
    #           'flight_route', 'totPassengers', 'dateFrom', 'dateTo')
    form_class = FlightForm
    template_name = 'stripManagement/flightplan_update_form.html'
    success_url = reverse_lazy('list_flight')
    success_message = "Flight updated succesfully"
    slug_field = 'aeronef_id'
    slug_url_kwarg = 'aeronef_id'
    # def get_absolute_url(self):  # new
    #     return reverse('list_flight', args=[str(self.aircraft_id)])


class delete_flight(DeleteView):
    model = flightPlan
    # fields = ('aircraft_id', 'flight_num', 'company', 'departAirport', 'destAirport', 'safety_airport', 'estDepTime',
    #           'estArrTime', 'flight_level',
    #           'flight_route', 'totPassengers', 'dateFrom', 'dateTo')
    form_class = FlightForm
    template_name = 'list_flight_plan.html'
    # success_url = reverse_lazy('list_flight')
    success_message = "Flight deleted succesfully"
    slug_field = 'aeronef_id'
    slug_url_kwarg = 'aeronef_id'
    # def get_absolute_url(self):  # new
    #     return reverse('list_flight', args=[str(self.aircraft_id)])

# def delete_flight_plan(request, aeronef_id):
#     # dictionary for initial data with
#     # field names as keys
#     context = {}
#
#     # fetch the object related to passed id
#     obj = get_object_or_404(flightPlan, aeronef_id=aeronef_id)
#
#     if request.method == "POST":
#         # delete object
#         obj.delete()
#         # after deleting redirect to
#         # home page
#         return HttpResponseRedirect("list_flight")
#
#     return render(request, "delete_flight_plan.html", context)

def uploadexcel(request):
    excel_data = ""

    if request.method == 'POST' and 'btn4' in request.POST:
        excel_file = request.FILES["excelfile"]
        print(excel_file)

        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Feuil1"]
        # print(worksheet["A5"].value)
        print(worksheet)

        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                print(type(cell.value))
                row_data.append(str(cell.value))

            #
            # print(row_data[2])
            # print(row_data[6])
            def get_company_instance(company_name):
                try:
                    companies = company.objects.get(company_name=company_name)
                except company.DoesNotExist:
                    return None
                return companies

            company.objects.create(
                company_name=row_data[2]
            )
            s = 1
            flightPlan.objects.get_or_create(
                aircraft_id=row_data[0],
                flight_num=row_data[1],
                company=get_company_instance(company_name=row_data[2]),
                departAirport=row_data[3],
                destAirport=row_data[4],
                safety_airport=row_data[5],
                estDepTime=row_data[6],
                estArrTime=row_data[7],
                flight_level=row_data[8],
                flight_route=row_data[9],
                totPassengers=row_data[10],
                # dateFrom=row_data[11],
                # dateTo=row_data[12],
            )
            excel_data.append(row_data)

    return render(request, 'add_flight_excel.html', {"excel_data": excel_data})
