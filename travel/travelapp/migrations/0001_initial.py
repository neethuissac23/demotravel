# Generated by Django 4.2b1 on 2023-03-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.FileField(upload_to='pics/')),
                ('desc', models.TextField()),
            ],
        ),
    ]