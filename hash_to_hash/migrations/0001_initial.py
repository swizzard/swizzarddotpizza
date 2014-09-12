# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('baseline', models.BooleanField(default=False)),
                ('hashtags', models.ManyToManyField(to='hash_to_hash.Hashtag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag', models.ForeignKey(to='hash_to_hash.Hashtag', to_field=u'id')),
                ('cluster', models.ForeignKey(to='hash_to_hash.Cluster', to_field=u'id')),
                ('nos', models.IntegerField(default=0)),
                ('seen', models.IntegerField(default=0, verbose_name='times_seen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
