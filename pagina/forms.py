from django import forms
from .models import Producto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column, Row, Field, Div
from crispy_bootstrap5.bootstrap5 import FloatingField, Switch, Accordion

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