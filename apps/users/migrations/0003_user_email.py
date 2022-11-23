# Generated by Django 4.1.3 on 2022-11-23 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(
                default=django.utils.timezone.now, max_length=255, unique=True
            ),
            preserve_default=False,
        ),
    ]
