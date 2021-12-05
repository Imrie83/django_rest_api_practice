# Generated by Django 3.0.6 on 2021-12-03 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Screening time')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movielist.Cinema', verbose_name='Cinem')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movielist.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='movies',
            field=models.ManyToManyField(through='movielist.Screening', to='movielist.Movie'),
        ),
    ]