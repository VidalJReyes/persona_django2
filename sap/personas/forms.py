from django.forms import ModelForm, EmailInput

from personas.models import Personas


class PersonaForm(ModelForm):
    class Meta:
        model = Personas
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }