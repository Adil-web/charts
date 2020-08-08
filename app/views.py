from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Data, Name, ChartType

# Рендеринг chart.html файла
class ChartView(TemplateView):
    template_name = 'app/chart.html'

    #Соеденение с базой данных
    def get_context_data(self, **kwargs):
        chartdata = Data.objects.all()
        first_three_data = chartdata[:3]
        first_six_data = chartdata[:6]
        first_twelve_data = chartdata
        chartname = Name.objects.all()
        charttype = ChartType.objects.all()

        ctx = {
            'otherdata': chartdata,
            'name': chartname,
            'type': charttype,
            'threedata': first_three_data,
            'sixdata': first_six_data,
            'twelvedata': first_twelve_data
        }
        return ctx