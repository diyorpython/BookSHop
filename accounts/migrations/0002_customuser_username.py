# Generated by Django 4.1.4 on 2023-01-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
