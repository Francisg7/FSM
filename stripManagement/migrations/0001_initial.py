# Generated by Django 4.0.5 on 2022-06-10 15:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('matricule', models.CharField(default='', max_length=14, unique=True)),
                ('email', models.EmailField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
                'ordering': ['matricule'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('company_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'company',
                'ordering': ['company_name'],
            },
        ),
        migrations.CreateModel(
            name='strip',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('aircraft_id', models.CharField(max_length=20)),
                ('flight_rule', models.CharField(max_length=20, null=True)),
                ('flight_type', models.CharField(max_length=20, null=True)),
                ('aeronef_type', models.CharField(max_length=20, null=True)),
                ('departAirport', models.CharField(max_length=20, null=True)),
                ('destAirport', models.CharField(max_length=20, null=True)),
                ('estDepTime', models.TimeField(blank=True, null=True)),
                ('estArrTime', models.TimeField(blank=True, null=True)),
                ('flight_speed', models.CharField(max_length=20, null=True)),
                ('flight_level', models.CharField(max_length=20, null=True)),
                ('flight_route', models.CharField(max_length=20, null=True)),
                ('flight_num', models.CharField(max_length=20, null=True)),
                ('dateFrom', models.DateField(blank=True, null=True)),
                ('dateTo', models.DateField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('stripImage', models.ImageField(blank=True, null=True, upload_to='media')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'strip',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='flightPlan',
            fields=[
                ('aeronef_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('aircraft_id', models.CharField(max_length=20)),
                ('departAirport', models.CharField(max_length=20, null=True)),
                ('destAirport', models.CharField(max_length=20, null=True)),
                ('estDepTime', models.TimeField(blank=True, null=True)),
                ('estArrTime', models.TimeField(blank=True, null=True)),
                ('flight_level', models.CharField(max_length=20, null=True)),
                ('flight_route', models.CharField(max_length=20, null=True)),
                ('safety_airport', models.CharField(max_length=20, null=True)),
                ('totPassengers', models.CharField(max_length=20, null=True)),
                ('flight_num', models.CharField(max_length=20, null=True)),
                ('dateFrom', models.DateField(blank=True, null=True)),
                ('dateTo', models.DateField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stripManagement.company')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'flightPlan',
                'ordering': ['created_on'],
            },
        ),
    ]
