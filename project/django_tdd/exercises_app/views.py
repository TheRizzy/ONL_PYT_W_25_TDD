from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import ProductForm
from .models import Product


class ProductView(View):
    def get(self, request, id_):
        product = get_object_or_404(Product, pk=id_)
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
