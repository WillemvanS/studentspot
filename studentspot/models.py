from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    teststatus = models.ForeignKey(Slot)

    def __str__(self):
        return self.date.strftime('%d-%m-%Y')

class Slot(models.Model):
    student = models.ForeignKey(User)
    day = models.ForeignKey(Day)
    slot = models.CharField(max_length=3, default='enm')

class House(models.Model):
    houseName = models.CharField(max_length=50, default='house', primary_key=True) #The date should not be changed automaticaly and is the primary key of each object a defautl value is mandatory
    days_forward = models.PositiveIntegerField(default=20)
    student1 = models.CharField(max_length=20, default='empty')
    student2 = models.CharField(max_length=20, default='empty')
    student3 = models.CharField(max_length=20, default='empty')
    student4 = models.CharField(max_length=20, default='empty')
    student5 = models.CharField(max_length=20, default='empty')
    student6 = models.CharField(max_length=20, default='empty')
    student7 = models.CharField(max_length=20, default='empty')
    student8 = models.CharField(max_length=20, default='empty')
    student9 = models.CharField(max_length=20, default='empty')
    student10 = models.CharField(max_length=20, default='empty')
    student11 = models.CharField(max_length=20, default='empty')
    student12 = models.CharField(max_length=20, default='empty')
    student13 = models.CharField(max_length=20, default='empty')
    student14 = models.CharField(max_length=20, default='empty')
    student15 = models.CharField(max_length=20, default='empty')
    student16 = models.CharField(max_length=20, default='empty')
    student17 = models.CharField(max_length=20, default='empty')
    student18 = models.CharField(max_length=20, default='empty')
    student19 = models.CharField(max_length=20, default='empty')
    student20 = models.CharField(max_length=20, default='empty')
    def __str__(self):
        return self.houseName

class UserPlus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status1 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status2 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status3 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status4 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status5 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status6 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo
    status7 = models.CharField(max_length=3, default='enm') #Should be either ewm, enm or koo

    @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
