from django import forms
from .models import Producto, ProductoCaracteristica, Caracteristica, Categoria, Marca
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column, Row, Field, Div
from crispy_bootstrap5.bootstrap5 import FloatingField, Switch, Accordion
from django.contrib.auth.forms import AuthenticationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'marca', 'categoria']
        widgets = {
            'precio': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'stock': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''} 
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-success'))

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'validacion-no-color'
        self.helper.attrs = { 'novalidate': '' }
        self.helper.layout = Layout(
            FloatingField('username'),
            FloatingField('password'),
            Submit('submit', 'Iniciar Sesión', css_class="btn-success")
        )

class ProductoCaracteristicaForm(forms.ModelForm):
    class Meta:
        model = ProductoCaracteristica
        fields = ['caracteristica', 'descripcion_caract']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            FloatingField("caracteristica"),
            FloatingField("descripcion_caract"),
            Submit('submit', 'Guardar', css_class='btn-success')
        )

class CaracteristicaForm(forms.ModelForm):
    class Meta:
        model = Caracteristica
        fields = ['nomb_caracteristica']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-success'))

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nomb_marca']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-success'))
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nomb_categoria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-success'))