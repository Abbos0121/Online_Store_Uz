from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .models import Product


@login_required(login_url='login/')
def profile_view(request):
    myproducts = Product.objects.all().values()

    template = loader.get_template('new_app.html')
    context = {
        'myproducts': myproducts,
    }
    return HttpResponse(template.render(context, request))



