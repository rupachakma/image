# Generated by Django 4.2.5 on 2023-09-22 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herapp', '0002_alter_office_proimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='proimg',
            new_name='profileImg',
        ),
    ]