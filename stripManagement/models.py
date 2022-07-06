from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class users(AbstractUser):
    Service = [("Previ-protec", "Prevision Protection"), ("VMA", "Aeorodrome  Meteorologie Survey "),
               ("Observateur", "Meteorological Observation"),
               ("AIM", "Airport Information Management"), ("IL", "Local Information"),
               ("IRE", "Radio Electric Infrastructure"),
               ("Facturation", "Facturation"), ("Telecom", "Telecom"), ("Tower", "Tower")]
    AIM = 1
    TOWER = 2
    CU = 3

    ROLE_CHOICES = ((AIM, 'AIM'), (TOWER, 'TOWER'), (CU, 'CU'))

    id = models.BigAutoField(primary_key=True)
    matricule = models.CharField(max_length=14, unique=True, default="")
    # password = models.CharField(max_length=20)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    service = models.CharField(choices=Service, max_length=20, blank=True),
    phone = models.IntegerField(null=True, validators=[RegexValidator(r'^\d{1,10}$')])
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=20)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'username', 'phone', 'service']
    USERNAME_FIELD = 'matricule'

    def __str__(self):
        return "matricule:{} name:{}".format(self.matricule, self.first_name + self.last_name)

    class Meta:
        db_table = 'users'
        ordering = ['matricule']
    #
    # def clean_username(self):
    #     username = self.clean_fields['username'].lower()
    #     r = users.objects.filter(username=username)
    #     if r.count():
    #         raise ValidationError("Username already exists")
    #     return username
    #
    # def clean_email(self):
    #     email = self.clean_fields['email'].lower()
    #     r = users.objects.filter(email=email)
    #     if r.count():
    #         raise ValidationError("Email already exists")
    #     return email
    #
    # def save(self, commit=True):
    #     user = users.objects.create_user(
    #         self.clean_fields['username'],
    #         self.clean_fields['first_name'],
    #         self.clean_fields['last_name'],
    #         self.clean_fields['email'],
    #         self.clean_fields['password1']
    #     )
    #     return user


class company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'company'
        ordering = ['company_name']


class flightPlan(models.Model):
    aeronef_id = models.BigAutoField(primary_key=True)
    aircraft_id = models.CharField(max_length=10, unique=True)
    # flight_rule = models.CharField(max_length=20, null=True)
    flight_type = models.CharField(max_length=10, null=True)
    # aeronef_type = models.CharField(max_length=20, null=True)
    departAirport = models.CharField(max_length=4, null=True)
    destAirport = models.CharField(max_length=4, null=True)
    estDepTime = models.TimeField(blank=True, null=True)
    estArrTime = models.TimeField(blank=True, null=True)
    # flight_speed = models.CharField(max_length=20, null=True)
    flight_level = models.IntegerField(null=True)
    flight_route = models.CharField(max_length=20, null=True)
    flight_speed = models.IntegerField(null=True)
    safety_airport = models.CharField(max_length=4, null=True)
    transpondeur = models.CharField(max_length=4, null=True)
    board_equipment = models.CharField(max_length=10, null=True)
    turbulance = models.CharField(max_length=10, null=True)
    totPassengers = models.CharField(max_length=20, null=True)
    flight_num = models.CharField(max_length=20, null=True)
    dateFrom = models.DateField(blank=True, null=True)
    dateTo = models.DateField(blank=True, null=True)
    # stripImage = models.ImageField(null=True, blank=True, upload_to='media')
    company = models.ForeignKey(company, on_delete=models.SET_NULL, null=True)
    # printed = models.BooleanField(max_length=5, blank=True, null=True)
    # squack = models.CharField(max_length=20, null=True, default='----')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    users = models.ForeignKey(users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.aircraft_id

    class Meta:
        db_table = 'flightPlan'
        ordering = ['created_on']


class strip(models.Model):
    id = models.BigAutoField(primary_key=True)
    aircraft_id = models.CharField(max_length=20)
    # flight_rule = models.CharField(max_length=20, null=True)
    flight_type = models.CharField(max_length=20, null=True)
    # aeronef_type = models.CharField(max_length=20, null=True)
    departAirport = models.CharField(max_length=4, null=True)
    destAirport = models.CharField(max_length=4, null=True)
    estDepTime = models.TimeField(blank=True, null=True)
    estArrTime = models.TimeField(blank=True, null=True)
    flight_speed = models.IntegerField(null=True)
    flight_level = models.IntegerField(null=True)
    flight_route = models.CharField(max_length=20, null=True)
    # flight_num = models.CharField(max_length=20, null=True)
    transpondeur = models.CharField(max_length=4, null=True)
    board_equipment = models.CharField(max_length=10, null=True)
    tirbulance = models.CharField(max_length=10, null=True)
    dateFrom = models.DateField(blank=True, null=True)
    dateTo = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    stripImage = models.ImageField(null=True, blank=True, upload_to='media')
    users = models.ForeignKey(users, on_delete=models.SET_NULL, null=True)
    flight_plan = models.ForeignKey(flightPlan, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.aircraft_id

    class Meta:
        db_table = 'strip'
        ordering = ['created_on']
