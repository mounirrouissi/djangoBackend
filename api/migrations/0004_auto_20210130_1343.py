# Generated by Django 3.1.5 on 2021-01-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210130_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places', models.CharField(choices=[('1', '1'), ('2', '2')], default='', max_length=15)),
                ('category', models.CharField(choices=[('enfant', 'enfant'), ('adult', 'adult')], default='', max_length=15)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='festival',
            name='category',
        ),
        migrations.RemoveField(
            model_name='festival',
            name='places',
        ),
        migrations.AlterField(
            model_name='festival',
            name='city',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='festival',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='festival',
            name='status',
            field=models.CharField(default='', max_length=15),
        ),
    ]
