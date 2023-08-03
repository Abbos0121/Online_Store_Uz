from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from new_app.models import Product, BasketItem
from .forms import CustomUserCreationForm, ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def profile_view(request):
    user = request.user
    user_info = {
        'username': user.username,
    }
    context = {'user_info': user_info}
    return render(request, 'new_app.html', context)


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Шаблон для страницы входа

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, self.template_name, {'error': 'Неверные учетные данные'})

        return super().post(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class CustomTermsView(CreateView):           #terms.html
    form_class = CustomUserCreationForm
    template_name = 'terms.html'
    success_url = reverse_lazy('terms')


def index_view(request):
    return render(request, 'index.html')


def contact_view(request):
    return render(request, 'contact.html')


def shop_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop.html', context)


def testimonial_view(request):
    return render(request, 'testimonial.html')


def why_view(request):
    return render(request, 'why.html')


def search_results_view(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search_results.html', context)


@login_required
def basket_views(request):
    user = request.user

    basket_items = BasketItem.objects.filter(user=user)

    context = {'basket_items': basket_items}
    return render(request, 'basket.html', context)


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket_item, created = BasketItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        basket_item.quantity += 1
        basket_item.save()

    return redirect('basket')


def remove_from_basket(request, product_id):
    basket_item = get_object_or_404(BasketItem, product__id=product_id, user=request.user)

    basket_item.delete()

    return redirect('basket')


def my_products(request):

    products = Product.objects.filter(user=request.user)

    return render(request, 'my_products.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('my_products')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


@login_required
def delete_product(request, product_id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=product_id, user=request.user)
            product.delete()
            return redirect('my_products')
        except Product.DoesNotExist:
            pass

    return redirect('my_products')

