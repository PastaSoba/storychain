# Generated by Django 2.1.7 on 2019-05-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storybone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttext', models.TextField(max_length=100)),
                ('lasttext', models.TextField(max_length=100)),
            ],
        ),
    ]
