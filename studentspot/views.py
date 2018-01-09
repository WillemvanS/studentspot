from django.shortcuts import render

# Create your views here.

#Renders a html page for show_calendar using the show_calendar.html template
def show_calendar(request):
    return render(request, 'studentspot/show_calendar.html')
