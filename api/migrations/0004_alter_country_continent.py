# Generated by Django 3.2.3 on 2021-05-28 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_country_continent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='api.continent'),
        ),
    ]
