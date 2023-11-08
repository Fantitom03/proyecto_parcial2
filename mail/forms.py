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
        # Completar aqui. Validar que el campo “mail_destinatario” no sea igual al “mail_origen”
        pass
