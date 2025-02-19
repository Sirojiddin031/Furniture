from django.views.generic import TemplateView
from .models import About, AboutModel, AboutCategoryModel



class AboutView(TemplateView):
    template_name = 'pages/about-us.html'
    model = AboutModel
    context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = AboutCategoryModel.objects.all()
        return context
    
def about_view(request):
    about = About.objects.all()
    print(about)
    context = {
        'about': about
    }
    return render(request, 'about.html', context)