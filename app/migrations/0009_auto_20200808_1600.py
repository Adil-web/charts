# Generated by Django 3.0.8 on 2020-08-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200807_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charttype',
            options={'verbose_name': 'Chart type', 'verbose_name_plural': 'Chart type'},
        ),
        migrations.AlterModelOptions(
            name='name',
            options={'verbose_name': 'Chart name', 'verbose_name_plural': 'Chart name'},
        ),
        migrations.AlterField(
            model_name='charttype',
            name='chartType',
            field=models.CharField(choices=[('bar', 'bar'), ('doughnut', 'doughnut'), ('bubble', 'bubble'), ('pie', 'pie'), ('radar', 'radar'), ('polarArea', 'polarArea'), ('horizontalBar', 'horizontalBar'), ('scatter', 'scatter'), ('line', 'line')], default='line', max_length=20),
        ),
    ]