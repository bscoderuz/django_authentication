# Generated by Django 4.1.5 on 2023-01-13 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_address_user_auth_type_user_bio_user_sex_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('verify_type', models.CharField(choices=[('manager', 'manager'), ('via_email', 'via_email')], max_length=31)),
                ('expiration_time', models.DateTimeField(null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]