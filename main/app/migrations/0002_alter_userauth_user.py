# Generated by Django 4.2.5 on 2023-09-10 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userauth",
            name="user",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.user"
            ),
        ),
    ]
