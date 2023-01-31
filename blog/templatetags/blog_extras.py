from django.contrib.auth import get_user_model
user_model = get_user_model()

from django import template
register = template.Library()


from django.utils.html import escape
from django.utils.safestring import mark_safe



from django.utils.html import format_html

# format_html works similarly to the built in str.format method,
# except each argument is automatically escaped before being interpolated.

@register.filter
def author_details(author, current_user):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)

@register.simple_tag(name="row")
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)
    
@register.simple_tag
def endrow():
    return format_html("</div>")

@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")
