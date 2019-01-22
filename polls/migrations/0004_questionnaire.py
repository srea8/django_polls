# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-14 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190112_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionnaire_text', models.CharField(max_length=200)),
                ('pubdate', models.DateField(verbose_name='date published')),
                ('members', models.ManyToManyField(to='polls.Question')),
            ],
        ),
    ]