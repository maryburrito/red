import re
from django import template
from django.db.models import Q
from django.urls import NoReverseMatch, reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    request_url_name = context['request'].resolver_match.url_name
    if url_name == request_url_name:
        return 'active'
    return ''

@register.simple_tag(takes_context=True)
def active_if_prefix(context, url_name_prefix):
    request_url_name = context['request'].resolver_match.url_name
    if request_url_name.startswith(url_name_prefix):
        return 'active'
    return ''
