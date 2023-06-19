# Generated by Django 4.2.2 on 2023-06-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_alter_specialcare_head_c_alter_specialcare_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="specialcare",
            name="length1",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="gest_age",
            field=models.CharField(
                help_text="WW/DDD",
                max_length=255,
                null=True,
                verbose_name="gestational age",
            ),
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="length",
            field=models.CharField(max_length=3, null=True, verbose_name="length (cm)"),
        ),
    ]