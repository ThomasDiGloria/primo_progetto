# Generated by Django 5.1.3 on 2025-01-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_articolo_visualizzazioni'),
    ]

    operations = [
        migrations.AddField(
            model_name='giornalista',
            name='anno_di_nascita',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='articolo',
            name='visualizzazioni',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
