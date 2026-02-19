from multiprocessing import context
from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "About us - Online Store",
                "subtitle": "About us",
                "description": "This is an about page ...",
                "author": "Developed by: David Curelop",
            }
        )
        return context


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Contact us - Online Store",
                "subtitle": "Contact Information",
                "email": "abc@example.com",
                "phone": "+57 1234567890",
                "address": "Calle 123, Medellin, Colombia",
            }
        )
        return context


class ProductIndexView(View):
    template_name = "products/index.html"

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.objects.all()
        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = "products/show.html"

    def get(self, request, id):
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Product, pk=product_id)

        except (ValueError, IndexError):
            return HttpResponseRedirect("/")

        viewData = {}
        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.name + " - Online Store"
        viewData["subtitle"] = product.name + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)


class ProductCreateView(View):
    template_name = "products/create.html"

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid() and form.cleaned_data["price"] > 0:
            Product.products.append(
                {
                    "id": str(len(Product.products) + 1),
                    "name": form.cleaned_data["name"],
                    "description": "New product",
                    "price": form.cleaned_data["price"],
                }
            )
            return redirect("productCreated")
        else:
            if form.cleaned_data["price"] <= 0:
                form.add_error("price", "El precio no debe ser menor o igual que 0")
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)


class ProductCreatedView(TemplateView):
    template_name = "products/productCreated.html"


class ProductListView(ListView):

    model = Product

    template_name = "product_list.html"

    context_object_name = (
        "products"  # This will allow you to loop through 'products' in your template
    )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["title"] = "Products - Online Store"

        context["subtitle"] = "List of products"

        return context
