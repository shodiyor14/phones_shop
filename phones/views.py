from django.shortcuts import render
from phones.models import PhonesModel, PhonesTagModel, PhonesModelsCategory, PhonesColorModel, PhonesBrandModel
from django.views.generic import TemplateView, ListView


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['phones'] = PhonesModel.objects.order_by('-pk')[:3]
        return context


class PhonesListView(ListView):
    template_name = 'phones.html'
    queryset = PhonesModel.objects.order_by('-pk')
