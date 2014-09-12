from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(needs_autoescape=True, name="bold_tag")
@stringfilter
def bold_tag(tweet, hashtag, autoescape=None):
	if autoescape:
		esc = conditional_escape
	else:
		esc = lambda x: x
	if hashtag[0] != "#":
		hashtag = "#"+hashtag
	result = re.sub(r'\b(#?{0})\b'.format(esc(hashtag)), r'<strong>\g<1></strong>', tweet)
	return mark_safe(result)
