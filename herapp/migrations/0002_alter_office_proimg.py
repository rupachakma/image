# Generated by Django 4.2.5 on 2023-09-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='proimg',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
