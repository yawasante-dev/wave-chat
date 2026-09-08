from django import template

register = template.Library()

@register.filter
def avatar_color(username):
    return sum(ord(c) for c in username) % 8