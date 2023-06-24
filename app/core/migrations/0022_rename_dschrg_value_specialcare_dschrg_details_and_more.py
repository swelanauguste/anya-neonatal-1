# Generated by Django 4.2.2 on 2023-06-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0021_rename_surg_other_value_specialcare_surg_other_details"),
    ]

    operations = [
        migrations.RenameField(
            model_name="specialcare",
            old_name="dschrg_value",
            new_name="dschrg_details",
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="at_36_wks_ga",
            field=models.CharField(
                blank=True,
                help_text="Copy growth/GA graph",
                max_length=25,
                null=True,
                verbose_name="at 36 weeks GA",
            ),
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="blood_prods_vol",
            field=models.CharField(
                blank=True,
                help_text="ml vol total",
                max_length=4,
                null=True,
                verbose_name="blood products Volume",
            ),
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="dschrg",
            field=models.CharField(
                choices=[("L", "Live"), ("D", "Dead"), ("T", "Transfer")],
                default="L",
                max_length=2,
                verbose_name="discharge",
            ),
        ),
        migrations.AlterField(
            model_name="specialcare",
            name="dschrg_post_mort",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No")],
                default="Y",
                max_length=2,
                verbose_name="post mortem",
            ),
        ),
    ]
