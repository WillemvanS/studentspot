from django.db import models
from django.utils import timezone

class Day(models.Model):
    date = models.DateField(default=timezone.now, auto_now=False, auto_now_add=False, primary_key=True) #The date should not be changed automaticaly and is the primary key of each object a defautl value is mandatory
    status1 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status2 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status3 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status4 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status5 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status6 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status7 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status8 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status9 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status10 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status11 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status12 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status13 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status14 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status15 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status16 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status17 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status18 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status19 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status20 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo

    def __str__(self):
        return self.date.strftime('%d-%m-%Y')
