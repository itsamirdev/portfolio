from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from items.models import ItemBox, About, Project
from items.forms import ContactForm


class IndexView(View):
    class_form = ContactForm

    def get(self, request):
        items = ItemBox.objects.filter(is_main_setting=True)
        about = get_object_or_404(About, is_main_setting=True)
        projects = Project.objects.filter(is_main_setting=True)
        form = self.class_form()
        context = {
            'item_box': items,
            'about': about,
            'projects': projects,
            'forms': form
        }
        return render(request, "index.html", context)

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "index.html", {'forms': form})


class AboutView(TemplateView):
    template_name = "about.html"
