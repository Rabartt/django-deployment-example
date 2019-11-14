from django import template

register =template.Library()

# another way to register the function or put a name from which we gonna call it
# on templates is using decorators!

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')

# register.filter('cut', cut)
