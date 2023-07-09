from django.forms import ModelForm
from exercises_app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
