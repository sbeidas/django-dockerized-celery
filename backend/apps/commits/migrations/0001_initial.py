# Generated by Django 2.1.1 on 2021-05-12 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('provider', models.CharField(choices=[('github', 'GitHub'), ('bitbucket', 'BitBucket')], max_length=20)),
                ('status', models.CharField(choices=[('out-of-date', 'Out-of-Date'), ('syncing', 'Syncing'), ('up-to-date', 'Up-to-Date')], default='out-of-date', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='commit',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='commits.Repository'),
        ),
    ]
