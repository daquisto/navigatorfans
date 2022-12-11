from django.forms import ModelForm

from .models import Guitar


class GuitarForm(ModelForm):
    class Meta:
        model = Guitar
        fields = '__all__'
