from django import forms

from blog.models import Comment


from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
#FormHelper               
# form_method: Set the form method, GET or POST. It defaults to POST. If set to POST, then the crispy template tag will automatically render the CSRF token in the form.
# form_action: If you want the form to submit to a different page than the one on which it was loaded, you can set the URL, path, or URL name to this attribute.
# form_id: The value to set as the id attribute of the <form> tag.
# form_class: The value to set as the class attribute of the <form> tag.
# attrs: A dictionary of attributes to set on the <form> tag.            