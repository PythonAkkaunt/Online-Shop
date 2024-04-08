# Generated by Django 5.0.4 on 2024-04-08 11:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='static/uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ism')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Familiya')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Ro'yhatdan o'tgan vaqti")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Manzil sarlavhasi')),
                ('country', models.CharField(max_length=50, verbose_name='Mamlakat')),
                ('province', models.CharField(max_length=50, verbose_name='Viloyat')),
                ('district', models.CharField(max_length=50, verbose_name='Shahar / Tuman')),
                ('street', models.CharField(max_length=50, verbose_name="Ko'cha nomi va uy raqami")),
                ('zip_code', models.IntegerField(verbose_name='Pochta Indeksi')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_images', to='accounts.profile')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.uploadfile')),
            ],
        ),
    ]
