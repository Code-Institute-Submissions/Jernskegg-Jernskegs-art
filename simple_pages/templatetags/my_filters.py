'''
This adds the ability to add classes to forms.
add {% load my_filters %} to html to load these filters
then in your form fields you can add "addclass" to add
your own css eg.{{ field |add_class:'css-selector'}}
'''

from django import template
register = template.Library()


@register.filter(name='add_class')
def addclass(value, arg):
    ''' returns the inputed "css" to the html and renders it'''
    return value.as_widget(attrs={'class': arg})
