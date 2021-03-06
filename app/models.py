from colorfield.fields import ColorField
from django.db import models

# Объект charts_types для выбора типа в chart js
charts_types = {
    ("line", "line"),
    ("bar", "bar"),
    ("radar", "radar"),
    ("doughnut", "doughnut"),
    ("pie", "pie"),
    ("polarArea", "polarArea"),
    ("bubble", "bubble"),
    ("scatter", "scatter"),
    ("horizontalBar", "horizontalBar")
}

# База данных для имени диаграммы
class Name(models.Model):
    name = models.CharField(max_length=220, default='chart')

    class Meta:
        verbose_name = "Chart name"
        verbose_name_plural = "Chart name"

    def __str__(self):
        return "{}".format(self.name)

# База данных для выбора типа диаграммы
class ChartType(models.Model):
    chartType = models.CharField(
        max_length=20,
        choices=charts_types,
        default="line",
    )

    class Meta:
        verbose_name = "Chart type"
        verbose_name_plural = "Chart type"

    def __str__(self):
        return "{}".format(self.chartType)


# База данных для labels, data, bgcolor, borderColor
class Data(models.Model):
    labels = models.CharField(max_length=220)
    data = models.IntegerField()
    backgroundColor = ColorField(default='#FF0000')
    borderColor = ColorField(default='#FF0000')

    def __str__(self):
        return "{}".format(self.labels)