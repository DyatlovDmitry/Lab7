# Generated by Django 4.0.4 on 2022-06-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_post_is_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_liked',
            field=models.BooleanField(verbose_name=False),
        ),
    ]