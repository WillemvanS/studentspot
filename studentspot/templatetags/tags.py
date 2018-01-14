from django import template

register = template.Library()

@register.simple_tag
def check_group():
   my_group = Group.objects.get(name='Test Huis')
   if my_group in request.user.groups.all():
       return True

def is_member(user):
    return user.groups.filter(name='Test Huis').exists()
