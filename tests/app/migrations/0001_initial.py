# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('office', models.CharField(verbose_name='office', max_length=255)),
                ('address', models.CharField(verbose_name='address', max_length=255)),
            ],
            options={
                'verbose_name': 'office',
                'verbose_name_plural': 'offices',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('surname', models.CharField(verbose_name='surname', max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], verbose_name='gender', max_length=255)),
                ('security_level', models.PositiveIntegerField(verbose_name='security level')),
                ('some_excluded_field', models.DecimalField(max_digits=10, verbose_name='some decimal', null=True, decimal_places=3)),
                ('office', models.ForeignKey(blank=True, null=True, to='app.Office')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='tag', max_length=255)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
