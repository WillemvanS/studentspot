from django.shortcuts import render
from django.utils import timezone
from .models import Day, House

# Create your views here.
#Renders a html page for show_calendar using the show_calendar.html template and the selected days
def show_calendar(request):
    forward = House.objects.get(houseName="Group_9").days_forward #how many days the calendar should show
    for x in range (0, forward):
        if not Day.objects.filter(date=(timezone.now() + timezone.timedelta(days=x))).exists():
            Day.objects.create(date=(timezone.now() + timezone.timedelta(days=x)))
    days = (Day.objects.filter(date__lte=(timezone.now() + timezone.timedelta(days=forward)))).filter(date__gte=timezone.now()).order_by('date')
    houses = (House.objects.filter(houseName="Group_9"))
    return render(request, 'studentspot/show_calendar.html', {'days': days, 'houses' : houses})

def homepage(request):
    return render(request, 'studentspot/homepage.html')
