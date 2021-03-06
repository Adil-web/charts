# Generated by Django 3.0.8 on 2020-08-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200807_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='chartType',
            field=models.CharField(choices=[('radar', 'radar'), ('line', 'line'), ('polar area', 'polarArea'), ('doughnut', 'doughnut'), ('bar', 'bar'), ('scatter', 'scatter'), ('pie', 'pie'), ('bubble', 'bubble')], default='line', max_length=20),
        ),
        migrations.AlterField(
            model_name='data',
            name='labels',
            field=models.CharField(max_length=220),
        ),
    ]
