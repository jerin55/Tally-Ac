# Generated by Django 4.0.5 on 2022-08-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_debit'),
    ]

    operations = [
        migrations.CreateModel(
            name='cred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('credit', models.IntegerField()),
                ('debit', models.IntegerField()),
            ],
        ),
    ]
