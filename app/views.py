from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Data, Name, ChartType

# Create your views here.
class ChartView(TemplateView):
    template_name = 'app/chart.html'

    def get_context_data(self, **kwargs):
        chartdata = Data.objects.all()
        chartname = Name.objects.all()
        charttype = ChartType.objects.all()

        ctx = {
            'qs': chartdata,
            'name': chartname,
            'type': charttype,
        }
        return ctx