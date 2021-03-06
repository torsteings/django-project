# Generated by Django 3.1.2 on 2021-05-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('open_price', models.DecimalField(decimal_places=15, max_digits=20)),
                ('low_price', models.DecimalField(decimal_places=15, max_digits=20)),
                ('profit', models.DecimalField(decimal_places=15, max_digits=20)),
                ('risk', models.DecimalField(decimal_places=15, max_digits=20)),
                ('new_candidate', models.CharField(max_length=10)),
            ],
        ),
    ]
