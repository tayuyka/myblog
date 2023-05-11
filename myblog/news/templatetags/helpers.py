from django import template
from django.utils.safestring import mark_safe
from bleach import clean

register = template.Library()

@register.filter
def sanitize(value):
    allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'p', 'br']
    cleaned_value = clean(value, tags=allowed_tags, strip=True)
    return mark_safe(cleaned_value)