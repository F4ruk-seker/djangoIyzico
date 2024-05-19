# Generated by Django 5.0.6 on 2024-05-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('item_type', models.CharField(choices=[('P', 'physical'), ('v', 'virtual')], default='P', max_length=1)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]