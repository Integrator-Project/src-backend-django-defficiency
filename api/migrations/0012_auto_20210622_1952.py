# Generated by Django 3.2.3 on 2021-06-22 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_country_slug_api'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativenamecountry',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='api.country'),
        ),
        migrations.AlterField(
            model_name='alternativenamevaccine',
            name='vaccine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccines', to='api.vaccine'),
        ),
        migrations.AlterField(
            model_name='translationscountry',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='api.country'),
        ),
        migrations.AlterField(
            model_name='vaccineapplication',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='api.country'),
        ),
    ]