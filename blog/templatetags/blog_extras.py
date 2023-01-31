from django.contrib.auth import get_user_model
user_model = get_user_model()

from django import template
register = template.Library()


from django.utils.html import escape
from django.utils.safestring import mark_safe



# @register.filter(name="author_name")
# def author_details(author):
#     #if it is in wrong type 
#     if not isinstance(author, user_model):
#         # return empty string as safe default
#         return ""
#     # Now we know the whole string is safe to be marked 
#     #as safe, because it’s composed only of HTML that we’ve defined,
#     #and all user supplied data is escaped.

#     if author.first_name and author.last_name:
#         name = escape(f"{author.first_name} {author.last_name}")
#     else:
#         name = escape(f"{author.username}")
#     # return name
#     if author.email:
#         email = author.email
#         prefix = f'<a href="mailto:{email}">'
#         suffix = "</a>"
#     else:
#         prefix = ""
#         suffix = ""

#     return mark_safe(f"{prefix}{name}{suffix}")



from django.utils.html import format_html

# format_html works similarly to the built in str.format method,
# except each argument is automatically escaped before being interpolated.

@register.filter(name="author_name")
def author_details(author,current_user=None):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")# marked as safe 


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