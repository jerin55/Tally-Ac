# Generated by Django 4.0.5 on 2022-09-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_vouchert_credit_alter_vouchert_debit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchert',
            name='credit',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='vouchert',
            name='debit',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
