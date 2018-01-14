from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Day, House
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
#Renders a html page for show_calendar using the show_calendar.html template and the selected days
@login_required
def show_calendar(request):
    group = request.user.groups.all()[0]
    users = group.user_set.all()
    forward = House.objects.get(houseName="Group_9").days_forward #how many days the calendar should show
    forward = 30
    for x in range (0, forward):
        if not Day.objects.filter(date=(timezone.now() + timezone.timedelta(days=x))).exists():
            currentday = Day(date=(timezone.now() + timezone.timedelta(days=x)))
            currentday.save()
            for user in users:
                  Slot.objects.create(student=user, day=currentday)
    days = (Day.objects.filter(date__lte=(timezone.now() + timezone.timedelta(days=forward)))).filter(date__gte=timezone.now()).order_by('date')
    houses = (House.objects.filter(houseName="Group_9"))
    return render(request, 'studentspot/show_calendar.html', {'days': days, 'houses' : houses, 'group' : group, 'users' : users})

def homepage(request):
    return render(request, 'studentspot/homepage.html')

def login(request):
    return render(request, 'studentspot/login.html')

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            #messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'studentspot/register.html', {'form': f})

def add_to_group(request):
   my_group = Group.objects.get(name='Test Huis')
   my_group.user_set.add(request.user.id)
   return render(request, 'studentspot/homepage.html')

def is_member(user):
    return user.groups.filter(name='Test Huis').exists()
