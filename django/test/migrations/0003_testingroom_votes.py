# Generated by Django 5.0.3 on 2024-03-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_alter_testingroom_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingroom',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]