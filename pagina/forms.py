from django import forms
from .models import Producto, ProductoCaracteristica
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column, Row, Field, Div
from crispy_bootstrap5.bootstrap5 import FloatingField, Switch, Accordion
from django.contrib.auth.forms import AuthenticationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'marca', 'categoria']
    
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
        fields = ['producto', 'caracteristica', 'descripcion_caract']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            FloatingField("caracteristica"),
            FloatingField("descripcion_caract")
        )
