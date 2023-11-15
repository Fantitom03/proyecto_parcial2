from django import forms
from .models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('mail_origen', 'destinatario', 'asunto', 'cuerpo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Asigna la clase CSS a todos los widgets del formulario
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['mail_origen'].widget.attrs['readonly'] = 'true'

    def clean(self):
        super().clean()
        mail_origen = self.cleaned_data["mail_origen"]
        mail_destinatario = self.cleaned_data["destinatario"]
        if mail_origen == mail_destinatario:
            raise forms.ValidationError("El mail de origen no puede ser igual que el del destinatario")
        pass
