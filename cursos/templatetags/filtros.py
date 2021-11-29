<<<<<<< HEAD
from django import template

register = template.Library()

@register.filter
def return_list(value, arg):
=======
from django import template

register = template.Library()

@register.filter
def return_list(value, arg):
>>>>>>> 1651482b46c304b36ab1d5056382003c08636891
    return [i for i in range(int(arg))]