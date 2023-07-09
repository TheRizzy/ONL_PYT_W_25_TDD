from django.shortcuts import render, redirect
from django.views import View

from .models import Product
from .forms import ProductForm


class ProductView(View):
    def get(self, request, id_):
        product = Product.objects.get(pk=id_)
        ctx = {
            'name': product.name,
            'description': product.description,
            'price': product.price
        }
        return render(request, 'product.html', ctx)


class AddProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


class ProductsListView(View):
    def get(self, request):
        products = Product.objects.all().order_by('name')
        return render(request, 'products_list.html', {'products': products})
