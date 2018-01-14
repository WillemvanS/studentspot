from django import template

register = template.Library()

@register.group_tag
def check_group():
   my_group = Group.objects.get(name='Test Huis')
   if my_group in request.user.groups.all():
       return True
