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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=255, verbose_name='office')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
            ],
            options={
                'verbose_name_plural': 'offices',
                'verbose_name': 'office',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('surname', models.CharField(max_length=255, verbose_name='surname')),
                ('gender', models.CharField(max_length=255, choices=[('M', 'Male'), ('F', 'Female')], verbose_name='gender')),
                ('security_level', models.PositiveIntegerField(verbose_name='security level')),
                ('some_excluded_field', models.DecimalField(max_digits=10, null=True, verbose_name='some decimal', decimal_places=3)),
                ('office', models.ForeignKey(null=True, to='app.Office', blank=True)),
            ],
            options={
                'verbose_name_plural': 'persons',
                'verbose_name': 'person',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='tag')),
            ],
            options={
                'verbose_name_plural': 'tags',
                'verbose_name': 'tag',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
            preserve_default=True,
        ),
    ]