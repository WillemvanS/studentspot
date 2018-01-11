from django.shortcuts import render
from django.utils import timezone
from .models import Day, House

# Create your views here.
days_forward = 7 #how many days the calendar should show
#Renders a html page for show_calendar using the show_calendar.html template and the selected days
def show_calendar(request):
    days = (Day.objects.filter(date__lte=(timezone.now() + timezone.timedelta(days=days_forward)))).filter(date__gte=timezone.now()).order_by('date')
    houses = (House.objects.filter(houseName="Group_9"))
    return render(request, 'studentspot/show_calendar.html', {'days': days, 'houses' : houses})
