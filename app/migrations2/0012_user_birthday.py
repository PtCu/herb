# Generated by Django 3.0.3 on 2020-09-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190810_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(db_column='userBirthday', null=True),
        ),
    ]