from django import template

register = template.Library()

@register.filter
def current_username(request):
    return request.user.username