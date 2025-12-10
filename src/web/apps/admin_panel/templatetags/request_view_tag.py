from django import template
import json

register = template.Library()


@register.filter(name='startswith')
def startswith(text, starts):
    if isinstance(text, str):
        return any(text.startswith(s) for s in starts.split(','))
    return False

@register.filter('to_json')
def to_json(ls_string):
    return json.dumps(ls_string)
