from django import forms

from .models import Comments
from mptt.forms import TreeNodeChoiceField


class CommentFrom(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comments.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'display': 'none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comments
        fields = ('autor', 'parent', 'text')

