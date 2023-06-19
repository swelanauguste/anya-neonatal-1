# Generated by Django 4.2.2 on 2023-06-16 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_transport_remove_specialcare_trans_air_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="specialcare",
            name="trans_land",
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="transport",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="core.transport",
            ),
        ),
    ]