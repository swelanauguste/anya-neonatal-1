# Generated by Django 4.2.2 on 2023-06-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_specialcare_transport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialcare",
            name="sip",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No")],
                default="Y",
                max_length=1,
                verbose_name="SIP",
            ),
        ),
    ]
