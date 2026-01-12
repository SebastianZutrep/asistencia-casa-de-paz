from django import forms
from .models import Integrante, Reunion, Asistencia

class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'tipo',
            'telefono',
            'email',
            'direccion',
            'sexo',
            'rol',
            'activo'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección de residencia'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-control'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class ReunionForm(forms.ModelForm):
    class Meta:
        model = Reunion
        fields = ['fecha', 'tema', 'maestro', 'tipo']
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'tema': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tema de la reunión'
                }
            ),
            'maestro': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['maestro'].queryset = Integrante.objects.filter(rol__in=['Maestro', 'Lider'])

        for field in self.fields.values():
            if not field.widget.attrs.get('class'):
                field.widget.attrs['class'] = 'form-control'

        # Opcional: placeholders elegantes
        self.fields['fecha'].label = "Fecha"
        self.fields['tema'].label = "Tema"
        self.fields['maestro'].label = "Maestro / Líder"
        self.fields['tipo'].label = "Tipo de reunión"

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['integrante', 'presente', 'comentario']  
        widgets = {
            'integrante': forms.HiddenInput(),  # importante, no mostrar en la tabla
            'presente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comentario'}),
        }