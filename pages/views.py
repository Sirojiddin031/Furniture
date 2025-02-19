from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from products.models import ProductModel
from .models import AboutModel

from pages.forms import ContactForm

def home_view(request):
    products = ProductModel.objects.all()  # Mahsulotlarni olish
    return render(request, 'home.html', {'products': products})

def home_page_view(request):
    return render(request, 'home.html')


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    # success_url = reverse_lazy('pages:contact')

    def get_success_url(self):
        return reverse_lazy('pages:contact')

    def form_valid(self, form):
        messages.success(self.request, _('Your contact information is sent'))
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors:
            messages.error(self.request, error)
        return super().form_invalid(form)


def about_view(request):
    # AboutModel dan barcha ma'lumotlarni olish
    posts = AboutModel.objects.all()
    
    # Context orqali template ga uzatish
    context = {
        'posts': posts  # template da ishlatgan o'zgaruvchi nomi
    }
    
    return render(request, 'about.html', context)