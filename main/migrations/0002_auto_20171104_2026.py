# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-04 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=30, null=True)),
                ('score_increment', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('text', models.CharField(max_length=256)),
                ('node_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('twitter_name', models.CharField(max_length=30, null=True)),
                ('twitter_handle', models.CharField(max_length=30, null=True)),
                ('twitter_id', models.CharField(max_length=30, null=True)),
                ('facebook_name', models.CharField(max_length=30, null=True)),
                ('facebook_id', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=130, null=True)),
                ('zipcode', models.CharField(max_length=130, null=True)),
                ('phone_number', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('email2', models.EmailField(max_length=254, null=True)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='People',
        ),
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person'),
        ),
    ]