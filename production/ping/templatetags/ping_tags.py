from django import template

register = template.Library()


@register.filter(name='checkBlank')
def checkBlank(string):

    if string is None:
        return ''

    return string
