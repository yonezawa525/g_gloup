# Generated by Django 4.2.2 on 2023-06-29 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_id', models.IntegerField()),
                ('log_meisai', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('lastlogin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserClass',
            fields=[
                ('class_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
                ('class_tanto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('status_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userpost_date', models.DateField()),
                ('userpost_coment', models.CharField(max_length=1050)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toukou.userstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toukou.user')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=255)),
                ('user_tall', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='toukou.user')),
            ],
        ),
    ]
