# Generated by Django 4.2 on 2023-05-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_pro_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='pro',
        ),
    ]
