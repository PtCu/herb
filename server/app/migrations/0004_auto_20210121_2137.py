# Generated by Django 3.0.3 on 2021-01-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210121_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='isShow',
            field=models.CharField(choices=[('是', '是'), ('否', '否')], default='否', max_length=20, verbose_name='是否允许发布'),
        ),
    ]