# Generated by Django 4.2.2 on 2023-06-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_remove_specialcare_fio_specialcare_fio2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialcare",
            name="head_c",
            field=models.CharField(
                max_length=3, null=True, verbose_name="head circumference (cm)"
            ),
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="weight",
            field=models.CharField(max_length=4, null=True, verbose_name="weight (g)"),
        ),
    ]
