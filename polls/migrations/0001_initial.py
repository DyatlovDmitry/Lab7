# Generated by Django 4.0.4 on 2022-05-07 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_heading', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
            ],
        ),
        # migrations.CreateModel(
        #     name='Like',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.post')),
        #     ],
        # ),
    ]
