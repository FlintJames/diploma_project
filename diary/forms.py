from django.forms import ModelForm, BooleanField

from diary.models import Entry


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class EntryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Entry
        exclude = ('views_counter', 'owner', 'number_of_views', 'publication_sign',)
