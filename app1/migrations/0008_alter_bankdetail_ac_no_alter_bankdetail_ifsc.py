# Generated by Django 4.0.5 on 2022-08-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_bankdetail_ifsc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='ac_no',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='ifsc',
            field=models.IntegerField(null=True),
        ),
    ]
